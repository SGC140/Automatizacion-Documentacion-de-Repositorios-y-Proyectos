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

Gemini_API = os.getenv("API_GEMINI_KEY")
Gemini_API_2 = os.getenv("ANOTHER_API_KEY")
AI_User = genai.Client(api_key=Gemini_API)

Modelo_1 = 'gemini-3.5-flash'
Modelo_2 = 'gemini-2.5-flash'
Modelo_3 = 'gemini-3.0-flash'

Consolidado_Readmes = ""
Repositorios = Git_User.get_repos()

Separador = "="*60

for repo in Repositorios:
    READMES = repo.get_contents("README.md")
    Contenido = READMES.decoded_content.decode("utf-8")
    Consolidado_Readmes += f"{Separador}\nLink del Repositorio Asociado: https://github.com/SGC140/{repo.name}\n{Separador}\n{Contenido}"

#with open("Consolidado_Readmes.txt", "w", encoding="utf-8") as Consolidado:
    #Consolidado.write(Consolidado_Readmes)

def consolidado_GENAI(User_API_KEY, Nombre_Modelo, Instrucciones, Prompt):

    client = genai.Client(api_key=User_API_KEY)
    Max_Intentos = 20
    Max_Intentos += 1
    for intento in range(Max_Intentos):
        try:
            Respuesta = client.models.generate_content(
                model=Nombre_Modelo,
                contents=Prompt,
                config=types.GenerateContentConfig(
                    system_instruction=Instrucciones,
                    temperature=0.3
                ) 
            )

            return Respuesta.text
        
        except Exception as error:
            if intento < Max_Intentos:
                print("Reintentado en 60 segundos")
                time.sleep(60)
            else:
                print("Límite de intentos superados")
                return None


instrucciones = """
Actúa como un Principal Data Analyst & Automation Architect. Tu tarea es redactar un README.md de Portafolio Maestro altamente profesional, técnico y optimizado, basándote en el consolidado de repositorios provisto.

REGLA DE ORO (Optimización de Tokens y Lectura): 
NO generes secciones largas para cada repositorio. Concentra el análisis profundo de tus habilidades, tecnologías y arquitecturas en la sección de "Perfil y Capacidades". La sección de "Proyectos" debe ser un catálogo conciso.

Estructura obligatoria del documento (usa Markdown):

1. HEADER Y BADGES
- Título principal del portafolio.
- Badges estéticos (sin versiones) de las tecnologías transversales detectadas (ej. Python, SQL, BigQuery, GCP, ETL, APIs).

2. PERFIL PROFESIONAL Y ENFOQUE
- Redacta 2-3 párrafos integrando tu formación en Ciencia Política/Políticas Públicas con la Ingeniería de Datos y Automatización.
- Destaca tu capacidad para conectar la gestión organizacional con el diseño de ecosistemas de datos, gobernanza e inteligencia operativa.

3. ARQUITECTURA TRANSVERSAL Y CAPACIDADES (La sección más detallada)
- Agrupa los patrones encontrados en los repositorios. Describe a nivel técnico cómo construyes soluciones:
  * Automatización de flujos y pipelines (ETL/ELT).
  * Consolidación y validación de datos.
  * Estandarización institucional y apoyo a la toma de decisiones.

4. ECOSISTEMA DE PROYECTOS (El Catálogo)
- Por cada repositorio en el consolidado, genera ÚNICAMENTE este formato conciso:
  ### [Nombre del Repo](Link_Detectado)
  - **Propósito:** 1 o 2 líneas explicando el problema que resuelve y su valor organizacional.
  - **Stack:** Tecnologías clave (separadas por comas).
  - **Impacto:** 1 viñeta directa sobre el resultado (ej. automatización de X horas, unificación de Y fuentes).

5. RESTRICCIONES ESTRICTAS
- NO TANTOS EMOJIS. MUY MUY POCOS.
- Tono puramente técnico, directo y analítico (evita el estilo adulador o de marketing de LinkedIn).
- Omite cualquier dato sensible (tokens, IPs, credenciales).
- No inventes habilidades o tecnologías que no estén demostradas en los READMEs.
"""

prompt = f"""
Sintetiza el siguiente consolidado de repositorios para generar el README.md del Portafolio Maestro. 
Aplica estrictamente las reglas de concisión: extrae todo el peso técnico hacia las secciones de perfil/capacidades, y mantén la lista de proyectos breve, impactante y con sus enlaces.

Consolidado de repositorios:
{Consolidado_Readmes}
"""

configuraciones_respaldo = [
    {"api": Gemini_API_2, "modelo": Modelo_1, "nombre": "Personal_1"},
    {"api": Gemini_API_2, "modelo": Modelo_2, "nombre": "Personal_2"},
    {"api": Gemini_API,   "modelo": Modelo_1, "nombre": "Empresarial_1"},
    {"api": Gemini_API,   "modelo": Modelo_2, "nombre": "Empresarial_2"},
    {"api": Gemini_API,   "modelo": Modelo_3, "nombre": "Empresarial_3"}
]

portfolio_final = None

for config in configuraciones_respaldo:
    try:
        resultado = consolidado_GENAI(config["api"], config["modelo"], instrucciones, prompt)
        if resultado:
            portfolio_final = resultado
            print(f"Funcionó con el intento asociado al agente {config["nombre"]}")
            with open("Portafolio_README.md", "w", encoding="utf-8") as Portafolio:
                Portafolio.write(portfolio_final)
            break
    except Exception as error:
        print(f"Fallo en el agente {config['nombre']}")
        if '503' in str(error):
            print(f"Ejecución detenida en {config['nombre']} por saturación de peticiones u otro error no iterable")
            continue
else:
    print("Se agotaron todas las instancias y no se pudo crear el portafolio")
