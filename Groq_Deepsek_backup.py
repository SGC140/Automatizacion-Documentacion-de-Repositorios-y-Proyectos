import os
import time
import google
from google import genai
from google.genai import types
from openai import OpenAI
from dotenv import load_dotenv
from github import Github, Auth

load_dotenv(override=True)

Git_TOKEN = os.getenv("GIT_TOKEN")
auth = Auth.Token(Git_TOKEN)
Git = Github(auth=auth)
Git_User = Git.get_user() 

Groq_API = os.getenv("GROQ_KEY")
Groq_user = OpenAI(
    api_key=Groq_API,
    base_url="https://api.groq.com/openai/v1"
)

def consultar_ia(prompt, instrucciones):

    respuesta = Groq_user.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        temperature=0.3,
        messages=[
            {
                "role": "system",
                "content": instrucciones
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return respuesta.choices[0].message.content

with open("Consolidado_Documentación.txt", "r") as Historico:
    Repos_documentados = Historico.read().split("\n")

print(f"Lista de Repos documentados: {Repos_documentados}")

Repos = Git_User.get_repos()
for repo in Repos:
    print(f"Documentando el Repositorio: {repo.name}")

    acumulated_script = ""
    elementos = repo.get_contents("")
    if repo.name in Repos_documentados:
        print(f"Saltando {repo.name} porque ya fue documentado")
        continue
    else:
        while elementos:
            archivo = elementos.pop(0)

            if archivo.type == "dir":
                elementos.extend(repo.get_contents(archivo.path))
            elif archivo.name.endswith(('.py', '.sql', '.ipynb', '.json')):
                try:
                    contenido = archivo.decoded_content.decode("utf-8")
                    acumulated_script += f"\n\n### Archivo: {archivo.path} ###\n{contenido}"
                except Exception as error:
                    print(f"No se puedo documentar el archivo {archivo.name}: {error}")
        
        if not acumulated_script:
            print(f"saltando {repo.name}")
            continue
        
        instrucciones = """Eres un Senior Data Analyst & Automation Analyst. Crea un README.md profesional, exhaustivo y estructurado para este repositorio basándote en el código proporcionado.
        Usa Markdown y cumple estrictamente con los siguientes requisitos:
        1. Incluye 'Badges' (escudos) estéticos al inicio, y si pueden llevar los links de la documentación, mejor. IMPORTANTE: NO INCLUYAS LAS VERSIONES, SOLO LA TECNOLOGÍA (ej. versión de Python, licencia, estado del proyecto).
        1.1 Si puedes incluir imágenes de los badges, bien, si no pues no. Es importante aclarar que si tienes que documentar proyectos de SQL es BigQuery
        2. Agrega un Índice (Table of Contents) navegable con enlaces ancla a cada sección para mejorar la experiencia del desarrollador.
        3. Explica la arquitectura, las dependencias y la lógica principal con su respectivo payload y pipeline.
        4. En la sección de configuración, especifica explícitamente si se requieren dependencias a nivel de sistema operativo (ej. instalación de FFmpeg, Tesseract, controladores, etc.), no solo las librerías del lenguaje de programación usado.
        5. Si el código genera salidas de datos estructurados (JSON, diccionarios, CSV), incluye un pequeño bloque de código de ejemplo mostrando la estructura esperada de esa salida para ilustrar los resultados.
        6. Sé muy técnico y preciso al detallar las tecnologías y el valor agregado frente a otras soluciones (siempre y cuando no incluya información sensible, empresarial-confidencial o personal), enfatizando el porqué del uso de ciertas librerías. Segmenta el código para explicar las partes fundamentales.
        7. NO reveles datos sensibles, credenciales, tokens o IDs específicos, direcciones, nombres, contactos bajo ninguna circunstancia. Si existen nombres propios remplácelos por genéricos o cosas como "Usuario 1/Persona 1/Empresa 1" Y cosas así
        8. Mantén un tono puramente técnico, analítico y directo. NO USES EMOJIS EN NINGUNA PARTE DEL README. Evita la adulación y NO escribas con el estilo de LinkedIn (evita abusar de oraciones adversativas o frases cliché).
        9. Responde las preguntas de negocio, destaca el valor agregado del código, destaca lo que se muestra, lo que permite medir, lo que permite diagnósticar, lo que permite resolver, acotar, optimizar, estandarizar y repensar (ahonda mucho en esta cuestión)"""
        
        prompt = f"""Genera el README.md final para este proyecto aplicando todas las directrices de estructura solicitadas (badges, índice, requisitos de SO, ejemplos de salida). 
        Aquí está el código fuente (está acumulado en un solo bloque, así que analízalo detalladamente por ruta de archivo para entender la integración). Del mismo modo, responde las necesidades de negocio, de la investigación :\n\n{acumulated_script}"""

        max_intentos = 5
        respuesta = None

        for intento in range(max_intentos):
            try:
                respuesta = consultar_ia(prompt, instrucciones)
                break
            except Exception as error_api:
                print(f"Servidor saturado o error: {error_api}")
                if intento < max_intentos - 1:
                    print("Esperando 60 segundos antes de reintentar...")
                    time.sleep(60)
                else:
                    print(f"Se agotaron los reintentos para {repo.name}. Saltando...")

        if not respuesta:
            continue

        readme_final = respuesta
        ruta_readme = "README.md"
        readme_path = "README_English.md"
        commit = f"Docs: Autogenerado y automatizado README con agentes contextualizados con códigos iterativos para {repo.name}"
        english_commit = f"Docs: Auto-generated and automated README with contextualized agents with iterative codes for {repo.name}"

        time.sleep(15)

        instrucciones_traductor = f"Eres un Senior Data Analyst & Automation Analyst experto y adicional a ello eres un traductor experto en lenguaje técnico del ámbito tech (SOLO DEBES GENERAR EL README, NADA MÁS)."

        prompt_traduccion = f"""Genera la traducción, al inglés, de esta documentación generada para un Readme.md de repositorios: {respuesta}. 
        Es importante que mantengas la literalidad del mensaje pero también las condiciones contextuales de la gramática anglosajona. 
        Respeta los nombre originales de las variables y en el contexto explica su propósito, de ser necesario. Abstente solo de traducir, no quiero nada más, solo debes traducir y ya. No quiero observaciones tuyas, comentarios ni nada, solo traduce"""

        answer = None

        for intento in range(max_intentos):
            try:
                print(f"Traduciendo README (Intento {intento + 1}/{max_intentos})...")
                answer = consultar_ia(prompt_traduccion, instrucciones_traductor)
                break
            except Exception as error_api:
                print(f"Servidor saturado en traduccion: {error_api}")
                if intento < max_intentos - 1:
                    print("Esperando 60 segundos antes de reintentar...")
                    time.sleep(60)
                else:
                    print(f"Fallo la traduccion para {repo.name}.")

        if not answer:
            continue

        english_readme = answer

        try:
            archivo_md_existente = repo.get_contents(ruta_readme)
            repo.update_file(ruta_readme, commit, readme_final, archivo_md_existente.sha)
            print(f"Readme del repo: {repo.name} actualizado con éxito.")
        except:
            repo.create_file(ruta_readme, commit, readme_final)
            print(f"Readme del repo: {repo.name} creado con éxito.")

        time.sleep(5)

        try:
            file_md = repo.get_contents(readme_path)
            repo.update_file(readme_path, english_commit, english_readme, file_md.sha)
            print(f"Readme from repo: {repo.name} updated succesfully.")
        except:
            repo.create_file(readme_path, english_commit, english_readme)
            print(f"Readme from repo: {repo.name} created succesfully.")
        
        with open("Consolidado_Documentación.txt", "a") as Documento:
            Documento.write("\n"+repo.name)

        time.sleep(5)
        

print("Documentación creada/actualizada y finalizada con éxito")