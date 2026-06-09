import os
import time
import google
from google import genai
from google.genai import types
from dotenv import load_dotenv
from github import Github, Auth

load_dotenv(override=True)

Git_TOKEN = os.getenv("GIT_TOKEN")
auth = Auth.Token(Git_TOKEN)
Git = Github(auth=auth)
Git_User = Git.get_user() 

Gemini_API = os.getenv("API_GEMINI_KEY")
AI_User = genai.Client(api_key=Gemini_API)


Repos = Git_User.get_repos()
for repo in Repos:
    print(f"Documentando el Repositorio: {repo}")

    acumulated_script = ""
    elementos = repo.get_contents("")

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
    
    instrucciones = """Eres un Senior Data Analyst & Automation Analyst. Crea un README.md profesional para este repositorio basándote en el código. 
    Usa Markdown, explica la arquitectura, las dependencias y la lógica principal. No reveles datos sensibles (muy importante esto). Y no escribas 
    como escriben en Linkedin, evita abusar de las oraciones adversativas (frases tipo LinkedIn). Sé muy técnico y muy preciso a la hora de detallar las tecnologías, al igual que
    el valor agregado de este código a diferencia de otros en el mercado, detalla la estructura, enfatiza las librerías y el porqué de su uso, segmenta el código para explicar
    las partes más fundamentales sin ser adulador sino, más bien, técnico."""
    
    prompt = f"Genera el README.md para este proyecto. Aquí está el código fuente (como puedes ver, está acumulado, entonces léelo bien):\n{acumulated_script}"

    respuesta = AI_User.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=instrucciones,
            temperature=0.3
        )
    )

    readme_final = respuesta.text
    ruta_readme = "README.md"
    readme_path = "README_English.md"
    commit = f"Docs: Autogenerado y automatizado README con agentes contextualizados con códigos iterativos para {repo.name}"
    english_commit = f"Docs: Auto-generated and automated README with contextualized agents with iterative codes for {repo.name}"

    time.sleep(15)

    instrucciones_traductor = f"Eres un Senior Data Analyst & Automation Analyst experto y adicional a ello eres un traductor experto en lenguaje técnico del ámbito tech."

    prompt_traduccion = f"""Genera la traducción, al inglés, de esta documentación generada para un Readme.md de repositorios: {respuesta.text}. 
    Es importante que mantengas la literalidad del mensaje pero también las condiciones contextuales de la gramática anglosajona. 
    Respeta los nombre originales de las variables y en el contexto explica su propósito, de ser necesario"""

    answer = AI_User.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_traduccion,
        config=types.GenerateContentConfig(
            system_instruction=instrucciones_traductor,
            temperature=0.3
        )
    )

    english_readme = answer.text

    try:
        archivo_md_existente = repo.get_contents(ruta_readme)
        repo.update_file(ruta_readme, commit, readme_final, archivo_md_existente.sha)
        print(f"Readme del repo: {repo.name} actualizado con éxito.")
    except:
        repo.create_file(ruta_readme, commit, readme_final)
        print(f"Readme del repo: {repo.name} creado con éxito.")

    time.sleep(5)

    #Inglés:

    try:
        file_md = repo.get_contents(readme_path)
        repo.update_file(readme_path, english_commit, english_readme, file_md.sha)
        print(f"Readme from repo: {repo.name} updated succesfully.")
    except:
        repo.create_file(readme_path, english_commit, english_readme)
        print(f"Readme from repo: {repo.name} created succesfully.")



    time.sleep(5)
    break

print("Documentación creada/actualizada y finalizada con éxito")