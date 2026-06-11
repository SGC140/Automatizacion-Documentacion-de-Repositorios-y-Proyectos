============================================================
Repositorio Asociado: Auditor-a-Clases
============================================================
# 🚀 Sistema de Auditoría Automatizada de Contenido Educativo

Este repositorio alberga un sistema integral para la auditoría automatizada de contenido de video educativo, diseñado para optimizar los procesos de control de calidad en entornos de aprendizaje digital. Utilizando la inteligencia artificial de Google Gemini, integración con Google Drive y herramientas avanzadas de procesamiento de video, el sistema descarga, optimiza, analiza y genera informes detallados en formato PDF a partir de grabaciones de clases.

El objetivo principal es proporcionar una solución escalable y objetiva para evaluar la calidad pedagógica y técnica de las clases, permitiendo a las instituciones educativas identificar rápidamente áreas de mejora y estandarizar la excelencia académica.

## 🛡️ Badges

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![Google Drive](https://img.shields.io/badge/Google%20Drive-Integration-green?style=flat-square&logo=google-drive&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI%20Powered-orange?style=flat-square&logo=google-gemini&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Video%20Processing-lightgrey?style=flat-square&logo=ffmpeg&logoColor=white)
![MoviePy](https://img.shields.io/badge/MoviePy-Video%20Editing-purple?style=flat-square&logo=moviepy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white)
![PyDrive2](https://img.shields.io/badge/PyDrive2-Google%20Drive%20API-yellowgreen?style=flat-square&logo=google-drive&logoColor=white)
![XHTML2PDF](https://img.shields.io/badge/XHTML2PDF-PDF%20Generation-red?style=flat-square&logo=pdf&logoColor=white)
![Project Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

## 📝 Índice

*   [Introducción](#-introducción)
*   [Arquitectura del Sistema](#-arquitectura-del-sistema)
*   [Características Principales](#-características-principales)
*   [Requisitos del Sistema](#-requisitos-del-sistema)
    *   [Dependencias de Sistema Operativo](#dependencias-de-sistema-operativo)
    *   [Dependencias de Python](#dependencias-de-python)
*   [Configuración del Proyecto](#-configuración-del-proyecto)
    *   [Configuración de Credenciales de Google Drive](#configuración-de-credenciales-de-google-drive)
    *   [Configuración de la API de Google Gemini](#configuración-de-la-api-de-google-gemini)
    *   [Variables de Entorno](#variables-de-entorno)
*   [Uso del Proyecto](#-uso-del-proyecto)
    *   [Flujo de Ejecución](#flujo-de-ejecución)
    *   [Ejecución del Script Principal (`main.py`)](#ejecución-del-script-principal-mainpy)
    *   [Generación de Informes HTML y PDF (`Create_html_to_PDF.py`)](#generación-de-informes-html-y-pdf-create_html_to_pdfpy)
*   [Estructura de Datos de Salida](#-estructura-de-datos-de-salida)
    *   [Ejemplo de Salida JSON](#ejemplo-de-salida-json)
    *   [Ejemplo de Salida CSV](#ejemplo-de-salida-csv)
*   [Análisis Técnico y Valor Agregado](#-análisis-técnico-y-valor-agregado)
    *   [Integración con Google Drive](#integración-con-google-drive)
    *   [Optimización de Video con FFmpeg y MoviePy](#optimización-de-video-con-ffmpeg-y-moviepy)
    *   [Auditoría de Contenido con Google Gemini](#auditoría-de-contenido-con-google-gemini)
    *   [Generación de Informes Profesionales](#generación-de-informes-profesionales)
*   [Impacto en el Negocio](#-impacto-en-el-negocio)
    *   [Preguntas de Negocio Abordadas](#preguntas-de-negocio-abordadas)
    *   [Valor Agregado](#valor-agregado)
    *   [Permite Medir](#permite-medir)
    *   [Permite Diagnosticar](#permite-diagnosticar)
    *   [Permite Resolver y Acotar](#permite-resolver-y-acotar)
    *   [Permite Optimizar](#permite-optimizar)
    *   [Permite Estandarizar](#permite-estandarizar)
    *   [Permite Repensar](#permite-repensar)
*   [Licencia](#-licencia)

---

## 💡 Introducción

Este proyecto automatiza el proceso de auditoría de videos de clases, transformando la supervisión manual en un flujo de trabajo eficiente y basado en IA. Desde la descarga de videos desde Google Drive hasta la generación de informes PDF estandarizados, el sistema garantiza una evaluación consistente y detallada de la calidad educativa. Es una herramienta esencial para instituciones que buscan escalar sus operaciones de control de calidad sin comprometer la profundidad del análisis.

## 🏗️ Arquitectura del Sistema

El sistema opera a través de un pipeline secuencial y modular, diseñado para procesar videos de clases y generar informes de auditoría completos.

**Pipeline General:**

1.  **Ingesta de Videos:** Los videos de clases son obtenidos desde una carpeta específica en Google Drive.
2.  **Descarga y Verificación:** Los videos se descargan localmente, con mecanismos de reintento y verificación de integridad.
3.  **Optimización de Video:** Los videos descargados se comprimen y aceleran para reducir el tamaño y el tiempo de procesamiento por la IA.
4.  **Auditoría con IA (Google Gemini):** El video optimizado (o sus segmentos) se envía a Google Gemini para un análisis profundo de su contenido pedagógico y técnico, generando un informe estructurado en formato JSON.
5.  **Persistencia de Datos:** El informe JSON se guarda localmente como archivo `.txt` y se convierte a `.csv` para facilitar el análisis de datos.
6.  **Estilización con IA (Google Gemini):** El informe JSON (`.txt`) se envía nuevamente a Google Gemini para ser transformado en un documento HTML profesional y estéticamente diseñado.
7.  **Generación de PDF:** El HTML generado se convierte a un archivo PDF final, listo para su distribución.

**Componentes Clave:**

*   **Módulo de Integración con Google Drive (`main.py`):** Gestiona la autenticación, listado y descarga de archivos de video.
*   **Módulo de Procesamiento de Video (`main.py`):** Emplea `MoviePy` y `FFmpeg` para la compresión, redimensionamiento, aceleración y, si es necesario, segmentación de videos.
*   **Módulo de Auditoría con IA (`main.py`):** Interactúa con la API de Google Gemini (`gemini-2.5-flash`) para analizar el contenido del video, utilizando prompts estructurados y manejo de contexto para videos largos.
*   **Módulo de Generación de Datos Estructurados (`main.py`):** Procesa la respuesta JSON de Gemini y la guarda en formatos `.txt` y `.csv`.
*   **Módulo de Generación de Informes Profesionales (`Create_html_to_PDF.py`):** Utiliza Google Gemini para estilizar el informe de texto en HTML y `xhtml2pdf` para la conversión final a PDF.

## ✨ Características Principales

*   **Automatización Completa:** Desde la descarga de videos hasta la generación de informes PDF, el proceso es totalmente automatizado.
*   **Integración Robusta con Google Drive:** Descarga segura y verificada de videos desde carpetas específicas.
*   **Optimización Inteligente de Video:** Compresión y aceleración de videos para reducir costos y tiempos de procesamiento de la IA, con un robusto sistema de fallback entre `MoviePy` y `FFmpeg`.
*   **Auditoría de Contenido Basada en IA:** Utiliza Google Gemini para un análisis profundo de la claridad del profesor, dominio del tema, uso de herramientas, participación y manejo del tiempo.
*   **Manejo de Videos Extensos:** Capacidad para segmentar videos largos y procesarlos iterativamente con la IA, manteniendo la coherencia del informe final mediante un mecanismo de contexto acumulado.
*   **Informes Estructurados y Accionables:** Genera informes en formato JSON y CSV, facilitando el análisis programático y la integración con otros sistemas.
*   **Generación de Informes Profesionales en PDF:** Transforma los datos de auditoría en documentos HTML estéticamente agradables y luego en PDFs listos para su presentación, con un diseño coherente y profesional.
*   **Manejo de Errores y Reintentos:** Incluye lógica para reintentar descargas fallidas y manejar límites de cuota de la API de Gemini.

## ⚙️ Requisitos del Sistema

### Dependencias de Sistema Operativo

*   **FFmpeg:** Es una herramienta fundamental para la manipulación de video. Se utiliza para la compresión, aceleración y segmentación de videos.
    *   **Instalación (Linux/macOS):**
        ```bash
        sudo apt update && sudo apt install ffmpeg # Debian/Ubuntu
        brew install ffmpeg # macOS (Homebrew)
        ```
    *   **Instalación (Windows):** Descargue el ejecutable desde el [sitio oficial de FFmpeg](https://ffmpeg.org/download.html) y asegúrese de que la ruta al ejecutable `ffmpeg.exe` esté incluida en la variable de entorno PATH de su sistema.

### Dependencias de Python

Se recomienda el uso de un entorno virtual para gestionar las dependencias.

```bash
pip install pandas gspread oauth2client pydrive2 python-dotenv moviepy imageio-ffmpeg google-generativeai xhtml2pdf
```

## 🛠️ Configuración del Proyecto

### Configuración de Credenciales de Google Drive

Este proyecto utiliza `pydrive2` para interactuar con Google Drive. Necesitará un archivo de credenciales para autenticarse.

1.  **Crear un Proyecto en Google Cloud Console:**
    *   Vaya a [Google Cloud Console](https://console.cloud.google.com/).
    *   Cree un nuevo proyecto o seleccione uno existente.
2.  **Habilitar la API de Google Drive:**
    *   En el menú de navegación, vaya a "APIs y servicios" > "Biblioteca".
    *   Busque "Google Drive API" y habilítela.
3.  **Crear Credenciales de OAuth 2.0 (ID de Cliente de Escritorio):**
    *   Vaya a "APIs y servicios" > "Credenciales".
    *   Haga clic en "Crear credenciales" > "ID de cliente de OAuth".
    *   Seleccione "Aplicación de escritorio" como tipo de aplicación.
    *   Asigne un nombre y haga clic en "Crear".
    *   Descargue el archivo JSON resultante.
4.  **Renombrar y Colocar el Archivo:**
    *   Renombre el archivo JSON descargado a `credentials_module.json`.
    *   Colóquelo en la raíz de su proyecto.

La primera vez que ejecute el script `main.py`, se abrirá una ventana del navegador para que autorice el acceso a su cuenta de Google Drive. Una vez autorizado, `pydrive2` guardará un token de acceso en `credentials_module.json` para futuras autenticaciones.

### Configuración de la API de Google Gemini

El proyecto requiere una clave de API para Google Gemini.

1.  **Obtener una Clave de API:**
    *   Visite [Google AI Studio](https://aistudio.google.com/app/apikey) o la consola de Google Cloud para generar una clave de API para Gemini.
2.  **Configurar la Variable de Entorno:**
    *   Cree un archivo `.env` en la raíz de su proyecto.
    *   Agregue su clave de API de Gemini de la siguiente manera:
        ```dotenv
        API_KEY_GEMINI_PRO_1.5="TU_CLAVE_API_DE_GEMINI"
        ```
    *   **Nota:** El nombre de la variable `API_KEY_GEMINI_PRO_1.5` es el que se espera en el código.

### Variables de Entorno

Además de la clave de API de Gemini, necesita especificar la carpeta de Google Drive de donde se descargarán los videos.

*   En el archivo `.env`, agregue la siguiente variable:
    ```dotenv
    carpeta_drive="ID_DE_LA_CARPETA_DE_GOOGLE_DRIVE"
    ```
    *   Para obtener el ID de una carpeta de Google Drive, abra la carpeta en su navegador. El ID es la parte de la URL después de `/folders/` (ej. `https://drive.google.com/drive/folders/ESTE_ES_EL_ID`).

## 🚀 Uso del Proyecto

### Flujo de Ejecución

El sistema está diseñado para ejecutarse en dos fases principales:

1.  **Fase de Auditoría y Generación de Datos (`main.py`):** Descarga videos, los procesa con IA y genera informes JSON/CSV.
2.  **Fase de Generación de Informes PDF (`Create_html_to_PDF.py`):** Toma los informes JSON generados y los convierte en documentos HTML estilizados y luego en PDFs.

### Ejecución del Script Principal (`main.py`)

Este script es el encargado de la auditoría de los videos.

1.  Asegúrese de que todas las [dependencias](#dependencias-de-python) estén instaladas y las [variables de entorno](#variables-de-entorno) configuradas.
2.  Ejecute el script desde la terminal:
    ```bash
    python main.py
    ```
3.  El script:
    *   Se autenticará con Google Drive.
    *   Listará y descargará los videos de la carpeta especificada.
    *   Optimizará cada video.
    *   Subirá el video (o sus partes) a Google Gemini para su auditoría.
    *   Generará un archivo `Reporte_Auditoria_NOMBRE_VIDEO.txt` (JSON) y `Reporte_Auditoria_NOMBRE_VIDEO.csv` por cada video auditado.
    *   Eliminará los archivos temporales de video.

### Generación de Informes HTML y PDF (`Create_html_to_PDF.py`)

Una vez que `main.py` ha generado los archivos `.txt` con los informes JSON, este script los transformará en informes PDF profesionales.

1.  Asegúrese de que la [API de Google Gemini](#configuración-de-la-api-de-google-gemini) esté configurada en su archivo `.env`.
2.  Ejecute el script desde la terminal:
    ```bash
    python Create_html_to_PDF.py
    ```
3.  El script:
    *   Buscará todos los archivos `Reporte_Auditoria_*.txt` en el directorio actual.
    *   Para cada archivo, lo subirá a Google Gemini.
    *   Solicitará a Gemini que convierta el contenido del informe en un código HTML estilizado, siguiendo las directrices de diseño predefinidas.
    *   Guardará el HTML generado como `Reporte_Auditoria_NOMBRE_VIDEO.html`.
    *   Convertirá el archivo HTML a `Reporte_Auditoria_NOMBRE_VIDEO.pdf` utilizando `xhtml2pdf`.
    *   Eliminará los archivos temporales de Gemini.

## 📊 Estructura de Datos de Salida

El proceso de auditoría genera datos estructurados en formato JSON, que luego se pueden exportar a CSV para un análisis tabular.

### Ejemplo de Salida JSON

El archivo `Reporte_Auditoria_NOMBRE_VIDEO.txt` contendrá un objeto JSON con la siguiente estructura:

```json
{
  "resumen_clase": "Descripción concisa de los temas cubiertos en la clase, incluyendo los puntos principales y el enfoque pedagógico.",
  "objetivo_alcanzado": "Sí - El objetivo de la lección fue claramente alcanzado, con una demostración efectiva de los conceptos clave.",
  "puntos_fuertes": [
    "Claridad excepcional en la explicación de conceptos complejos.",
    "Uso efectivo de ejemplos prácticos y analogías para facilitar la comprensión.",
    "Fomento activo de la participación estudiantil mediante preguntas abiertas.",
    "Excelente manejo de las herramientas digitales para la presentación de contenido."
  ],
  "oportunidades_mejora": [
    "Algunas transiciones entre temas fueron abruptas, afectando ligeramente el flujo.",
    "Podría integrar más actividades interactivas para reforzar el aprendizaje práctico.",
    "El ritmo en la sección final fue un poco acelerado, dejando menos tiempo para preguntas."
  ],
  "recomendaciones_accionables": [
    "Planificar transiciones más suaves entre los módulos temáticos.",
    "Incorporar un breve ejercicio práctico o un quiz al final de cada sección principal."
  ],
  "nivel_participacion": "Alta - Los alumnos interactuaron activamente, haciendo preguntas pertinentes y respondiendo a los planteamientos del profesor.",
  "manejo_del_tiempo": "Adecuado - El tiempo se distribuyó de manera equilibrada entre la exposición teórica, ejemplos y un espacio para preguntas, aunque el final fue un poco ajustado.",
  "herramientas_utilizadas": [
    "Presentación de diapositivas (Google Slides)",
    "Pizarrón virtual (Jamboard)",
    "Encuestas rápidas (Mentimeter)"
  ],
  "incidencias_notables": [
    "Breve interrupción de audio al inicio debido a un micrófono mal configurado (resuelto rápidamente)."
  ],
  "calificacion_pedagogica": 92,
  "calificacion_tecnica": 88,
  "comentario_final": "La clase demostró un alto nivel de preparación y ejecución pedagógica. Se recomienda un enfoque en la fluidez de las transiciones y la integración de más elementos interactivos para maximizar la retención del aprendizaje."
}
```

### Ejemplo de Salida CSV

El archivo `Reporte_Auditoria_NOMBRE_VIDEO.csv` presentará los datos del JSON en un formato tabular, con las listas concatenadas por saltos de línea para mantener la información en una sola celda.

```csv
resumen_clase,objetivo_alcanzado,puntos_fuertes,oportunidades_mejora,recomendaciones_accionables,nivel_participacion,manejo_del_tiempo,herramientas_utilizadas,incidencias_notables,calificacion_pedagogica,calificacion_tecnica,comentario_final
"Descripción concisa de los temas cubiertos en la clase, incluyendo los puntos principales y el enfoque pedagógico.","Sí - El objetivo de la lección fue claramente alcanzado, con una demostración efectiva de los conceptos clave.","Claridad excepcional en la explicación de conceptos complejos.\nUso efectivo de ejemplos prácticos y analogías para facilitar la comprensión.\nFomento activo de la participación estudiantil mediante preguntas abiertas.\nExcelente manejo de las herramientas digitales para la presentación de contenido.","Algunas transiciones entre temas fueron abruptas, afectando ligeramente el flujo.\nPodría integrar más actividades interactivas para reforzar el aprendizaje práctico.\nEl ritmo en la sección final fue un poco acelerado, dejando menos tiempo para preguntas.","Planificar transiciones más suaves entre los módulos temáticos.\nIncorporar un breve ejercicio práctico o un quiz al final de cada sección principal.","Alta - Los alumnos interactuaron activamente, haciendo preguntas pertinentes y respondiendo a los planteamientos del profesor.","Adecuado - El tiempo se distribuyó de manera equilibrada entre la exposición teórica, ejemplos y un espacio para preguntas, aunque el final fue un poco ajustado.","Presentación de diapositivas (Google Slides)\nPizarrón virtual (Jamboard)\nEncuestas rápidas (Mentimeter)","Breve interrupción de audio al inicio debido a un micrófono mal configurado (resuelto rápidamente).",92,88,"La clase demostró un alto nivel de preparación y ejecución pedagógica. Se recomienda un enfoque en la fluidez de las transiciones y la integración de más elementos interactivos para maximizar la retención del aprendizaje."
```

## 🔬 Análisis Técnico y Valor Agregado

Este proyecto integra diversas tecnologías para construir un pipeline de auditoría robusto y eficiente. La selección de cada herramienta se basa en su capacidad para aportar valor técnico y resolver desafíos específicos.

### Integración con Google Drive

*   **Tecnología:** `pydrive2`
*   **Valor Agregado:** `pydrive2` proporciona una interfaz Pythonic para la API de Google Drive, simplificando la autenticación (OAuth 2.0), la navegación de archivos y la descarga. La implementación incluye lógica de reintento y verificación del tamaño del archivo (`os.path.getsize` vs `archivo['fileSize']`) para asegurar descargas completas y fiables, mitigando problemas de red o de la API. Esto es crucial para garantizar que el material fuente para la auditoría sea íntegro.

### Optimización de Video con FFmpeg y MoviePy

La optimización de video es un paso crítico para reducir los costos y el tiempo de procesamiento de la IA, ya que los modelos de lenguaje multimodal consumen recursos en función de la duración y calidad del video.

*   **Tecnología:** `MoviePy` (con `imageio-ffmpeg` como backend) y `FFmpeg` (directamente vía `subprocess`).
*   **Valor Agregado:**
    *   **Reducción de Costos y Tiempo:** Al reducir la resolución (`height=240` o `scale=-2:360`), acelerar la reproducción (`MultiplySpeed, 1.5` o `setpts=0.666667*PTS, atempo=1.5`), y disminuir el `fps` (`0.5`), se minimiza la cantidad de datos que la IA debe procesar, optimizando el consumo de tokens y el tiempo de respuesta.
    *   **MoviePy:** Ofrece una abstracción de alto nivel para la edición de video, facilitando operaciones como redimensionamiento y cambio de velocidad con una sintaxis intuitiva. Es útil para prototipado rápido.
    *   **FFmpeg (Directo):** La implementación de `subprocess.run` con `FFmpeg` es un mecanismo de *fallback* robusto. `FFmpeg` es el estándar de la industria para el procesamiento de medios, conocido por su eficiencia y control granular. Cuando `MoviePy` (que a veces puede ser menos estable o más lento para ciertas operaciones) falla, la llamada directa a `FFmpeg` garantiza que la optimización se complete de manera fiable. Los parámetros como `-filter_complex`, `-preset ultrafast`, `-b:a 32k`, y `-ac 1` están ajustados para una compresión máxima con una calidad suficiente para el análisis de contenido (no para visualización de alta fidelidad).
    *   **Segmentación de Videos Largos:** Para videos que exceden los límites de tokens de Gemini, `FFmpeg` se utiliza para segmentar el video en partes más pequeñas (`-segment_time 1500` para 25 minutos por segmento). Esto permite procesar videos de cualquier duración, superando las limitaciones de la API.

### Auditoría de Contenido con Google Gemini

El corazón del sistema reside en la capacidad de la IA para analizar el contenido pedagógico y técnico de las clases.

*   **Tecnología:** `google.generativeai` con el modelo `gemini-2.5-flash`.
*   **Valor Agregado:**
    *   **Análisis Multimodal Avanzado:** `gemini-2.5-flash` es un modelo multimodal optimizado para velocidad y eficiencia, ideal para procesar videos y extraer información relevante sobre la dinámica de la clase.
    *   **Prompts Estructurados y `system_instruction`:** La definición de un `system_instruction` (`Eres un Auditor de Calidad Educativa...`) y un `prompt_final` detallado que exige una salida JSON específica, asegura que la IA se adhiera a un rol y formato predefinidos. Esto es crucial para la consistencia y la parseabilidad de los informes.
    *   **Manejo de Contexto para Videos Segmentados (RAG-like):** La función `generar_prompt_dinamico` implementa un mecanismo de "memoria" o contexto acumulado. Para videos segmentados, el informe JSON generado por un fragmento anterior se alimenta de nuevo a la IA como `contexto_anterior` para el siguiente fragmento. Esto permite a Gemini construir un informe unificado y coherente a lo largo de todo el video, superando las limitaciones de la ventana de contexto de la API para entradas muy largas.
    *   **Manejo de Rate Limits:** La lógica de reintento con `time.sleep(30)` para errores `429` (Quota Exceeded) garantiza la robustez del proceso frente a las limitaciones de la API, evitando fallos en la auditoría de videos extensos o en lotes.
    *   **Métricas Cuantitativas y Cualitativas:** La estructura JSON solicita calificaciones numéricas (`calificacion_pedagogica`, `calificacion_tecnica`) junto con descripciones cualitativas detalladas, proporcionando una visión holística.

### Generación de Informes Profesionales

La presentación de los resultados es tan importante como el análisis en sí.

*   **Tecnología:** `google.generativeai` (para HTML) y `xhtml2pdf` (para PDF).
*   **Valor Agregado:**
    *   **Estilización con IA:** Utilizar Gemini para convertir el JSON en HTML (`PROMPT` en `Create_html_to_PDF.py`) permite una generación dinámica de informes con un diseño profesional y estético, sin necesidad de plantillas HTML estáticas complejas. La estricta directriz de **no usar flexbox, CSS grid, ni variables :root** en el prompt asegura la compatibilidad con `xhtml2pdf` y evita complejidades de renderizado que podrían surgir con CSS moderno.
    *   **Consistencia de Marca:** La `Plantilla_HTML` (CSS) incrustada en el prompt guía a Gemini para usar colores y fuentes específicos (`Tahoma`, paleta naranja), asegurando que los informes finales se alineen con la identidad visual de la compañía.
    *   **Generación de PDF Robusta:** `xhtml2pdf` (`pisa.CreatePDF`) es una biblioteca Python fiable para convertir HTML y CSS a PDF. A diferencia de `pdfkit` (que a menudo requiere `wkhtmltopdf` como dependencia externa de SO), `xhtml2pdf` es una solución más autocontenida en Python, lo que simplifica la implementación y el despliegue. Produce documentos PDF de alta calidad, listos para su distribución o archivo.

## 📈 Impacto en el Negocio

Este sistema de auditoría automatizada de contenido educativo no es solo una herramienta técnica, sino una palanca estratégica para la mejora continua y la eficiencia operativa en instituciones educativas.

### Preguntas de Negocio Abordadas

*   ¿Cómo podemos asegurar una calidad de enseñanza consistente en todas nuestras clases grabadas?
*   ¿Qué puntos específicos necesitan mejorar nuestros instructores para optimizar la experiencia de aprendizaje?
*   ¿Es posible escalar nuestro proceso de control de calidad sin incurrir en costos prohibitivos de personal?
*   ¿Estamos aprovechando al máximo las herramientas digitales en nuestras clases?
*   ¿Cómo podemos obtener retroalimentación objetiva y estandarizada sobre el desempeño docente?

### Valor Agregado

El sistema proporciona un valor agregado significativo al transformar un proceso manual, subjetivo y lento en uno automatizado, objetivo y escalable. Libera a los auditores humanos para que se concentren en tareas de mayor valor estratégico, como el desarrollo de programas de capacitación o la mentoría individualizada, en lugar de la revisión rutinaria de videos. La consistencia en la evaluación y la rapidez en la entrega de informes permiten una toma de decisiones ágil y basada en datos.

### Permite Medir

*   **Calidad Pedagógica y Técnica:** Cuantifica el desempeño del instructor con calificaciones numéricas (0-100), complementadas con descripciones cualitativas.
*   **Nivel de Participación:** Evalúa la interacción de los alumnos (Alta/Media/Baja) y describe su dinámica.
*   **Manejo del Tiempo:** Mide la eficiencia en la distribución del tiempo de la clase.
*   **Uso de Herramientas:** Registra las herramientas digitales utilizadas, permitiendo un seguimiento de la adopción tecnológica.
*   **Incidencias:** Identifica y registra problemas técnicos o interrupciones, cuantificando su frecuencia y tipo.
*   **Puntos Fuertes y Oportunidades:** Proporciona listas estructuradas de aciertos y áreas de mejora, facilitando el análisis de tendencias.

### Permite Diagnosticar

*   **Debilidades Específicas del Instructor:** Identifica patrones de fallos (ej. "muletillas", explicaciones confusas, falta de interacción) que requieren atención.
*   **Ineficiencias Metodológicas:** Diagnostica si ciertas metodologías no están siendo efectivas o si el ritmo de la clase es inadecuado.
*   **Problemas Técnicos Recurrentes:** Señala incidencias como fallas de conexión o problemas de audio, que pueden indicar necesidades de infraestructura o capacitación técnica.
*   **Brechas en la Adopción Tecnológica:** Revela si las herramientas digitales no se están utilizando o si su uso es subóptimo.
*   **Necesidades de Capacitación:** Agrega datos para identificar áreas comunes de mejora en el cuerpo docente, informando el diseño de programas de desarrollo profesional.

### Permite Resolver y Acotar

*   **Recomendaciones Accionables:** Proporciona sugerencias concretas y directas para que los profesores mejoren en su próxima clase.
*   **Foco en la Mejora:** Permite a los directores académicos acotar las áreas de mejora para cada instructor, haciendo la retroalimentación más efectiva y menos abrumadora.
*   **Intervención Temprana:** Al identificar rápidamente problemas, se pueden implementar soluciones antes de que afecten a un gran número de estudiantes.
*   **Optimización de Recursos:** Dirige los recursos de capacitación y soporte técnico hacia donde son más necesarios.

### Permite Optimizar

*   **Proceso de QA:** Reduce drásticamente el tiempo y el costo asociados con la auditoría manual de videos.
*   **Desarrollo Docente:** Optimiza la efectividad de los programas de capacitación al basarlos en datos reales y necesidades identificadas.
*   **Experiencia del Estudiante:** Mejora indirectamente la calidad de la enseñanza, lo que se traduce en una mejor experiencia de aprendizaje y mayores tasas de retención.
*   **Uso de Ancho de Banda y Almacenamiento:** La compresión de videos para la IA optimiza el uso de recursos de red y almacenamiento en la nube.
*   **Escalabilidad:** Permite auditar un volumen masivo de clases sin un aumento lineal en el personal de QA.

### Permite Estandarizar

*   **Criterios de Evaluación:** Establece un conjunto uniforme y objetivo de criterios de evaluación aplicados por la IA, eliminando la subjetividad humana.
*   **Formato de Informes:** Genera informes estandarizados en JSON, CSV y PDF, facilitando la comparación, el archivo y la integración con sistemas de gestión académica.
*   **Nivel de Calidad:** Define un umbral de calidad consistente para todas las clases, asegurando que se cumplan los estándares institucionales.
*   **Procesos Internos:** Estandariza el flujo de trabajo de control de calidad, desde la ingesta de videos hasta la entrega de informes.

### Permite Repensar

*   **Estrategias Pedagógicas Institucionales:** Los datos agregados pueden revelar la necesidad de repensar y adaptar las metodologías de enseñanza a nivel institucional, promoviendo enfoques más efectivos y participativos.
*   **Diseño Curricular:** Si los informes muestran consistentemente dificultades en ciertos temas o la falta de uso de herramientas específicas, puede llevar a una revisión del diseño de los cursos.
*   **Programas de Formación Docente:** Permite rediseñar los programas de desarrollo profesional para abordar las competencias más críticas y las deficiencias comunes identificadas por la IA.
*   **Infraestructura Tecnológica:** La recurrencia de incidencias técnicas puede impulsar una reevaluación y mejora de la infraestructura de red, plataformas LMS o equipos de grabación.
*   **Modelo de Evaluación de Desempeño:** El sistema puede integrar nuevas métricas o ajustar las existentes, permitiendo una evolución continua del modelo de evaluación docente.
*   **Innovación en el Aula:** Al liberar tiempo de los equipos de QA y proporcionar insights claros, se fomenta la experimentación con nuevas herramientas y enfoques pedagógicos, sabiendo que su impacto será medido y reportado.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo `LICENSE` para obtener más detalles.============================================================
Repositorio Asociado: Automatizacion-Documentacion-de-Repositorios-y-Proyectos
============================================================
# Automatización de Documentación de Repositorios con LLMs

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub%20API-Integration-informational?style=flat-square&logo=github&logoColor=white)
![Groq API](https://img.shields.io/badge/Groq%20API-Llama-green?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyQzIgMTcuNTIgNi40OCAyMiAxMiAyMkMxNy41MiAyMiAyMiAxNy41MiAyMiAxMkMyMiA2LjQ4IDE3LjUyIDIgMTIgMlpNMTIgNEwxNiA4SDhMMTIgNFpNMTggMTJMMTQuNSAxNS41TDE4IDE5VjEyWk02IDEyVjE5TDEwLjUgMTUuNUw2IDEyWk0xMiAxNkw4IDE5SDE2TDEyIDE2WiIgZmlsbD0id2hpdGUiLz4KPC9zdmc+&logoColor=white)
![Google Gemini API](https://img.shields.io/badge/Google%20Gemini%20API-AI%20Platform-orange?style=flat-square&logo=google&logoColor=white)
![Project Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-Unspecified-lightgrey?style=flat-square)

Este repositorio alberga un sistema automatizado diseñado para generar y actualizar documentación `README.md` para proyectos de GitHub utilizando modelos de lenguaje grandes (LLMs). La solución aborda la necesidad crítica de mantener una documentación consistente y actualizada en entornos de desarrollo ágiles y con múltiples repositorios.

---

## Tabla de Contenidos

*   [1. Visión General del Proyecto](#1-visión-general-del-proyecto)
*   [2. Arquitectura del Sistema](#2-arquitectura-del-sistema)
*   [3. Estructura del Código](#3-estructura-del-código)
*   [4. Configuración del Entorno](#4-configuración-del-entorno)
    *   [4.1. Dependencias a Nivel de Sistema Operativo](#41-dependencias-a-nivel-de-sistema-operativo)
    *   [4.2. Dependencias de Python](#42-dependencias-de-python)
    *   [4.3. Variables de Entorno](#43-variables-de-entorno)
*   [5. Lógica Principal y Pipeline](#5-lógica-principal-y-pipeline)
    *   [5.1. Flujo de Ejecución](#51-flujo-de-ejecución)
    *   [5.2. Payload y Prompts](#52-payload-y-prompts)
*   [6. Valor Agregado y Justificación Técnica](#6-valor-agregado-y-justificación-técnica)
    *   [6.1. Respuesta a Necesidades de Negocio](#61-respuesta-a-necesidades-de-negocio)
    *   [6.2. Justificación de Tecnologías](#62-justificación-de-tecnologías)
*   [7. Ejemplos de Salida](#7-ejemplos-de-salida)
    *   [7.1. Archivo `Consolidado_Documentación.txt`](#71-archivo-consolidadodocumentacióntxt)
    *   [7.2. Contenido del `README.md` Generado](#72-contenido-del-readmemd-generado)
*   [8. Contribución](#8-contribución)
*   [9. Licencia](#9-licencia)

---

## 1. Visión General del Proyecto

Este proyecto implementa un sistema de automatización para la generación y actualización de archivos `README.md` en repositorios de GitHub. Utiliza la capacidad de los Modelos de Lenguaje Grandes (LLMs) para analizar el contenido del código fuente de un repositorio y sintetizar una documentación estructurada y relevante. La solución está diseñada para operar de manera autónoma, iterando sobre los repositorios de un usuario de GitHub, identificando aquellos que requieren documentación o actualización, y aplicando un proceso de generación y traducción de READMEs.

El objetivo principal es estandarizar la documentación, reducir la carga manual de los desarrolladores y asegurar que la información esencial de cada proyecto esté siempre disponible y actualizada, tanto en español como en inglés.

## 2. Arquitectura del Sistema

La arquitectura del sistema es de tipo cliente-servidor, donde el script Python actúa como cliente, interactuando con las APIs de GitHub y las APIs de los LLMs (Groq y Google Gemini) como servicios externos.

```
+---------------------+       +---------------------+
|                     |       |                     |
|  Script Python      |       |  GitHub API         |
|  (`main.py` /       |------>|  (PyGithub)         |
|   `Groq_Deepsek_backup.py`)|       |                     |
|                     |       +---------------------+
|  - Carga .env       |                 |
|  - Autenticación    |                 |
|  - Lee `Consolidado_Documentación.txt` |                 |
|  - Itera Repositorios |                 |
|  - Extrae Código    |                 |
|                     |       +---------------------+
|                     |------>|  Groq API           |
|                     |       |  (openai client)    |
|                     |       +---------------------+
|                     |                 |
|                     |       +---------------------+
|                     |------>|  Google Gemini API  |
|                     |       |  (google.genai)     |
|                     |       +---------------------+
|                     |                 |
|  - Genera READMEs   |<----------------+
|  - Traduce READMEs  |<----------------+
|  - Actualiza Repositorios |
|  - Actualiza `Consolidado_Documentación.txt` |
+---------------------+
```

**Componentes Clave:**

*   **Script Principal (`main.py` o `Groq_Deepsek_backup.py`):** Orquesta todo el proceso. Se encarga de la autenticación, la interacción con GitHub, la preparación del `prompt` para los LLMs, la invocación de las APIs de los LLMs, el manejo de respuestas y la actualización de los repositorios.
*   **GitHub API (a través de `PyGithub`):** Permite al script autenticarse, listar repositorios, acceder a su contenido (archivos y directorios), y crear o actualizar archivos (`README.md`, `README_English.md`).
*   **Groq API (a través del cliente `openai`):** Proporciona acceso a modelos de lenguaje de alto rendimiento (ej., Llama-3) para la generación de texto. Utilizado para la creación inicial del `README.md` en español y su posterior traducción.
*   **Google Gemini API (a través de `google-generativeai`):** Ofrece una alternativa o complemento a Groq para la generación de texto, utilizando modelos como `gemini-2.5-flash`. También se utiliza para la creación y traducción de READMEs.
*   **Archivo `Consolidado_Documentación.txt`:** Actúa como un registro persistente de los repositorios que ya han sido procesados, evitando re-procesamientos innecesarios y optimizando el uso de recursos de la API.

## 3. Estructura del Código

El proyecto consta de dos archivos Python principales que implementan la misma lógica pero utilizan diferentes proveedores de LLM, lo que permite flexibilidad o pruebas A/B entre ellos.

*   **`Groq_Deepsek_backup.py`**:
    *   Utiliza la API de Groq para interactuar con modelos como `llama-3.3-70b-versatile`.
    *   Implementa la función `consultar_ia` para interactuar con la API de Groq.
    *   El resto de la lógica (iteración de repositorios, extracción de código, generación de prompts, manejo de errores, traducción y actualización de GitHub) es idéntica a `main.py`.

*   **`main.py`**:
    *   Utiliza la API de Google Gemini para interactuar con modelos como `gemini-2.5-flash`.
    *   La interacción con Gemini se realiza directamente a través del cliente `AI_User.models.generate_content`.
    *   El resto de la lógica (iteración de repositorios, extracción de código, generación de prompts, manejo de errores, traducción y actualización de GitHub) es idéntica a `Groq_Deepsek_backup.py`.

Ambos scripts comparten la siguiente estructura lógica:

```python
# Carga de variables de entorno
import os
from dotenv import load_dotenv
load_dotenv(override=True)

# Autenticación con GitHub
from github import Github, Auth
Git_TOKEN = os.getenv("GIT_TOKEN")
auth = Auth.Token(Git_TOKEN)
Git = Github(auth=auth)
Git_User = Git.get_user()

# Autenticación con LLM API (Groq o Gemini)
# ... (diferente implementación según el archivo) ...

# Lectura de repositorios ya documentados
with open("Consolidado_Documentación.txt", "r") as Historico:
    Repos_documentados = Historico.read().split("\n")

# Iteración sobre los repositorios del usuario
Repos = Git_User.get_repos()
for repo in Repos:
    # Lógica para saltar repositorios ya documentados
    if repo.name in Repos_documentados:
        continue

    # Acumulación de contenido de archivos relevantes (.py, .sql, .ipynb, .json)
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
                print(f"Error al decodificar {archivo.name}: {error}")

    if not acumulated_script:
        continue

    # Definición de instrucciones y prompt para la generación del README
    instrucciones = """Eres un Senior Data Analyst & Automation Analyst. Crea un README.md profesional..."""
    prompt = f"""Genera el README.md final para este proyecto...:\n\n{acumulated_script}"""

    # Llamada a la API del LLM para generar el README (con reintentos)
    respuesta = None
    for intento in range(max_intentos):
        try:
            # ... (Llamada a Groq o Gemini) ...
            break
        except Exception as error_api:
            time.sleep(60)

    if not respuesta:
        continue

    readme_final = respuesta.text if hasattr(respuesta, 'text') else respuesta # Manejo de respuesta de Gemini vs Groq

    # Definición de instrucciones y prompt para la traducción del README
    instrucciones_traductor = f"Eres un Senior Data Analyst & Automation Analyst experto y adicional a ello eres un traductor experto..."
    prompt_traduccion = f"""Genera la traducción, al inglés, de esta documentación...: {readme_final}"""

    # Llamada a la API del LLM para traducir el README (con reintentos)
    english_readme = None
    for intento in range(max_intentos):
        try:
            # ... (Llamada a Groq o Gemini) ...
            break
        except Exception as error_api:
            time.sleep(60)

    if not english_readme:
        continue

    english_readme = english_readme.text if hasattr(english_readme, 'text') else english_readme

    # Actualización o creación de README.md y README_English.md en el repositorio
    commit_msg_es = f"Docs: Autogenerado y automatizado README con agentes contextualizados con códigos iterativos para {repo.name}"
    commit_msg_en = f"Docs: Auto-generated and automated README with contextualized agents with iterative codes for {repo.name}"

    try:
        # Actualizar/Crear README.md (español)
        # ...
    except Exception:
        # Crear README.md (español)
        # ...

    time.sleep(5)

    try:
        # Actualizar/Crear README_English.md (inglés)
        # ...
    except Exception:
        # Crear README_English.md (inglés)
        # ...

    # Registro del repositorio documentado
    with open("Consolidado_Documentación.txt", "a") as Documento:
        Documento.write("\n"+repo.name)

    time.sleep(5)

print("Documentación creada/actualizada y finalizada con éxito")
```

## 4. Configuración del Entorno

Para ejecutar este proyecto, es necesario configurar el entorno de desarrollo con las dependencias adecuadas y las variables de entorno requeridas.

### 4.1. Dependencias a Nivel de Sistema Operativo

Este proyecto no requiere dependencias específicas a nivel de sistema operativo (como FFmpeg, Tesseract, o controladores de hardware) más allá de un entorno Python funcional y acceso a internet para comunicarse con las APIs externas.

### 4.2. Dependencias de Python

Las librerías de Python necesarias se pueden instalar utilizando `pip`. Se recomienda el uso de un entorno virtual para gestionar las dependencias.

```bash
# Crear un entorno virtual (si aún no tienes uno)
python -m venv venv

# Activar el entorno virtual
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar las dependencias
pip install python-dotenv PyGithub openai google-generativeai
```

### 4.3. Variables de Entorno

El proyecto utiliza variables de entorno para gestionar credenciales sensibles, lo que es una práctica de seguridad recomendada. Debes crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```ini
GIT_TOKEN="tu_token_personal_de_acceso_de_github"
GROQ_KEY="tu_clave_api_de_groq"
API_GEMINI_KEY="tu_clave_api_de_google_gemini"
```

**Notas sobre los tokens:**

*   **`GIT_TOKEN`**: Un Personal Access Token (PAT) de GitHub con los permisos necesarios para leer repositorios (`repo` scope) y escribir archivos (`write:repo_hook`, `public_repo` o `repo` completo si es necesario para repositorios privados).
*   **`GROQ_KEY`**: La clave API obtenida de la plataforma Groq.
*   **`API_GEMINI_KEY`**: La clave API obtenida de Google AI Studio o Google Cloud para Gemini.

## 5. Lógica Principal y Pipeline

### 5.1. Flujo de Ejecución

El pipeline de ejecución sigue una secuencia definida para cada repositorio:

1.  **Inicialización:** Carga de variables de entorno y autenticación con GitHub y los proveedores de LLM.
2.  **Registro de Repositorios Documentados:** Lee el archivo `Consolidado_Documentación.txt` para obtener una lista de repositorios que ya han sido procesados.
3.  **Iteración de Repositorios:** Obtiene todos los repositorios del usuario autenticado en GitHub.
4.  **Filtrado:** Para cada repositorio, verifica si ya está en la lista de `Repos_documentados`. Si es así, lo salta.
5.  **Extracción de Código:** Si el repositorio no ha sido documentado, recorre recursivamente su contenido. Acumula el texto de todos los archivos con extensiones `.py`, `.sql`, `.ipynb` y `.json`.
6.  **Generación de README (Español):**
    *   Construye un `prompt` detallado que incluye las instrucciones específicas para la generación del README y el código fuente acumulado del repositorio.
    *   Envía este `prompt` a la API del LLM (Groq o Gemini).
    *   Implementa un mecanismo de reintentos con esperas para manejar posibles errores de la API o saturación del servidor.
7.  **Traducción de README (Inglés):**
    *   Una vez obtenido el README en español, construye un nuevo `prompt` para solicitar su traducción al inglés, manteniendo la terminología técnica.
    *   Envía este `prompt` a la API del LLM.
    *   También incluye un mecanismo de reintentos.
8.  **Actualización de GitHub:**
    *   Intenta actualizar el archivo `README.md` (español) en el repositorio. Si no existe, lo crea.
    *   Intenta actualizar el archivo `README_English.md` (inglés) en el repositorio. Si no existe, lo crea.
    *   Cada operación de actualización/creación se realiza con un mensaje de commit descriptivo.
9.  **Registro:** Añade el nombre del repositorio al archivo `Consolidado_Documentación.txt` para marcarlo como documentado.
10. **Pausas:** Introduce pausas (`time.sleep`) entre las operaciones de la API para evitar exceder los límites de tasa y para permitir que las APIs procesen las solicitudes.

### 5.2. Payload y Prompts

El `payload` principal enviado a los LLMs es una cadena de texto que contiene las instrucciones para la generación del README y el código fuente del repositorio.

**Ejemplo de `instrucciones` (role: `system`):**

```
Eres un Senior Data Analyst & Automation Analyst. Crea un README.md profesional, exhaustivo y estructurado para este repositorio basándote en el código proporcionado.
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
9. Responde las preguntas de negocio, destaca el valor agregado del código, destaca lo que se muestra, lo que permite medir, lo que permite diagnósticar, lo que permite resolver, acotar, optimizar, estandarizar y repensar (ahonda mucho en esta cuestión)
```

**Ejemplo de `prompt` (role: `user`):**

```
Genera el README.md final para este proyecto aplicando todas las directrices de estructura solicitadas (badges, índice, requisitos de SO, ejemplos de salida). 
Aquí está el código fuente (está acumulado en un solo bloque, así que analízalo detalladamente por ruta de archivo para entender la integración). Del mismo modo, responde las necesidades de negocio, de la investigación :

### Archivo: Groq_Deepsek_backup.py ###
import os
import time
# ... contenido del archivo Groq_Deepsek_backup.py ...

### Archivo: main.py ###
import os
import time
# ... contenido del archivo main.py ...
```

Para la traducción, se utiliza un `prompt` similar, pero con instrucciones específicas para la traducción y el texto del README ya generado.

## 6. Valor Agregado y Justificación Técnica

### 6.1. Respuesta a Necesidades de Negocio

Este sistema de automatización de documentación aborda varias necesidades críticas en el desarrollo de software y la gestión de proyectos:

*   **Resuelve la falta de documentación:** Elimina el cuello de botella de la documentación manual, asegurando que cada repositorio tenga un `README.md` inicial y actualizado.
*   **Estandariza la calidad y estructura:** Al utilizar un LLM con instrucciones precisas, se garantiza una estructura consistente y un nivel de detalle técnico uniforme en todos los READMEs, mejorando la coherencia organizacional.
*   **Optimiza el tiempo del desarrollador:** Libera a los desarrolladores de la tarea repetitiva y a menudo tediosa de escribir documentación, permitiéndoles enfocarse en el desarrollo de código.
*   **Acota el alcance de la documentación:** Se enfoca en los archivos de código fuente clave (`.py`, `.sql`, `.ipynb`, `.json`), asegurando que la documentación sea relevante y directamente vinculada al activo de código.
*   **Permite medir la cobertura de documentación:** El archivo `Consolidado_Documentación.txt` permite un seguimiento claro de qué repositorios han sido procesados, facilitando métricas sobre el estado de la documentación.
*   **Diagnostica inconsistencias:** Al generar documentación de forma programática, se pueden identificar patrones de código o estructuras de repositorio que dificultan la documentación, lo que puede llevar a mejoras en las prácticas de desarrollo.
*   **Repensar la estrategia de documentación:** Transforma la documentación de una tarea reactiva y manual a un proceso proactivo, automatizado y escalable. Esto fomenta la integración de la documentación en los flujos de CI/CD y posiciona a los LLMs como herramientas fundamentales para la gestión del conocimiento técnico.
*   **Valor agregado estratégico:** Mejora la incorporación de nuevos miembros al equipo, facilita la transferencia de conocimiento entre proyectos, reduce la deuda técnica asociada a la falta de documentación y, en última instancia, acelera el ciclo de vida del desarrollo de software.

### 6.2. Justificación de Tecnologías

*   **`python-dotenv`**: Es fundamental para la gestión segura de credenciales. Permite almacenar tokens de API y claves en un archivo `.env` local, manteniéndolos fuera del control de versiones y protegiéndolos de exposiciones accidentales.
*   **`PyGithub`**: Esta librería es la interfaz estándar de Python para la API de GitHub. Su uso simplifica enormemente la interacción con los repositorios, permitiendo operaciones como listar repositorios, acceder a su contenido (archivos y directorios), y realizar commits para crear o actualizar archivos. Su robustez y facilidad de uso son clave para la automatización de las tareas de GitHub.
*   **`openai` (para Groq API)**: Aunque el nombre de la librería es `openai`, se utiliza para interactuar con la API de Groq, que es compatible con la especificación de la API de OpenAI. Groq se elige por su rendimiento excepcional y baja latencia, lo que es crucial para procesar grandes volúmenes de código y generar respuestas rápidamente. Su capacidad para ejecutar modelos de lenguaje de última generación como Llama-3 de manera eficiente lo convierte en una opción atractiva para tareas de generación de texto intensivas.
*   **`google-generativeai` (para Google Gemini API)**: La inclusión de la API de Google Gemini proporciona una alternativa estratégica o un mecanismo de fallback. Gemini, con modelos como `gemini-2.5-flash`, ofrece una potente capacidad de comprensión y generación de texto, siendo una opción robusta y competitiva. La dualidad de proveedores de LLM permite comparar el rendimiento, la calidad de las respuestas y la resiliencia del sistema ante posibles interrupciones de un único proveedor.
*   **Manejo de reintentos y `time.sleep`**: La implementación de reintentos con esperas exponenciales (o fijas en este caso) es una práctica estándar y crítica al interactuar con APIs externas. Protege contra fallos transitorios de red, límites de tasa de API y saturación del servidor, asegurando la robustez y fiabilidad del pipeline de automatización.

## 7. Ejemplos de Salida

El proyecto genera dos tipos principales de salidas: un archivo de registro de repositorios documentados y los archivos `README.md` y `README_English.md` dentro de cada repositorio.

### 7.1. Archivo `Consolidado_Documentación.txt`

Este archivo es un simple registro de texto plano, donde cada línea contiene el nombre de un repositorio que ha sido procesado exitosamente.

```
repo-proyecto-a
mi-proyecto-de-datos
servicio-api-rest
analisis-ventas-q4
```

### 7.2. Contenido del `README.md` Generado

El contenido del `README.md` (y `README_English.md`) es un documento Markdown estructurado, siguiendo las directrices proporcionadas al LLM. A continuación, se muestra un ejemplo de la estructura esperada, no el contenido exacto, ya que este variará según el código del repositorio.

```markdown
# Nombre del Repositorio

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub%20API-Integration-informational?style=flat-square&logo=github&logoColor=white)
![Project Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-Unspecified-lightgrey?style=flat-square)

Este repositorio contiene un proyecto dedicado a [Descripción breve del propósito del proyecto].

## Tabla de Contenidos

*   [1. Visión General](#1-visión-general)
*   [2. Arquitectura](#2-arquitectura)
*   [3. Configuración](#3-configuración)
*   [4. Uso](#4-uso)
*   [5. Estructura de Datos de Salida](#5-estructura-de-datos-de-salida)
*   [6. Valor de Negocio](#6-valor-de-negocio)

## 1. Visión General

El objetivo principal de este proyecto es [Explicación detallada del objetivo]. Se centra en [áreas clave, funcionalidades, etc.].

## 2. Arquitectura

El sistema sigue una arquitectura [cliente-servidor, microservicios, monolítica, etc.]. Los componentes principales incluyen:
*   **Componente A:** [Descripción]
*   **Componente B:** [Descripción]

## 3. Configuración

### 3.1. Dependencias a Nivel de Sistema Operativo

No se requieren dependencias específicas a nivel de sistema operativo más allá de un entorno Python estándar y acceso a red.

### 3.2. Dependencias de Python

Instale las dependencias usando pip:
```bash
pip install -r requirements.txt
```
(O listar las librerías específicas si no hay `requirements.txt`)

### 3.3. Variables de Entorno

Cree un archivo `.env` en la raíz del proyecto con las siguientes variables:
```ini
API_KEY="tu_clave_api"
DATABASE_URL="tu_url_de_base_de_datos"
```

## 4. Uso

Para ejecutar el proyecto:
```bash
python main.py
```
[Instrucciones más detalladas sobre cómo usar el proyecto, ejemplos de comandos, etc.]

## 5. Estructura de Datos de Salida

Si el código genera datos estructurados (ej. JSON, CSV), se mostrará un ejemplo aquí.
Por ejemplo, si un script genera un JSON con resultados de análisis:

```json
{
  "report_id": "REP-2023-10-26-001",
  "analysis_date": "2023-10-26",
  "metrics": {
    "total_records": 1500,
    "average_value": 45.75,
    "max_value": 120.00
  },
  "summary": "Análisis completado con éxito para el período especificado."
}
```

## 6. Valor de Negocio

Este proyecto aporta valor al [mencionar cómo el proyecto resuelve un problema de negocio, mejora un proceso, etc.]. Permite [medir, diagnosticar, resolver, acotar, optimizar, estandarizar, repensar] en el contexto de [dominio de negocio].

---
```

## 8. Contribución

Las contribuciones son bienvenidas. Por favor, abra un 'issue' para discutir cualquier cambio propuesto o envíe un 'pull request'.

## 9. Licencia

Este proyecto no especifica una licencia explícita. Se recomienda añadir un archivo `LICENSE` para definir los términos de uso y distribución.============================================================
Repositorio Asociado: Backend-Territorio
============================================================
# 🗺️ Análisis Geoespacial y Asignación de Recursos Territoriales

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange?style=flat-square&logo=pandas)
![Selenium](https://img.shields.io/badge/Selenium-Web%20Automation-green?style=flat-square&logo=selenium)
![Geopy](https://img.shields.io/badge/Geopy-Geocoding-lightgrey?style=flat-square)
![Folium](https://img.shields.io/badge/Folium-Interactive%20Maps-purple?style=flat-square)
![Gradio](https://img.shields.io/badge/Gradio-Web%20UI-red?style=flat-square)
![Dotenv](https://img.shields.io/badge/Dotenv-Config-yellowgreen?style=flat-square)
![Project Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

---

## 📋 Índice

1.  [Visión General del Proyecto](#1-visión-general-del-proyecto)
2.  [Valor de Negocio y Problemas Resueltos](#2-valor-de-negocio-y-problemas-resueltos)
3.  [Arquitectura y Flujo de Datos (Pipeline)](#3-arquitectura-y-flujo-de-datos-pipeline)
    *   [Componentes del Pipeline](#componentes-del-pipeline)
    *   [Flujo de Ejecución](#flujo-de-ejecución)
4.  [Configuración y Dependencias](#4-configuración-y-dependencias)
    *   [Requisitos a Nivel de Sistema Operativo](#requisitos-a-nivel-de-sistema-operativo)
    *   [Dependencias de Python](#dependencias-de-python)
    *   [Variables de Entorno](#variables-de-entorno)
5.  [Uso](#5-uso)
6.  [Detalle Técnico del Código](#6-detalle-técnico-del-código)
    *   [Extracción de Datos de Entidades Territoriales](#extracción-de-datos-de-entidades-territoriales)
        *   [`Casas de Juventud.py`](#casas-de-juventudpy)
        *   [`Manzanas_Cuidado.py`](#manzanas_cuidadopy)
        *   [`CIO.py`](#ciopy)
    *   [Geocodificación y Consolidación](#geocodificación-y-consolidación)
        *   [`Coordenadas.py`](#coordenadaspy)
    *   [Asignación Geoespacial de Personal](#asignación-geoespacial-de-personal)
        *   [`Georreferenciación.py`](#georreferenciaciónpy)
    *   [Interfaz de Usuario Interactiva](#interfaz-de-usuario-interactiva)
        *   [`app.py`](#apppy)
7.  [Ejemplos de Salida de Datos](#7-ejemplos-de-salida-de-datos)
    *   [`CDJ_FINAL.csv`](#cdj_finalcsv)
    *   [`df_asignaciones.csv`](#df_asignacionescsv)
    *   [Mapas Interactivos HTML](#mapas-interactivos-html)
8.  [Mejoras Futuras](#8-mejoras-futuras)
9.  [Licencia](#9-licencia)

---

## 1. Visión General del Proyecto

Este repositorio alberga una solución integral para la recolección, procesamiento geoespacial y visualización de datos de entidades territoriales de apoyo social (Casas de Juventud, Manzanas del Cuidado, Casas de Igualdad de Oportunidades para las Mujeres) y la asignación óptima de personal a estas entidades. El proyecto automatiza la extracción de información de fuentes web, geocodifica direcciones, calcula distancias geodésicas y genera asignaciones basadas en proximidad, culminando en una aplicación web interactiva para la visualización y análisis de las asignaciones.

## 2. Valor de Negocio y Problemas Resueltos

La gestión eficiente de recursos humanos y la optimización de la cobertura territorial son desafíos críticos para cualquier organización con presencia distribuida. Este proyecto aborda directamente estas problemáticas, proporcionando una herramienta analítica robusta que:

*   **Mide:** La distancia geográfica entre el personal operativo y las entidades territoriales bajo su responsabilidad. Esto cuantifica la eficiencia logística y el tiempo de desplazamiento potencial.
*   **Diagnostica:** Desequilibrios en la carga de trabajo geográfica, asignaciones subóptimas y áreas con baja cobertura o alta concentración de recursos. Permite identificar zonas donde la presencia del personal es ineficiente o donde se requiere una reevaluación de la estrategia de despliegue.
*   **Resuelve:** El problema de la asignación manual y subjetiva de personal a entidades. Mediante un algoritmo de proximidad, se generan asignaciones objetivas y eficientes, minimizando los tiempos de respuesta y maximizando la cobertura.
*   **Acota:** La incertidumbre en la planificación territorial al proporcionar una base de datos geoespacial actualizada y un mecanismo de asignación transparente. Reduce la ambigüedad en la definición de responsabilidades geográficas.
*   **Optimiza:** La logística operativa, los tiempos de desplazamiento del personal y, consecuentemente, los costos asociados. Mejora la capacidad de respuesta y la eficiencia en la prestación de servicios al asegurar que el personal esté asignado a las entidades más cercanas a su ubicación.
*   **Estandariza:** El proceso de asignación de personal a entidades territoriales. Al basarse en criterios geográficos objetivos, se elimina la variabilidad y se establece un procedimiento replicable y auditable.
*   **Repiensa:** La estrategia de despliegue de recursos y la planificación territorial. Los mapas interactivos y los datos de asignación permiten a los tomadores de decisiones visualizar patrones, identificar necesidades emergentes y considerar nuevas ubicaciones para entidades o personal, fomentando una gestión proactiva y basada en datos.

En síntesis, esta solución transforma datos brutos en inteligencia operativa, permitiendo una toma de decisiones estratégica para la optimización de la presencia territorial y la asignación de personal, lo que se traduce en una mejora directa de la eficiencia operativa y la calidad del servicio.

## 3. Arquitectura y Flujo de Datos (Pipeline)

El proyecto sigue una arquitectura modular, donde cada script cumple una función específica dentro de un pipeline de procesamiento de datos.

### Componentes del Pipeline

1.  **Extracción de Datos (Web Scraping):**
    *   **`Casas de Juventud.py`**: Extrae información de Casas de Juventud de un portal web gubernamental.
    *   **`Manzanas_Cuidado.py`**: Extrae información de Manzanas del Cuidado de su sitio web oficial.
    *   **`CIO.py`**: Procesa un archivo CSV preexistente de Casas de Igualdad de Oportunidades y lo integra con los datos de Casas de Juventud.

2.  **Consolidación y Geocodificación:**
    *   **`Coordenadas.py`**: Consolida los datos de todas las entidades, limpia las direcciones y utiliza servicios de geocodificación para obtener las coordenadas de latitud y longitud de cada entidad.

3.  **Georreferenciación y Asignación:**
    *   **`Georreferenciación.py`**: Geocodifica las direcciones del personal, calcula las distancias geodésicas entre cada miembro del personal y cada entidad, y realiza una asignación óptima basada en la mínima distancia.

4.  **Visualización y Interfaz de Usuario:**
    *   **`app.py`**: Genera una aplicación web interactiva utilizando Gradio, que muestra las asignaciones en un mapa Folium y una tabla filtrable.

### Flujo de Ejecución

El pipeline se ejecuta secuencialmente, con cada script generando archivos intermedios que son consumidos por el siguiente paso.

```mermaid
graph TD
    A[Inicio] --> B(Ejecutar Casas de Juventud.py);
    B --> C(Genera CDJ.csv con Casas de Juventud);
    C --> D(Ejecutar Manzanas_Cuidado.py);
    D --> E(Actualiza CDJ.csv con Manzanas del Cuidado);
    E --> F(Ejecutar CIO.py);
    F --> G(Actualiza CDJ.csv con Casas de Igualdad);
    G --> H(Ejecutar Coordenadas.py);
    H --> I(Genera CDJ_FINAL.csv con coordenadas de todas las entidades);
    I --> J(Genera mapa_CDJ.html);
    J --> K(Ejecutar Georreferenciación.py);
    K --> L(Lee CDJ_FINAL.csv y direcciones de personal desde .env);
    L --> M(Calcula distancias y asigna personal a entidades);
    M --> N(Genera df_asignaciones.csv);
    N --> O(Genera Mapa_Final_Asiganciones_CDJ.html);
    O --> P(Ejecutar app.py);
    P --> Q(Lanza interfaz web interactiva con mapa y tabla);
    Q --> R[Fin];
```

**Payloads de Extracción y Geocodificación:**

*   **Web Scraping (`Casas de Juventud.py`, `Manzanas_Cuidado.py`):**
    *   **Input:** URL de la página web.
    *   **Output (Ejemplo de un registro extraído):**
        ```json
        {
            "Nombre": "Casa de Juventud Usme",
            "Dirección": "Carrera 14 # 137-30 Sur",
            "Barrio": "Comuneros",
            "Localidad": "Usme",
            "Contacto": "3102000000"
        }
        ```
        (Similar para Manzanas del Cuidado, con campos adicionales como "Celular" y posible variación en "Contacto").

*   **Geocodificación (`Coordenadas.py`, `Georreferenciación.py`):**
    *   **Input (Query String):** `Dirección, Localidad, Bogotá, Colombia` o `Dirección, Barrio, Bogotá, Colombia`.
        *   Ejemplo: `"Carrera 14 # 137-30 Sur, Usme, Bogotá, Colombia"`
    *   **Output (Objeto de Geocodificación):**
        ```python
        # Representación conceptual del objeto retornado por geolocator.geocode
        Location(address='Carrera 14 # 137-30 Sur, Usme, Bogotá, Colombia', latitude=4.4987, longitude=-74.1234, ...)
        ```

## 4. Configuración y Dependencias

Para ejecutar este proyecto, es necesario configurar tanto dependencias a nivel de sistema operativo como librerías de Python.

### Requisitos a Nivel de Sistema Operativo

*   **Google Chrome:** Los scripts de web scraping (`Casas de Juventud.py`, `Manzanas_Cuidado.py`) utilizan Selenium con el navegador Google Chrome. Asegúrese de tenerlo instalado en su sistema.
*   **ChromeDriver:** Es el controlador necesario para que Selenium interactúe con Google Chrome. La versión de ChromeDriver debe ser compatible con la versión de su navegador Chrome.
    *   **Instalación:**
        1.  Verifique la versión de su Google Chrome (Ayuda > Información de Google Chrome).
        2.  Descargue la versión correspondiente de ChromeDriver desde [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).
        3.  Extraiga el archivo `chromedriver.exe` (o `chromedriver` en Linux/macOS) y colóquelo en una ubicación accesible por el sistema (ej., en el mismo directorio de los scripts o en una ruta incluida en la variable de entorno `PATH`).

### Dependencias de Python

Se recomienda utilizar un entorno virtual para gestionar las dependencias.

1.  **Crear un entorno virtual (opcional pero recomendado):**
    ```bash
    python -m venv venv
    ```
2.  **Activar el entorno virtual:**
    *   Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
3.  **Instalar las dependencias:**
    Cree un archivo `requirements.txt` con el siguiente contenido:
    ```
    pandas
    selenium
    geopy
    folium
    python-dotenv
    gradio
    ```
    Luego, instálelas:
    ```bash
    pip install -r requirements.txt
    ```

### Variables de Entorno

El script `Georreferenciación.py` utiliza variables de entorno para cargar las direcciones del personal.

1.  Cree un archivo `.env` en el directorio raíz del proyecto.
2.  Defina las direcciones del personal en el formato `NOMBRE_PERSONA="Dirección Completa"`:
    ```
    Zamara="Carrera 10 # 20-30, Bogotá"
    Esteban="Calle 50 # 15-25, Bogotá"
    # Agregue más personal según sea necesario
    ```
    **Nota:** Los nombres de las variables de entorno deben coincidir con las claves del diccionario `Info` en `Georreferenciación.py`.

## 5. Uso

Para ejecutar el pipeline completo y lanzar la aplicación web:

1.  Asegúrese de haber completado la [Configuración y Dependencias](#4-configuración-y-dependencias).
2.  Ejecute los scripts en el siguiente orden desde la terminal en el directorio raíz del proyecto:

    ```bash
    python "Casas de Juventud.py"
    python "Manzanas_Cuidado.py"
    python "CIO.py"
    python "Coordenadas.py"
    python "Georreferenciación.py"
    python "app.py"
    ```
    El último comando (`python app.py`) lanzará la interfaz web interactiva en su navegador predeterminado.

## 6. Detalle Técnico del Código

Esta sección profundiza en la lógica y las tecnologías empleadas en cada componente del pipeline.

### Extracción de Datos de Entidades Territoriales

#### `Casas de Juventud.py`

Este script se encarga de la extracción automatizada de datos de las Casas de Juventud.

*   **Tecnología:** `selenium` para la automatización del navegador web.
*   **Lógica:**
    1.  Inicializa un controlador de Chrome y navega a la URL de las Casas de Juventud.
    2.  Utiliza `WebDriverWait` y `expected_conditions` para asegurar que los elementos de la página estén cargados y sean interactuables antes de intentar acceder a ellos, mitigando problemas de sincronización.
    3.  Simula la interacción del usuario haciendo clic en la opción "Todas las localidades" para cargar todos los datos.
    4.  Itera a través de las páginas de resultados, extrayendo el nombre, dirección, barrio, localidad y contacto de cada tarjeta de entidad.
    5.  Detecta el botón de "siguiente página" y su estado `disabled` para determinar cuándo ha llegado al final de la paginación.
    6.  Almacena los datos en una lista de diccionarios.
    7.  Crea un `pandas.DataFrame` y le añade la columna `Tipo` con el valor "Casa de Juventud".
    8.  Guarda el DataFrame resultante en `CDJ.csv`.

*   **Valor Agregado:** Automatiza un proceso de recolección de datos que de otro modo sería manual y propenso a errores, garantizando la frescura y completitud de la información. La robustez de Selenium con `WebDriverWait` es crucial para manejar páginas dinámicas.

#### `Manzanas_Cuidado.py`

Similar al script anterior, este se enfoca en las Manzanas del Cuidado.

*   **Tecnología:** `selenium` para web scraping.
*   **Lógica:**
    1.  Navega a la URL principal de Manzanas del Cuidado.
    2.  Identifica y extrae los enlaces a las páginas individuales de cada Manzana del Cuidado.
    3.  Itera sobre cada enlace, navegando a la página de detalle para extraer información específica: Nombre, Dirección, Barrio, Contacto y Celular.
    4.  Implementa manejo de excepciones (`try-except NoSuchElementException`) para abordar variaciones en la estructura HTML de las páginas de detalle, lo que es común en sitios web heterogéneos.
    5.  Limpia y normaliza los datos extraídos (ej., eliminando saltos de línea, espacios extra).
    6.  Crea un `pandas.DataFrame` con los datos, añade la columna `Tipo` como "Manzana del Cuidado".
    7.  Lee el archivo `CDJ.csv` existente (que ya contiene Casas de Juventud), concatena los nuevos datos de Manzanas del Cuidado y sobrescribe `CDJ.csv`.

*   **Valor Agregado:** Extiende la capacidad de recolección de datos a otra categoría crítica de entidades. La lógica de manejo de errores en la extracción de campos es fundamental para la resiliencia del scraper ante cambios menores en la estructura del sitio web.

#### `CIO.py`

Este script se encarga de integrar datos de Casas de Igualdad de Oportunidades.

*   **Tecnología:** `pandas` para manipulación de datos.
*   **Lógica:**
    1.  Lee un archivo `CIO.csv` preexistente.
    2.  Añade una columna `Tipo` con el valor "Casas de Igualdad de Oportunidades para las Mujeres".
    3.  Renombra la columna ' Barrio' a 'Barrio' para estandarización.
    4.  Formatea la columna `Teléfono` para asegurar un prefijo internacional consistente (`+57`).
    5.  Lee el archivo `CDJ.csv` (que ya contiene Casas de Juventud y Manzanas del Cuidado).
    6.  Concatena los datos de `CIO_CSV` con `CDJ` y sobrescribe `CDJ.csv`.

*   **Valor Agregado:** Consolida diferentes fuentes de datos de entidades territoriales en un formato unificado, preparando el conjunto de datos para la geocodificación y análisis posterior. La estandarización de columnas y formatos es clave para la integridad de los datos.

### Geocodificación y Consolidación

#### `Coordenadas.py`

Este script toma los datos consolidados y los enriquece con información geoespacial.

*   **Tecnología:** `pandas` para manipulación de datos, `geopy` para geocodificación, `folium` para visualización de mapas.
*   **Lógica:**
    1.  Lee el archivo `CDJ.csv`.
    2.  Implementa una función `limpiar_direccion` para estandarizar abreviaturas comunes en direcciones (Cra., Cll., Dg., Av., Trans.). Esto es crucial para mejorar la precisión de la geocodificación.
    3.  Construye una columna `Query_GPS` combinando Dirección, Localidad/Barrio y "Bogotá, Colombia" para formar una cadena de consulta optimizada para el geocodificador.
    4.  Utiliza `geopy.geocoders.ArcGIS` como proveedor de geocodificación, elegido por su robustez y precisión para direcciones en Colombia.
    5.  Aplica `geopy.extra.rate_limiter.RateLimiter` para gestionar las solicitudes al servicio de geocodificación, evitando bloqueos por exceder los límites de tasa de la API. Se establece un `min_delay_seconds` de 1.5 segundos.
    6.  Aplica la función de geocodificación a la columna `Query_GPS` para obtener objetos de coordenadas.
    7.  Extrae la latitud y longitud de los objetos de coordenadas, manejando casos donde la geocodificación podría fallar (`loc is not None`).
    8.  Guarda el DataFrame enriquecido en `CDJ_FINAL.csv`.
    9.  Genera un mapa interactivo (`mapa_CDJ.html`) utilizando `folium`, marcando la ubicación de cada entidad con un icono y popup informativo.

*   **Valor Agregado:** Transforma direcciones textuales en coordenadas geográficas precisas, habilitando análisis espaciales. La elección de ArcGIS y el uso de `RateLimiter` demuestran una implementación técnica consciente de las limitaciones de las APIs y la necesidad de datos precisos. La generación de un mapa inicial permite una verificación visual rápida de la calidad de la geocodificación.

### Asignación Geoespacial de Personal

#### `Georreferenciación.py`

Este es el núcleo del análisis de asignación.

*   **Tecnología:** `pandas`, `geopy` (ArcGIS, geodesic), `python-dotenv`, `folium`.
*   **Lógica:**
    1.  Carga las direcciones del personal desde el archivo `.env` utilizando `python-dotenv`, garantizando que la información sensible no esté codificada directamente en el script.
    2.  Geocodifica las direcciones del personal utilizando `ArcGIS` y `RateLimiter`, de manera similar a las entidades.
    3.  Crea un DataFrame `df` con el personal y sus coordenadas.
    4.  Lee `CDJ_FINAL.csv` (entidades con coordenadas).
    5.  Realiza un `merge` de tipo `cross` entre el DataFrame de entidades y el DataFrame de personal. Esto crea todas las combinaciones posibles de entidad-persona.
    6.  Itera sobre el DataFrame combinado y calcula la `Distancia_km` entre cada entidad y cada persona utilizando `geopy.distance.geodesic`. Esta función es preferible a la distancia euclidiana para coordenadas geográficas, ya que considera la curvatura de la Tierra.
    7.  Ordena las asignaciones por `Nombre_Casa` y `Distancia_km`.
    8.  Agrupa por `Nombre_Casa` y selecciona la primera fila (`.head(1)`), lo que efectivamente asigna cada entidad a la persona más cercana.
    9.  Guarda el DataFrame de asignaciones en `df_asignaciones.csv` y en una subcarpeta `Entidades-Territorio/`.
    10. Genera un mapa interactivo final (`Mapa_Final_Asiganciones_CDJ.html`) utilizando `folium`. Este mapa visualiza:
        *   Marcadores para cada persona (icono de usuario, color verde).
        *   Marcadores para cada entidad asignada (icono de casa, colores distintivos por tipo de entidad: azul para Casas de Juventud, púrpura para Manzanas del Cuidado, morado oscuro para Casas de Igualdad).
        *   Líneas (`folium.PolyLine`) que conectan a cada persona con la entidad que le fue asignada, con colores y estilos de línea diferenciados por tipo de entidad para una mejor interpretación visual.

*   **Valor Agregado:** Este script es fundamental para la toma de decisiones. La combinación de geocodificación, cálculo de distancias geodésicas y la lógica de asignación por proximidad proporciona una base científica para la optimización de recursos. La generación del mapa final con líneas de asignación es una herramienta de visualización poderosa para comunicar los resultados del análisis. El uso de `.env` para datos de personal mejora la seguridad y flexibilidad.

### Interfaz de Usuario Interactiva

#### `app.py`

Este script proporciona una interfaz web para interactuar con los resultados del análisis.

*   **Tecnología:** `pandas`, `gradio`.
*   **Lógica:**
    1.  Lee el archivo `df_asignaciones.csv` (resultados de la asignación).
    2.  Carga el contenido HTML del mapa final (`Mapa_Final_Asiganciones_CDJ.html`) para incrustarlo directamente en la aplicación Gradio.
    3.  Crea una lista de colaboradores únicos para el filtro.
    4.  Define una función `filtro_persona` que filtra el DataFrame de asignaciones basado en el nombre del colaborador seleccionado.
    5.  Construye la interfaz de usuario con `gradio.Blocks`:
        *   Un título Markdown.
        *   Un componente `gr.HTML` que muestra el mapa interactivo.
        *   Otro título Markdown para la sección de la tabla.
        *   Un `gr.Dropdown` para seleccionar un colaborador.
        *   Un `gr.Dataframe` que muestra la tabla de asignaciones.
    6.  Configura el `Dropdown` para que, al cambiar su valor, llame a la función `filtro_persona` y actualice el `Dataframe`.
    7.  Lanza la aplicación Gradio.

*   **Valor Agregado:** Democratiza el acceso a los resultados del análisis. Permite a los usuarios no técnicos explorar las asignaciones de manera interactiva, filtrar por colaborador y visualizar el impacto geográfico de las decisiones. Gradio es una excelente elección para prototipos rápidos y dashboards sencillos, facilitando la interacción con modelos y datos.

## 7. Ejemplos de Salida de Datos

### `CDJ_FINAL.csv`

Este archivo contiene la lista consolidada de todas las entidades (Casas de Juventud, Manzanas del Cuidado, Casas de Igualdad) con sus direcciones geocodificadas (latitud y longitud).

```csv
Nombre,Dirección,Barrio,Localidad,Contacto,Celular,Tipo,Coordenadas,Latitud,Longitud
Casa de Juventud Usme,Carrera 14 # 137-30 Sur,Comuneros,Usme,+57 3102000000,3102000000,Casa de Juventud,"(4.4987, -74.1234)",4.4987,-74.1234
Manzana del Cuidado Bosa,Calle 70 Sur # 80-50,Bosa Central,Bosa,info@manzanabosa.com,3201000000,Manzana del Cuidado,"(4.6012, -74.1876)",4.6012,-74.1876
Casa de Igualdad de Oportunidades para las Mujeres Kennedy,Carrera 78 # 40-10 Sur,Kennedy Central,Kennedy,+57 3005000000,,Casas de Igualdad de Oportunidades para las Mujeres,"(4.6234, -74.1567)",4.6234,-74.1567
```

### `df_asignaciones.csv`

Este archivo contiene el resultado final de la asignación, mostrando qué persona fue asignada a qué entidad, junto con la distancia calculada.

```csv
Nombre_Casa,Dirección_Casa,Barrio,Localidad,Contacto,Celular,Tipo,Latitud_Casa,Longitud_Casa,Nombre_Persona,Dirección_Persona,concat,Coordenadas,Latitud_Persona,Longitud_Persona,Distancia_km
Casa de Juventud Usme,Carrera 14 # 137-30 Sur,Comuneros,Usme,+57 3102000000,3102000000,Casa de Juventud,4.4987,-74.1234,Zamara Perez,Carrera 10 # 20-30,Bogotá, Colombia,"(4.6000, -74.0800)",4.6000,-74.0800,15.23
Manzana del Cuidado Bosa,Calle 70 Sur # 80-50,Bosa Central,Bosa,info@manzanabosa.com,3201000000,Manzana del Cuidado,4.6012,-74.1876,Esteban Corredor,Calle 50 # 15-25,Bogotá, Colombia,"(4.6500, -74.0700)",4.6500,-74.0700,10.55
Casa de Igualdad de Oportunidades para las Mujeres Kennedy,Carrera 78 # 40-10 Sur,Kennedy Central,Kennedy,+57 3005000000,,Casas de Igualdad de Oportunidades para las Mujeres,4.6234,-74.1567,Esteban Corredor,Calle 50 # 15-25,Bogotá, Colombia,"(4.6500, -74.0700)",4.6500,-74.0700,7.89
```

### Mapas Interactivos HTML

Los scripts generan dos archivos HTML con mapas interactivos de Folium:

*   `mapa_CDJ.html`: Muestra la ubicación de todas las entidades geocodificadas.
*   `Mapa_Final_Asiganciones_CDJ.html`: Visualiza las asignaciones de personal a entidades con líneas de conexión y marcadores diferenciados. Este es el mapa incrustado en la aplicación Gradio.

## 8. Mejoras Futuras

*   **Optimización de Asignaciones:** Implementar algoritmos de optimización más avanzados (ej., programación lineal, algoritmos de emparejamiento) para considerar múltiples factores además de la distancia (ej., carga de trabajo, especialización del personal, capacidad de las entidades).
*   **Fuentes de Datos Dinámicas:** Integrar APIs directas de las entidades (si disponibles) en lugar de web scraping para una mayor robustez y actualización en tiempo real.
*   **Interfaz de Administración:** Desarrollar una interfaz para gestionar el personal y sus ubicaciones, así como para cargar nuevas entidades sin necesidad de modificar el archivo `.env` o CSV.
*   **Análisis de Rutas:** Integrar servicios de enrutamiento (ej., Google Maps API, OpenStreetMap) para calcular tiempos de viaje reales y distancias por carretera, en lugar de distancias geodésicas directas.
*   **Monitoreo y Alertas:** Implementar un sistema de monitoreo para detectar cambios en las páginas web de origen y alertar sobre posibles fallos en el web scraping.
*   **Despliegue en la Nube:** Contenerizar la aplicación (Docker) y desplegarla en una plataforma en la nube (ej., AWS, GCP, Azure) para escalabilidad y accesibilidad.

## 9. Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo `LICENSE` para más detalles.============================================================
Repositorio Asociado: BigQuery-Project---ETL-Data-Analysis-
============================================================
[![Google BigQuery](https://img.shields.io/badge/Google%20BigQuery-Service-blue?style=flat-square&logo=google-cloud&logoColor=white)](https://cloud.google.com/bigquery/docs)
[![SQL-ANSI](https://img.shields.io/badge/SQL-Standard%20ANSI-orange?style=flat-square)](https://en.wikipedia.org/wiki/SQL)
[![GCP](https://img.shields.io/badge/GCP-Google%20Cloud%20Platform-red?style=flat-square&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Project Status: Production](https://img.shields.io/badge/Project%20Status-Production-brightgreen?style=flat-square)](#)

# Enterprise Analytics & Employability Pipeline (BigQuery SQL)

Repositorio centralizado de consultas analíticas avanzadas y vistas estructuradas en Google BigQuery. Este proyecto implementa la lógica de extracción, transformación y unificación de datos (ETL/ELT) para el seguimiento académico, control de asistencia, conciliación de telemetría de plataforma, caracterización socioeconómica y métricas de empleabilidad en programas de impacto social y educativo.

---

## Índice

1. [Valor de Negocio y Marco Analítico](#valor-de-negocio-y-marco-analítico)
2. [Arquitectura de Datos y Pipeline](#arquitectura-de-datos-y-pipeline)
3. [Desglose Técnico de Módulos](#desglose-técnico-de-módulos)
   - [Módulo 1: Consultas Empresariales (Core Académico y Telemetría)](#módulo-1-consultas-empresariales-core-académico-y-telemetría)
   - [Módulo 2: Proyecto EFE (Impacto Social y Empleabilidad)](#módulo-2-proyecto-efe-impacto-social-y-empleabilidad)
4. [Requisitos del Sistema y Configuración](#requisitos-del-sistema-y-configuración)
5. [Estructuras de Salida Esperadas (Esquemas JSON)](#estructuras-de-salida-esperadas-esquemas-json)

---

## Valor de Negocio y Marco Analítico

Este repositorio resuelve la fragmentación de datos operativos y de plataforma, transformando registros crudos en activos de información estratégica. El diseño de las consultas permite abordar las siguientes necesidades de negocio:

*   **¿Qué permite medir?**
    *   **Engagement Real:** Cuantifica las horas efectivas de uso de la plataforma educativa por usuario, grupo académico y región geográfica.
    *   **Progreso Hacia la Certificación:** Determina el estado de avance de los estudiantes mediante la clasificación dinámica de estados globales (`GLOBAL_STATUS`), identificando quiénes han completado certificaciones o quiénes tienen pendientes.
    *   **Asistencia y Retención:** Mide la consistencia de la asistencia diaria y periódica, correlacionándola con estados financieros y académicos.
    *   **Impacto Social y NPS:** Centraliza la satisfacción del usuario (Net Promoter Score) evaluando de forma independiente a docentes, contenidos, plataforma y acompañamiento psicosocial.
    *   **Efectividad de Empleabilidad:** Monitorea la tasa de transición de estudiantes a candidatos contratados, evaluando el volumen de postulaciones y remisiones por empresa.

*   **¿Qué permite diagnosticar?**
    *   **Discrepancias de Telemetría:** El módulo de conciliación de horas (`Calculo_Diferencias_Reportes.sql`) compara las vistas de intentos de recursos frente a las vistas de uso activo, diagnosticando desfases en el reporte de logs de la plataforma.
    *   **Deserción Temprana:** Identifica patrones de inasistencia recurrente (`No asistió`, `Tarde`) combinados con estados académicos inactivos para activar alertas de deserción.
    *   **Cuellos de Botella en Empleabilidad:** Detecta en qué fase del embudo (Postulado, En Proceso, Contratado, No Disponible) se detienen los beneficiarios.

*   **¿Qué permite optimizar, estandarizar y repensar?**
    *   **Estandarización de Datos Heterogéneos:** Consolida esquemas de datos dispares provenientes de múltiples proyectos independientes (Proyectos A, B, C y D) en un único modelo unificado de caracterización, seguimiento y empleabilidad.
    *   **Optimización de Consultas:** Implementa técnicas avanzadas de BigQuery como funciones de ventana (`QUALIFY ROW_NUMBER()`), desanidamiento de estructuras (`UNNEST` con `STRUCT`) y expresiones regulares para evitar escaneos innecesarios de tablas y reducir costos de procesamiento.
    *   **Repensar la Estrategia de Acompañamiento:** Permite transitar de un análisis descriptivo reactivo a un monitoreo proactivo, correlacionando variables socioeconómicas (estrato, ingresos, escolaridad) con el rendimiento académico y el éxito en la inserción laboral.

---

## Arquitectura de Datos y Pipeline

El flujo de datos se ejecuta bajo un paradigma ELT dentro de Google BigQuery, estructurado en tres capas lógicas:

```
[ Fuentes de Datos Crudas ] 
       │
       ├── activity_dataset (fact_resources, fact_user_statistics, fact_statistics)
       ├── master_dataset (dim_user, dim_headquarters, dim_academic_component)
       └── dataset_fuente (Tablas crudas de Proyectos A, B, C, D)
       │
       ▼
[ Capa de Transformación (SQL Views & CTEs) ] ───► Conciliación de Telemetría (Diferencia de Horas)
       │
       ├── Normalización de Cadenas (REGEXP_REPLACE, REGEXP_CONTAINS)
       ├── Desanidamiento de Eventos (UNNEST + STRUCT)
       └── Deduplicación Analítica (QUALIFY ROW_NUMBER())
       │
       ▼
[ Capa de Consumo (Vistas Unificadas) ]
       │
       ├── vista_unificada_caracterizacion
       ├── vista_unificada_seguimiento
       ├── vista_unificada_empleabilidad
       └── vista_unificada_satisfaccion
```

1.  **Capa de Ingesta (Raw Data):** Tablas transaccionales de la plataforma educativa, logs de actividad física/digital, registros del CRM de inscripciones y archivos planos de caracterización cargados a Google Cloud Storage.
2.  **Capa de Procesamiento (Transformación y Limpieza):** Consultas SQL que ejecutan parsing de fechas, estandarización de géneros, niveles educativos, rangos de ingresos y cálculo de métricas agregadas.
3.  **Capa de Presentación (Vistas Unificadas):** Vistas optimizadas listas para ser consumidas por herramientas de Business Intelligence (Looker Studio, Power BI) o procesos de extracción automatizados.

---

## Desglose Técnico de Módulos

### Módulo 1: Consultas Empresariales (Core Académico y Telemetría)

Este módulo gestiona la actividad de los usuarios en la plataforma, su asistencia y la consistencia de las métricas de uso.

#### 1. Seguimiento de Progreso y Certificación (`512_Avanza.sql`)
Combina logs de consumo de recursos con estadísticas de progreso del usuario para determinar el estado de certificación global.
*   **Lógica Principal:**
    *   Filtra recursos tipo "Lección" mediante expresiones regulares.
    *   Calcula la edad del usuario en tiempo de ejecución basándose en su fecha de nacimiento.
    *   Utiliza una expresión condicional `CASE` compleja para clasificar el `GLOBAL_STATUS` del usuario según la relación entre grupos asignados y grupos completados (umbral de completitud $\ge 90\%$).
    *   Aplica `QUALIFY ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)` para garantizar un único registro por usuario/curso, priorizando el estado de consumo más alto.

```sql
-- Segmento clave: Deduplicación y ordenamiento de prioridad
PREVIOUS AS (
  SELECT DISTINCT *,
  FROM FINAL
  WHERE REGEXP_CONTAINS(LOWER(ACADEMIC_GROUP), 'group_indicator' )
  QUALIFY ROW_NUMBER() OVER(
    PARTITION BY COURSE, ACADEMIC_GROUP, USER 
    ORDER BY CONTENT_CONSUMPTION_STATUS DESC, COURSE DESC
  ) = 1
)
```

#### 2. Conciliación de Telemetría (`Calculo_Diferencias_Reportes.sql`)
Diagnóstica la consistencia del pipeline de datos comparando dos fuentes de registro de tiempo de uso.
*   **Lógica Principal:**
    *   Une múltiples fuentes de intentos de recursos (`vista_intentos_recurso_1, 2, 3`) mediante `UNION ALL`.
    *   Agrupa el tiempo de uso por año y mes para ambas fuentes (`ATTEMPT_VIEW` vs `USER_ACTIVE_VIEW`).
    *   Calcula la diferencia absoluta y formatea el resultado con separadores de miles para auditoría técnica.

```sql
-- Segmento clave: Cálculo de discrepancia mensual
SELECT
  AV.Anio,
  AV.Mes,
  AV.Horas_totales AS Horas_Attempt_View,
  UA.Horas_totales AS Horas_User_View,
  FORMAT("%'d", CAST(ROUND(AV.Horas_totales - UA.Horas_totales, 0) AS INT64)) AS DIFERENCIA_VISTAS
FROM ATTEMPT_VIEW AS AV
LEFT JOIN USER_ACTIVE_VIEW AS UA
  ON AV.Anio = UA.Anio AND AV.Mes = UA.Mes
```

#### 3. Control de Asistencia y Mapeo de Módulos (`Attendence_COL.sql` y `Attendence_ECO.sql`)
Normaliza los estados de asistencia y mapea las asignaturas dinámicamente a una nomenclatura estándar de módulos (`M0` a `M7`) según el programa académico.

---

### Módulo 2: Proyecto EFE (Impacto Social y Empleabilidad)

Este módulo unifica la información de múltiples proyectos de empleabilidad y formación, resolviendo la inconsistencia en la captura de datos de origen.

#### 1. Normalización de Caracterización (`Views_Caracterizacion.sql`)
Unifica datos demográficos y socioeconómicos de cuatro proyectos diferentes.
*   **Lógica Principal:**
    *   Homogeniza variables críticas como:
        *   **Ciudad de Residencia:** Mapea variaciones de escritura a `"Bogotá D. C."` y `"Cartagena Colombia"`.
        *   **Género:** Estandariza valores como `male`, `female`, `fem` a `"Masculino"` o `"Femenino"`.
        *   **Ingresos Mensuales:** Clasifica textos libres en rangos basados en el Salario Mínimo Mensual Legal Vigente (SMMLV).
        *   **Escolaridad:** Agrupa categorías educativas en niveles estándar (e.g., `"Técnico/Tecnológico completo"`, `"Universitario incompleto"`).

```sql
-- Segmento clave: Estandarización de escolaridad mediante Regex
CASE
  WHEN Escolaridad IS NULL OR Escolaridad = 'None' THEN 'Sin información'
  WHEN REGEXP_CONTAINS(LOWER(Escolaridad), 'ninguno|sin estudios') THEN 'Sin estudios'
  WHEN REGEXP_CONTAINS(LOWER(Escolaridad), 'posgrado|postgrado') THEN 'Postgrado'
  WHEN REGEXP_CONTAINS(LOWER(Escolaridad), 'universitario.*incompleto') THEN 'Universitario incompleto'
  WHEN REGEXP_CONTAINS(LOWER(Escolaridad), 'universitario|pregrado|profesional') THEN 'Universitario completo'
  ELSE Escolaridad
END AS Escolaridad
```

#### 2. Pivotado de Eventos de Empleabilidad (`Pivots_Empleabilidad_Suba.sql`)
Transforma un modelo de datos ancho (donde cada evento es una columna) a un modelo largo (filas por evento) para facilitar el análisis temporal en herramientas de visualización.
*   **Lógica Principal:**
    *   Utiliza la función `UNNEST` combinada con un arreglo de estructuras (`STRUCT`) para normalizar las columnas `fecha_evento_1` a `fecha_evento_5` en registros individuales con su respectivo atributo de tipo de evento.

```sql
-- Segmento clave: Unpivoting eficiente en BigQuery
SELECT
  documento_identidad,
  nombre_completo,
  eventos.tipo_evento,
  eventos.fecha_evento_unificada
FROM `mi_proyecto_gcp.dataset_analitica.tabla_base_eventos_extendida`,
UNNEST([
    STRUCT('Evento 1' AS tipo_evento, fecha_evento_1 AS fecha_evento_unificada),
    STRUCT('Evento 2' AS tipo_evento, fecha_evento_2 AS fecha_evento_unificada),
    STRUCT('Evento 3' AS tipo_evento, fecha_evento_3 AS fecha_evento_unificada),
    STRUCT('Evento 4' AS tipo_evento, fecha_evento_4 AS fecha_evento_unificada),
    STRUCT('Evento 5' AS tipo_evento, fecha_evento_5 AS fecha_evento_unificada)
]) AS eventos
```

---

## Requisitos del Sistema y Configuración

Para ejecutar, automatizar o desplegar estas consultas y vistas en un entorno de producción, se requieren los siguientes componentes a nivel de sistema operativo e infraestructura:

### 1. Requisitos de Infraestructura y Permisos (GCP)
*   **Google Cloud Project (GCP):** Acceso activo a un proyecto con BigQuery habilitado.
*   **Roles de IAM Requeridos:**
    *   `roles/bigquery.dataEditor` (para crear y modificar tablas/vistas).
    *   `roles/bigquery.jobUser` (para ejecutar consultas).
    *   `roles/bigquery.metadataViewer` (para explorar esquemas).

### 2. Herramientas de Línea de Comandos (CLI)
*   **Google Cloud CLI (gcloud):** Requerido para autenticación y despliegue automatizado.
    *   [Instrucciones de instalación de gcloud CLI](https://cloud.google.com/sdk/docs/install)
*   **bq Command-Line Tool:** Incluido en gcloud CLI, utilizado para ejecutar scripts SQL directamente desde la terminal.

### 3. Entorno de Automatización (Opcional - Python)
Si las consultas se integran en un pipeline de orquestación (e.g., Apache Airflow, Prefect, Google Cloud Functions), se requiere:
*   **Python**
*   **Librerías del Sistema Operativo:**
    *   `libffi-dev` y `libssl-dev` (necesarias para la autenticación segura de GCP en entornos Linux).
*   **Dependencias de Python (instalables vía pip):**
    ```bash
    pip install google-cloud-bigquery pandas db-dtypes
    ```

### 4. Despliegue de Vistas desde Terminal
Para desplegar las vistas unificadas de manera automatizada, ejecute el siguiente comando en su terminal:
```bash
gcloud auth login
bq query --use_legacy_sql=false < "Proyecto EFE/Views_Caracterizacion.sql"
```

---

## Estructuras de Salida Esperadas (Esquemas JSON)

A continuación se presentan ejemplos de la estructura de datos resultante generada por las consultas principales:

### 1. Salida de Seguimiento de Progreso (`512_Avanza.sql`)
Representa el estado consolidado de avance y uso de plataforma por usuario.

```json
[
  {
    "SIS_ID": 98765,
    "EMAIL": "usuario.estudiante@example.com",
    "FULL_NAME": "Persona Uno",
    "BIRTH_DATE": "15/08/1998",
    "AGE": 27,
    "GENDER": "Femenino",
    "DOCUMENT": "1000200300",
    "EDUCATIONAL_CENTER": "Centro Educativo Principal",
    "REGION": "Regional Norte",
    "REGION_CODE": "01 - Regional Norte",
    "DISTRICT": "Distrito Educativo 2",
    "SECTOR": "Oficial",
    "COUNTRY": "Generic Country",
    "CYCLE": "Ciclo Técnico",
    "ACADEMIC_GROUP": "group_indicator_A",
    "COURSE": "Desarrollo de Software",
    "RESOURCE_TYPE": "Lección Interactiva",
    "CONTENT_CONSUMPTION_STATUS": "Completado",
    "HOURS_OF_USE": 12.45,
    "LAST_ACCESS": "28-02-2026",
    "acamedic_component_name": "Introducción a SQL",
    "CONSUMPTION_STATUS": 100,
    "GLOBAL_STATUS": "CERTIFICACIONES COMPLETAS OBTENIDAS",
    "TOTAL_HOURS_OF_USE": 45.8
  }
]
```

### 2. Salida de Conciliación de Telemetría (`Calculo_Diferencias_Reportes.sql`)
Muestra la comparación mensual de horas registradas por diferentes componentes de tracking.

```json
[
  {
    "Anio": 2026,
    "Mes": 2,
    "Horas_Attempt_View": 15420.50,
    "Horas_User_View": 15395.20,
    "DIFERENCIA_VISTAS": "25"
  },
  {
    "Anio": 2026,
    "Mes": 1,
    "Horas_Attempt_View": 12800.10,
    "Horas_User_View": 12810.40,
    "DIFERENCIA_VISTAS": "-10"
  }
]
```

### 3. Salida de Caracterización Unificada (`Views_Caracterizacion.sql`)
Muestra los datos demográficos estandarizados de los beneficiarios de los proyectos.

```json
[
  {
    "Nombre": "Persona Dos",
    "Tipo_documento": "Cédula de Ciudadanía",
    "Documento": "10203040",
    "Fecha_nacimiento": "1995-04-12",
    "Edad": 30,
    "Estrato": "Estrato 2",
    "Sexo": "Masculino",
    "Actividad_principal": "Trabajar",
    "Proyecto": "Proyecto_A",
    "Ciudad_residencia": "Bogotá D. C.",
    "Numero_hijos_Personas_cargo": "Dos (2)",
    "Ingresos": "Entre 1 y 2 SMMLV",
    "Escolaridad": "Técnico/Tecnológico completo"
  }
]
```
============================================================
Repositorio Asociado: Cerebritos-Data-Analysis
============================================================
# Procesamiento y Agregación de Logs de Gamificación

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-Proprietary-blue)

Este repositorio contiene un script de Python diseñado para consolidar, limpiar y agregar datos de logs de gamificación provenientes de múltiples fuentes CSV. El objetivo principal es transformar datos brutos y fragmentados en un formato estructurado y analizable, facilitando la medición del engagement de los usuarios y el rendimiento por nivel educativo.

## Índice

1.  [Visión General del Proyecto](#1-visión-general-del-proyecto)
2.  [Arquitectura y Lógica del Pipeline](#2-arquitectura-y-lógica-del-pipeline)
    *   [Payload de Entrada](#payload-de-entrada)
    *   [Flujo del Pipeline](#flujo-del-pipeline)
3.  [Configuración y Dependencias](#3-configuración-y-dependencias)
    *   [Dependencias del Sistema Operativo](#dependencias-del-sistema-operativo)
    *   [Dependencias de Python](#dependencias-de-python)
    *   [Instalación](#instalación)
4.  [Estructura de Salida de Datos](#4-estructura-de-salida-de-datos)
    *   [Cerebros_parcial.csv](#cerebros_parcialcsv)
    *   [CSV_AGRUPADO.csv](#csv_agrupadocsv)
5.  [Análisis Técnico y Justificación de Librerías](#5-análisis-técnico-y-justificación-de-librerías)
6.  [Valor de Negocio y Aplicaciones](#6-valor-de-negocio-y-aplicaciones)
    *   [Preguntas de Negocio Abordadas](#preguntas-de-negocio-abordadas)
    *   [Valor Agregado](#valor-agregado)
    *   [Capacidades de Medición y Diagnóstico](#capacidades-de-medición-y-diagnóstico)
    *   [Resolución, Optimización y Estandarización](#resolución-optimización-y-estandarización)
    *   [Oportunidades de Repensar Estrategias](#oportunidades-de-repensar-estrategias)

---

## 1. Visión General del Proyecto

Este proyecto aborda la necesidad de consolidar y estandarizar datos de gamificación dispersos en múltiples archivos CSV. El script `main.py` automatiza la fusión de estos datasets, la selección y renombramiento de columnas clave, la normalización de identificadores de nivel educativo y la agregación de métricas de engagement. El resultado es un conjunto de datos limpio y listo para análisis, que permite una comprensión profunda del comportamiento del usuario dentro del sistema de gamificación.

## 2. Arquitectura y Lógica del Pipeline

La arquitectura del proyecto es de tipo ETL (Extract, Transform, Load) basada en un script monolítico de Python.

### Payload de Entrada

El pipeline requiere dos archivos CSV de entrada ubicados en el mismo directorio que el script `main.py`:

*   `Gamificación ago- dic.csv`: Contiene logs de gamificación de un período inicial.
*   `kuepa_sis.gamification_logsDic02-Mar1.csv`: Contiene logs de gamificación de un período posterior.

Ambos archivos deben contener columnas que permitan la extracción de `_id`, `user`, `increm[0]`, `correo[0]`, `Nivel[0][0]`, `logs[0].stats[0].value`, `logs[0].stats[0].message`, y `created_at`.

### Flujo del Pipeline

El script `main.py` ejecuta la siguiente secuencia de operaciones:

1.  **Extracción y Consolidación (Extract & Concatenate):**
    *   Carga `Gamificación ago- dic.csv` y `kuepa_sis.gamification_logsDic02-Mar1.csv` en DataFrames de Pandas.
    *   Concatena ambos DataFrames verticalmente para crear un dataset unificado.
    *   Guarda el dataset consolidado inicial como `cerebritos.csv`.

    ```python
    import pandas as pd

    data1 = pd.read_csv("Gamificación ago- dic.csv")
    data2 = pd.read_csv("kuepa_sis.gamification_logsDic02-Mar1.csv")
    data = pd.concat([data1, data2])
    data.to_csv("cerebritos.csv")
    ```

2.  **Selección y Renombramiento de Columnas (Transform - Selection & Renaming):**
    *   Selecciona un subconjunto específico de columnas relevantes para el análisis.
    *   Renombra estas columnas a nombres más descriptivos y amigables para el usuario.

    ```python
    columnas_necesarias = ["_id", "user", "increm[0]", "correo[0]", "Nivel[0][0]", "logs[0].stats[0].value", "logs[0].stats[0].message", "created_at"]
    df = df[columnas_necesarias]

    df = df.rename(columns={
        "logs[0].stats[0].value": "Cantidad Cerebritos",
        "logs[0].stats[0].message": "Razón de Cerebritos",
        "increm[0]": "ID_SIS",
        "correo[0]": "Correo",
        "_id": "ID_Logs",
        "user": "Id_User",
        "Nivel[0][0]": "Grado",
        "created_at": "Fecha"
    })
    ```

3.  **Normalización de Datos (Transform - Normalization):**
    *   Mapea los identificadores internos de los niveles educativos (ej. "6304e6f54ede93101de8c818") a descripciones legibles (ej. "6to Grado").

    ```python
    df['Grado'] = df['Grado'].replace("6304e6f54ede93101de8c818", "6to Grado")
    df['Grado'] = df['Grado'].replace("6304e6ecdff9db10550fabd1", "5to Grado")
    # ... (otras reemplazos de grados)
    ```

4.  **Guardado Intermedio (Load - Intermediate):**
    *   Guarda el DataFrame transformado hasta este punto como `Cerebros_parcial.csv`.

    ```python
    df.to_csv("Cerebros_parcial.csv")
    ```

5.  **Agregación de Datos (Transform - Aggregation):**
    *   Agrupa los datos por `Correo` y `Grado`.
    *   Calcula la suma total de "Cantidad Cerebritos" para cada combinación de `Correo` y `Grado`.

    ```python
    columnas_agrupacion = ["Correo", "Grado"]
    df_agrupado = df.groupby(columnas_agrupacion).agg(
        Total_cerebritos=('Cantidad Cerebritos', 'sum')
    ).reset_index()
    ```

6.  **Guardado Final (Load - Final):**
    *   Guarda el DataFrame agregado como `CSV_AGRUPADO.csv`.
    *   Guarda el DataFrame completo y limpio como `Listado_Completo.csv`.

    ```python
    df_agrupado.to_csv("CSV_AGRUPADO.csv")
    df.to_csv("Listado_Completo.csv")
    ```

## 3. Configuración y Dependencias

### Dependencias del Sistema Operativo

Este script no requiere dependencias a nivel de sistema operativo (ej. FFmpeg, Tesseract, controladores específicos). Su ejecución es independiente de componentes externos más allá del intérprete de Python.

### Dependencias de Python

El script depende exclusivamente de la librería `pandas`.

### Instalación

1.  **Clonar el Repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2.  **Crear un Entorno Virtual (Recomendado):**
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instalar Dependencias:**
    ```bash
    pip install pandas
    ```

4.  **Colocar Archivos de Entrada:**
    Asegúrese de que los archivos `Gamificación ago- dic.csv` y `kuepa_sis.gamification_logsDic02-Mar1.csv` estén presentes en el mismo directorio que `main.py`.

5.  **Ejecutar el Script:**
    ```bash
    python main.py
    ```

## 4. Estructura de Salida de Datos

El script genera varios archivos CSV. A continuación, se muestran ejemplos de la estructura de los dos archivos de salida más relevantes para el análisis.

### `Cerebros_parcial.csv`

Este archivo contiene el listado completo de logs de gamificación, con columnas seleccionadas, renombradas y los grados normalizados.

```csv
ID_Logs,Id_User,ID_SIS,Correo,Grado,Cantidad Cerebritos,Razón de Cerebritos,Fecha
65e4d204d80a3a00085a1a1a,6304e6f54ede93101de8c818,12345,usuario1@ejemplo.com,6to Grado,100,Completó Misión A,2023-01-15T10:30:00.000Z
65e4d204d80a3a00085a1a1b,6304e6ecdff9db10550fabd1,67890,usuario2@ejemplo.com,5to Grado,50,Respondió Pregunta,2023-01-15T11:00:00.000Z
65e4d204d80a3a00085a1a1c,6304e6f54ede93101de8c818,12345,usuario1@ejemplo.com,6to Grado,20,Participó en Foro,2023-01-15T11:15:00.000Z
```

### `CSV_AGRUPADO.csv`

Este archivo presenta la suma total de "Cantidad Cerebritos" por cada combinación única de `Correo` y `Grado`, ideal para análisis de rendimiento agregado.

```csv
Correo,Grado,Total_cerebritos
usuario1@ejemplo.com,6to Grado,120
usuario2@ejemplo.com,5to Grado,50
usuario3@ejemplo.com,4to Grado,80
```

## 5. Análisis Técnico y Justificación de Librerías

El script utiliza la librería `pandas` de Python, una herramienta fundamental para la manipulación y análisis de datos tabulares.

*   **`pandas.read_csv()`**: Permite la carga eficiente de datos desde archivos CSV a objetos `DataFrame`, que son la estructura de datos central de `pandas`. Su robustez maneja diversos formatos y opciones de parseo.
*   **`pandas.concat()`**: Esencial para la unificación de datasets. Permite combinar DataFrames a lo largo de un eje específico (en este caso, verticalmente, `axis=0`), lo que es crucial para consolidar logs de diferentes períodos en un único conjunto de datos coherente.
*   **Selección de Columnas (`df[columnas_necesarias]`)**: La notación de indexación de `pandas` facilita la selección precisa de subconjuntos de columnas, eliminando datos irrelevantes y reduciendo la complejidad del DataFrame.
*   **`DataFrame.rename()`**: Permite cambiar los nombres de las columnas de manera programática. Esto es vital para transformar nombres de columnas crípticos o generados automáticamente (ej. `logs[0].stats[0].value`) en etiquetas claras y significativas para el análisis (ej. `Cantidad Cerebritos`).
*   **`Series.replace()`**: Utilizado para la normalización de datos categóricos. En este caso, mapea IDs internos de grados a descripciones legibles por humanos, lo que mejora la interpretabilidad de los datos sin alterar la estructura subyacente.
*   **`DataFrame.groupby().agg().reset_index()`**: Esta secuencia de operaciones es el corazón de la agregación de datos.
    *   `groupby()`: Agrupa el DataFrame por una o más columnas (`Correo`, `Grado`), creando grupos lógicos de filas con valores idénticos en esas columnas.
    *   `agg()`: Aplica una o más funciones de agregación a los grupos. En este caso, se utiliza para calcular la `sum` de `Cantidad Cerebritos`, y se le asigna un nuevo nombre a la columna resultante (`Total_cerebritos`).
    *   `reset_index()`: Convierte las columnas de agrupación de nuevo en columnas regulares del DataFrame, lo que es útil para exportar los resultados a un formato plano como CSV.

La elección de `pandas` se justifica por su rendimiento optimizado para operaciones con grandes volúmenes de datos tabulares, su API intuitiva y su amplia adopción en la comunidad de ciencia de datos, lo que garantiza mantenibilidad y escalabilidad. Su capacidad para manejar datos heterogéneos y realizar transformaciones complejas con pocas líneas de código lo convierte en la herramienta ideal para este tipo de pipeline ETL.

## 6. Valor de Negocio y Aplicaciones

Este script de procesamiento de datos de gamificación ofrece un valor significativo al transformar datos brutos en inteligencia accionable, permitiendo una gestión más estratégica de las iniciativas de engagement.

### Preguntas de Negocio Abordadas

*   ¿Cuál es el nivel de engagement general de los usuarios con el sistema de gamificación?
*   ¿Cómo se distribuyen los "Cerebritos" (puntos de gamificación) entre los diferentes usuarios y grados?
*   ¿Existen diferencias significativas en la participación de gamificación entre los distintos niveles educativos?
*   ¿Qué usuarios son los más activos y cuáles podrían necesitar incentivos adicionales?

### Valor Agregado

El principal valor agregado de este script radica en la **centralización y estandarización de la información de gamificación**. Al consolidar datos de múltiples fuentes y normalizar sus formatos, se elimina la necesidad de procesamiento manual, reduciendo errores y el tiempo de preparación para el análisis. Esto permite a los analistas y gestores de producto enfocarse en la interpretación de los datos en lugar de su limpieza.

### Capacidades de Medición y Diagnóstico

*   **Medición:**
    *   **Total de "Cerebritos" por usuario y grado:** Cuantifica el rendimiento individual y colectivo.
    *   **Frecuencia de logs:** Permite inferir la actividad general de los usuarios.
    *   **Distribución de engagement:** Mide cómo se reparte la participación a través de la base de usuarios y los segmentos educativos.
*   **Diagnóstico:**
    *   **Identificación de brechas de engagement:** Permite detectar qué grados o grupos de usuarios muestran menor actividad, señalando posibles problemas en la relevancia o diseño de la gamificación para esos segmentos.
    *   **Detección de usuarios de alto rendimiento:** Facilita la identificación de "campeones" que pueden servir como modelos o para estudios de caso.
    *   **Análisis de tendencias:** Al consolidar datos a lo largo del tiempo, se pueden diagnosticar cambios en el engagement y la efectividad de las actualizaciones de gamificación.

### Resolución, Optimización y Estandarización

*   **Resuelve:**
    *   **Fragmentación de datos:** Unifica la información de gamificación dispersa en múltiples archivos.
    *   **Inconsistencia de datos:** Normaliza nombres de columnas y valores categóricos (ej. IDs de grados).
    *   **Dificultad de análisis:** Proporciona un dataset limpio y estructurado, listo para herramientas de BI o análisis estadístico.
*   **Optimiza:**
    *   **Tiempo de preparación de datos:** Automatiza un proceso que de otro modo sería manual y propenso a errores.
    *   **Eficiencia del análisis:** Los datos pre-procesados aceleran cualquier análisis posterior.
    *   **Toma de decisiones:** Al tener datos fiables y accesibles, las decisiones sobre la estrategia de gamificación pueden tomarse más rápidamente y con mayor fundamento.
*   **Estandariza:**
    *   **Formato de logs:** Asegura que todos los logs de gamificación sigan una estructura y nomenclatura consistentes.
    *   **Métricas clave:** Define claramente cómo se calculan y presentan las métricas de engagement.

### Oportunidades de Repensar Estrategias

La información generada por este pipeline permite **repensar** fundamentalmente las estrategias de gamificación:

*   **Diseño de Incentivos:** Si un grado específico muestra un bajo total de "Cerebritos", se puede repensar el tipo de actividades gamificadas o recompensas ofrecidas para ese grupo demográfico. Por ejemplo, los estudiantes de grados inferiores podrían responder mejor a recompensas tangibles o actividades más visuales, mientras que los de grados superiores podrían valorar más el reconocimiento o desafíos complejos.
*   **Segmentación de Contenido:** Al entender qué grados son más activos, se puede repensar la segmentación del contenido gamificado, adaptando los desafíos y las narrativas a los intereses y capacidades de cada nivel educativo.
*   **Intervenciones Dirigidas:** Se puede repensar la implementación de intervenciones proactivas para usuarios o grados con bajo engagement, ofreciendo apoyo personalizado o nuevas oportunidades de participación.
*   **Evaluación de Impacto:** La capacidad de medir el total de "Cerebritos" permite evaluar el impacto directo de nuevas características de gamificación o campañas específicas, llevando a un ciclo de mejora continua.
*   **Benchmarking Interno:** Los datos agregados por grado permiten establecer benchmarks internos de engagement, facilitando la identificación de las mejores prácticas entre los diferentes niveles educativos.

En resumen, este script no solo procesa datos, sino que habilita una capa de inteligencia de negocio que permite a la organización diagnosticar el estado actual de su gamificación, optimizar sus procesos y, lo más importante, repensar y evolucionar sus estrategias para maximizar el engagement y el impacto educativo.============================================================
Repositorio Asociado: Control_periodizacion_unificacion_DATA
============================================================
# Data Ingestion and Management Pipeline

Este repositorio alberga una colección de scripts diseñados para la ingesta, transformación y gestión de datos provenientes de diversas fuentes operacionales (principalmente Google Sheets) hacia un Data Warehouse centralizado en Google BigQuery. El sistema automatiza la limpieza, validación y carga de datos para múltiples proyectos, asegurando la consistencia y disponibilidad de la información para análisis y reportes.

---

## Badges

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-BigQuery-orange?style=for-the-badge&logo=google-cloud)
![Google Sheets](https://img.shields.io/badge/Google_Sheets-API-green?style=for-the-badge&logo=google-sheets)
![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-red?style=for-the-badge&logo=pandas)
![Project Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

---

## Índice

1.  [Visión General del Proyecto](#1-visión-general-del-proyecto)
2.  [Arquitectura del Sistema](#2-arquitectura-del-sistema)
    *   [Flujo de Datos](#21-flujo-de-datos)
    *   [Componentes Principales](#22-componentes-principales)
3.  [Estructura del Repositorio](#3-estructura-del-repositorio)
4.  [Configuración del Entorno](#4-configuración-del-entorno)
    *   [Dependencias a Nivel de Sistema Operativo](#41-dependencias-a-nivel-de-sistema-operativo)
    *   [Dependencias de Python](#42-dependencias-de-python)
    *   [Variables de Entorno](#43-variables-de-entorno)
    *   [Autenticación de Google Cloud](#44-autenticación-de-google-cloud)
5.  [Lógica Principal y Pipeline](#5-lógica-principal-y-pipeline)
    *   [Scripts de Ingestión de Datos (Upload)](#51-scripts-de-ingestión-de-datos-upload)
    *   [Módulo de Validación de Esquemas (`validacion_dataframes.py`)](#52-módulo-de-validación-de-esquemas-validacion_dataframespy)
    *   [Script de Apéndice Histórico (`Append_DATA_BQ.py`)](#53-script-de-apéndice-histórico-append_data_bqpy)
    *   [Scripts de Perfilado de Datos (`Limpieza_*.py`)](#54-scripts-de-perfilado-de-datos-limpieza_py)
    *   [Orquestador de Ejecución (`trigger.py`)](#55-orquestador-de-ejecución-triggerpy)
6.  [Ejemplos de Salida de Datos](#6-ejemplos-de-salida-de-datos)
    *   [DataFrame Limpio (Previo a BigQuery)](#61-dataframe-limpio-previo-a-bigquery)
    *   [Tabla de Apéndice Histórico en BigQuery](#62-tabla-de-apéndice-histórico-en-bigquery)
7.  [Valor de Negocio y Capacidades Analíticas](#7-valor-de-negocio-y-capacidades-analíticas)
    *   [Lo que se Muestra](#71-lo-que-se-muestra)
    *   [Lo que Permite Medir](#72-lo-que-permite-medir)
    *   [Lo que Permite Diagnosticar](#73-lo-que-permite-diagnosticar)
    *   [Lo que Permite Resolver](#74-lo-que-permite-resolver)
    *   [Lo que Permite Acotar](#75-lo-que-permite-acotar)
    *   [Lo que Permite Optimizar](#76-lo-que-permite-optimizar)
    *   [Lo que Permite Estandarizar](#77-lo-que-permite-estandarizar)
    *   [Lo que Permite Repensar](#78-lo-que-permite-repensar)

---

## 1. Visión General del Proyecto

Este proyecto automatiza la extracción, transformación y carga (ETL) de datos desde Google Sheets hacia Google BigQuery. Su objetivo principal es consolidar información operativa de múltiples programas y proyectos (e.g., "Ecolombia 2.0", "Colsubsidio 2026", "Jóvenes a la E", "Suba es Oportunidad") en un formato estructurado y centralizado. Esto facilita el análisis de datos, la generación de informes y la toma de decisiones basada en evidencia, eliminando la dependencia de procesos manuales propensos a errores y lentos.

---

## 2. Arquitectura del Sistema

La arquitectura se basa en un enfoque de micro-servicios (scripts) que interactúan con APIs de Google Cloud y bibliotecas de procesamiento de datos.

### 2.1 Flujo de Datos

El pipeline de datos sigue un patrón claro:

1.  **Origen**: Datos operativos residen en hojas de cálculo de Google Sheets, gestionadas por diferentes equipos de proyecto.
2.  **Extracción**: Los scripts de Python utilizan la API de Google Sheets (`gspread`) para leer los datos.
3.  **Transformación**: `pandas` se emplea para realizar operaciones de limpieza, normalización de nombres de columnas, conversión de tipos de datos, manejo de valores nulos y eliminación de duplicados.
4.  **Validación**: Un módulo de validación de esquemas compara la estructura del DataFrame transformado con el esquema de la tabla de destino en BigQuery para prevenir inconsistencias.
5.  **Carga**: Los datos limpios y validados se cargan en tablas específicas de Google BigQuery (`google-cloud-bigquery`).
6.  **Orquestación**: Un script `trigger.py` coordina la ejecución de todos los scripts de ingesta.
7.  **Apéndice Histórico**: Un script dedicado (`Append_DATA_BQ.py`) gestiona la creación de instantáneas históricas de ciertas tablas en BigQuery.
8.  **Perfilado de Datos**: Scripts de limpieza (`Limpieza_*.py`) permiten inspeccionar la calidad de los datos ya cargados en BigQuery.

### 2.2 Componentes Principales

*   **Google Sheets**: Fuente de datos primarios.
*   **Google Cloud BigQuery**: Data Warehouse escalable y sin servidor para el almacenamiento y análisis de datos.
*   **Python Scripts**:
    *   **Scripts de Ingestión (`Upload_*.py`, `Caracterizacion_*.py`, `Empleabilidad_*.py`, `Satisfaccion_*.py`, `CONVOCATORIA_*.py`, `UnificadoFormacion_*.py`)**: Responsables de la extracción, limpieza y carga de datos para cada fuente específica.
    *   **`validacion_dataframes.py`**: Módulo de control de calidad de esquemas.
    *   **`Append_DATA_BQ.py`**: Gestiona la creación de tablas históricas.
    *   **`Limpieza_*.py`**: Scripts de perfilado de datos para BigQuery.
    *   **`trigger.py`**: Orquestador principal del pipeline de ingesta.
*   **`credenciales.json`**: Archivo de credenciales de cuenta de servicio para autenticación en Google Cloud.
*   **`.env`**: Archivo para la gestión segura de variables de entorno (IDs de proyectos, datasets, hojas de cálculo).

---

## 3. Estructura del Repositorio

```
.
├── Append_DATA_BQ.py
├── CONVOCATORIA_ECOLOMBIA_2026.py
├── Caracterizacion Colsubsidio2026.py
├── Caracterizacion_ECO_2026.py
├── Caracterizacion_JAE_2026.py
├── Caracterizacion_Suba2026.py
├── Empleabilidad_ECO.py
├── Empleabilidad_JAE_2026_V1.0.py
├── Empleabilidad_Suba2026.py
├── Limpieza_caracterizacion.py
├── Limpieza_empleabilidad.py
├── Limpieza_satisfaccion.py
├── Limpieza_seguimiento.py
├── Satisfaccion_Colsubsidio2026.py
├── Satisfaccion_ECO.py
├── Satisfaccion_JAE_2026.py
├── Satisfaccion_Suba.py
├── UnificadoFormacion_Suba2026.py
├── Upload Colsubsidio2026.py
├── Upload Suba2026.py
├── Upload_ECO++_2026.py
├── Upload_JAE_2026.py
├── trigger.py
├── validacion_dataframes.py
├── credenciales.json
└── .env
```

---

## 4. Configuración del Entorno

Para ejecutar los scripts, es necesario configurar el entorno de desarrollo y autenticación.

### 4.1 Dependencias a Nivel de Sistema Operativo

Este proyecto no requiere dependencias específicas a nivel de sistema operativo más allá de una instalación estándar de Python. Todas las bibliotecas necesarias se gestionan a través de `pip`.

### 4.2 Dependencias de Python

Las bibliotecas de Python requeridas se listan a continuación. Se recomienda usar un entorno virtual para su instalación.

```bash
pip install pandas gspread google-cloud-bigquery python-dotenv
```

### 4.3 Variables de Entorno

Se utiliza un archivo `.env` para gestionar variables de entorno sensibles y configuraciones específicas del proyecto. Este archivo **no debe ser versionado** en sistemas de control de código fuente.

Cree un archivo `.env` en la raíz del proyecto con el siguiente formato, reemplazando los valores de ejemplo con los suyos:

```dotenv
PROJECT_ID="your-gcp-project-id"
DATA_SET="your-bigquery-dataset-id"
Sheets_Convocatoria_ECO="google-sheet-id-for-ecolombia-convocatoria"
Sheets_Colsubsidio="google-sheet-id-for-colsubsidio"
Sheets_JAE="google-sheet-id-for-jae"
Sheets_Seguimiento_Suba="google-sheet-id-for-suba-seguimiento"
Sheets_ECO="google-sheet-id-for-ecolombia-seguimiento"
Data_suba_empleabilidad="google-sheet-id-for-suba-empleabilidad"
Sheets_Satisfaccion_Suba="google-sheet-id-for-suba-satisfaccion"
Data_looker_suba="google-sheet-id-for-suba-looker-data"
BQ_Caracterizacion="your-bigquery-dataset-id.your-bigquery-table-caracterizacion"
BQ_Empleabilidad="your-bigquery-dataset-id.your-bigquery-table-empleabilidad"
BQ_Satisfaccion="your-bigquery-dataset-id.your-bigquery-table-satisfaccion"
BQ_Seguimiento="your-bigquery-dataset-id.your-bigquery-table-seguimiento"
```

### 4.4 Autenticación de Google Cloud

Este proyecto utiliza una cuenta de servicio de Google Cloud para autenticarse con BigQuery y Google Sheets.

1.  **Crear una Cuenta de Servicio**: En su proyecto de Google Cloud, cree una cuenta de servicio.
2.  **Asignar Roles**: Asigne los roles necesarios a la cuenta de servicio:
    *   `Editor de datos de BigQuery` (o `Propietario de datos de BigQuery`) para escribir en BigQuery.
    *   `Lector de datos de BigQuery` para leer de BigQuery (para `Append_DATA_BQ.py` y `Limpieza_*.py`).
    *   `Editor` (o `Propietario`) para Google Sheets y Google Drive (para `gspread` y acceso a hojas).
3.  **Generar Clave JSON**: Genere una clave JSON para la cuenta de servicio.
4.  **Guardar Archivo**: Renombre el archivo JSON descargado a `credenciales.json` y colóquelo en la raíz del repositorio. **Este archivo debe ser tratado como sensible y no debe ser versionado.**

---

## 5. Lógica Principal y Pipeline

El proyecto se compone de varios scripts Python, cada uno con una función específica dentro del pipeline de datos.

### 5.1 Scripts de Ingestión de Datos (Upload)

Los scripts como `CONVOCATORIA_ECOLOMBIA_2026.py`, `Caracterizacion_*.py`, `Empleabilidad_*.py`, `Satisfaccion_*.py`, `UnificadoFormacion_*.py` y `Upload_*.py` son los encargados de la ingesta de datos.

**Lógica Común:**

1.  **Carga de Configuración**: Utilizan `python-dotenv` para cargar las variables de entorno (`PROJECT_ID`, `DATASET_ID`, `TABLE_ID`, `Sheets_ID`).
2.  **Autenticación**: Establecen conexión con Google Sheets (`gspread`) y Google BigQuery (`google-cloud-bigquery`) usando `credenciales.json`.
3.  **Extracción**: Leen datos de una hoja de cálculo específica de Google Sheets.
4.  **Pre-procesamiento de Headers**: Manejan casos donde los encabezados pueden estar en filas diferentes a la primera o contener celdas vacías.
5.  **Limpieza y Transformación (`pandas`)**:
    *   Eliminación de filas y columnas completamente vacías.
    *   Reemplazo de cadenas vacías o espacios en blanco por `None`/`NaN`.
    *   Eliminación de filas con valores nulos en columnas clave (e.g., `Número de Documento`).
    *   **Normalización de Nombres de Columnas**: Proceso robusto para estandarizar los nombres de las columnas:
        *   Convertir a minúsculas.
        *   Reemplazar espacios por guiones bajos.
        *   Eliminar caracteres especiales y saltos de línea.
        *   Normalizar caracteres Unicode (acentos, ñ) a ASCII.
        *   Manejar columnas duplicadas.
    *   **Conversión de Tipos de Datos**: Conversión explícita de columnas a tipos numéricos (enteros, flotantes), fechas, o porcentajes según corresponda.
    *   Adición de una columna `proyecto` para identificar la fuente de los datos.
6.  **Validación de Esquema**: Invocan la función `validar_y_comparar` del módulo `validacion_dataframes.py` para asegurar que el DataFrame resultante coincida con el esquema de la tabla de destino en BigQuery.
7.  **Carga a BigQuery**: Utilizan `client_bq.load_table_from_dataframe` con `write_disposition="WRITE_TRUNCATE"` para sobrescribir la tabla de destino en BigQuery, asegurando que los datos siempre estén actualizados. `autodetect=True` permite a BigQuery inferir los tipos de datos de las columnas si no se especifica un esquema explícito.

**Ejemplo de Normalización de Columnas (fragmento de código común):**

```python
DF.columns = (DF.columns
              .str.replace(" ","_")
              .str.normalize('NFKD')
              .str.encode('ascii', errors='ignore')
              .str.decode('utf-8')
              .str.lower()
              .str.replace(r"[\r\n]+", "", regex=True)
              .str.replace(r"[^a-z0-9_#]", "", regex=True)              
              )
```

### 5.2 Módulo de Validación de Esquemas (`validacion_dataframes.py`)

Este módulo es fundamental para la integridad del pipeline. Antes de cada carga a BigQuery, se invoca para comparar el esquema del DataFrame de origen con el esquema de la tabla de destino en BigQuery.

**Lógica:**

1.  Intenta obtener el esquema de la tabla de BigQuery. Si la tabla no existe, el script se detiene.
2.  Compara la cantidad de columnas entre el DataFrame y la tabla de BigQuery.
3.  Compara los nombres de las columnas (después de ordenarlos) para identificar discrepancias.
4.  Si hay diferencias en cantidad o nombres, reporta las columnas faltantes o sobrantes y detiene la ejecución del script de carga, evitando así cargas de datos corruptas o incompletas.

**Valor Agregado:**
Este módulo actúa como un **guardián de la calidad del esquema**, previniendo errores costosos en BigQuery que podrían surgir de cambios inesperados en las hojas de cálculo de origen. Permite **diagnosticar** problemas de estructura de datos en la fuente antes de que afecten el Data Warehouse, **acotando** el riesgo de inconsistencias y **estandarizando** la expectativa de los esquemas.

### 5.3 Script de Apéndice Histórico (`Append_DATA_BQ.py`)

Este script se encarga de mantener un registro histórico de ciertas tablas en BigQuery.

**Lógica:**

1.  Identifica tablas en BigQuery que contienen la palabra "unificado" (excluyendo "formacion" y "append").
2.  Para cada una de estas tablas, lee su contenido en un DataFrame de `pandas`.
3.  Agrega una columna `Fecha_Append` con el formato `YYYY-MM` (mes y año de la ejecución).
4.  Carga el DataFrame resultante en una tabla de BigQuery con el sufijo `_APPEND` (e.g., `SUBA_2026_UnificadoFormacion_APPEND`).
5.  Utiliza `write_disposition="WRITE_APPEND"` para añadir los nuevos registros a la tabla existente, creando un historial de los datos a lo largo del tiempo.

**Valor Agregado:**
Permite **medir** la evolución de los datos a lo largo del tiempo, facilitando análisis de tendencias y comparaciones históricas. Resuelve la necesidad de **periodización** de datos sin modificar las tablas transaccionales principales, y **estandariza** el proceso de captura de instantáneas históricas.

### 5.4 Scripts de Perfilado de Datos (`Limpieza_*.py`)

Los scripts `Limpieza_caracterizacion.py`, `Limpieza_empleabilidad.py`, `Limpieza_satisfaccion.py` y `Limpieza_seguimiento.py` son herramientas de diagnóstico de calidad de datos.

**Lógica:**

1.  Se conectan a BigQuery y consultan una tabla específica (definida por una variable de entorno `BQ_*`).
2.  Cargan los datos en un DataFrame de `pandas`.
3.  Iteran sobre las columnas del DataFrame (excluyendo algunas columnas identificadoras como 'Nombre', 'Documento', etc.).
4.  Para cada columna, imprimen los `value_counts()`, mostrando la distribución de valores únicos y la presencia de nulos.

**Valor Agregado:**
Estos scripts son cruciales para **diagnosticar** problemas de calidad de datos en las tablas de BigQuery. Permiten a los analistas **identificar** rápidamente valores inconsistentes, errores de entrada, patrones inesperados o la prevalencia de valores nulos en columnas críticas. Esto facilita la **optimización** de los procesos de recolección de datos y la **estandarización** de los criterios de calidad.

### 5.5 Orquestador de Ejecución (`trigger.py`)

Este script actúa como el punto de entrada principal para ejecutar el pipeline de ingesta de datos.

**Lógica:**

1.  Escanea el directorio actual para encontrar todos los archivos `.py`.
2.  Mantiene una lista de `archivos_excluidos` (como `trigger.py` mismo, scripts de limpieza, validación, etc.) para no ejecutarlos directamente.
3.  Itera sobre los scripts restantes (`scripts_ejecutables`) y los ejecuta uno por uno utilizando `subprocess.run()`.
4.  Reporta el éxito o fracaso de cada ejecución.
5.  Al final, resume si la actualización fue completa o si hubo fallos, listando los scripts problemáticos.

**Valor Agregado:**
El `trigger.py` **automatiza** la ejecución secuencial de los scripts de ingesta, **simplificando** la operación del pipeline. Permite **resolver** la complejidad de ejecutar múltiples scripts manualmente y **estandariza** el proceso de actualización de datos. Su sistema de reporte de fallos ayuda a **diagnosticar** rápidamente cualquier interrupción en el flujo de datos.

---

## 6. Ejemplos de Salida de Datos

### 6.1 DataFrame Limpio (Previo a BigQuery)

Este es un ejemplo de la estructura de un DataFrame después de la limpieza y normalización por uno de los scripts de ingesta, justo antes de ser cargado a BigQuery.

```
   numero_de_documento  tipo_de_documento     nombre_completo  fecha_nacimiento  edad  genero  ...  estado_actual  fecha_actualizacion  proyecto
0            101234567                CC  Persona Uno Ejemplo        1990-01-15    34  Masculino  ...       Activo           2024-07-20  Ecolombia 2.0
1            209876543                TI  Persona Dos Ejemplo        2005-03-22    19  Femenino  ...       Inactivo           2024-07-19  Ecolombia 2.0
2            304567890                CC  Persona Tres Ejemplo       1988-11-01    35  Masculino  ...       Activo           2024-07-21  Ecolombia 2.0
```

### 6.2 Tabla de Apéndice Histórico en BigQuery

Ejemplo de cómo se vería una tabla en BigQuery después de múltiples ejecuciones del script `Append_DATA_BQ.py`, mostrando la columna `Fecha_Append`.

```sql
-- Ejemplo de tabla: `your-gcp-project-id.your-bigquery-dataset-id.ECOPLUS_2026_CONVOCATORIA_APPEND`

SELECT
    numero_de_documento,
    nombre_completo,
    estado_actual,
    fecha_actualizacion,
    proyecto,
    fecha_append
FROM
    `your-gcp-project-id.your-bigquery-dataset-id.ECOPLUS_2026_CONVOCATORIA_APPEND`
LIMIT 5;
```

| numero_de_documento | nombre_completo     | estado_actual | fecha_actualizacion | proyecto      | fecha_append |
| :------------------ | :------------------ | :------------ | :------------------ | :------------ | :----------- |
| 101234567           | Persona Uno Ejemplo | Activo        | 2024-07-20          | Ecolombia 2.0 | 2024-07      |
| 209876543           | Persona Dos Ejemplo | Inactivo      | 2024-07-19          | Ecolombia 2.0 | 2024-07      |
| 101234567           | Persona Uno Ejemplo | Activo        | 2024-08-20          | Ecolombia 2.0 | 2024-08      |
| 209876543           | Persona Dos Ejemplo | Activo        | 2024-08-19          | Ecolombia 2.0 | 2024-08      |
| 304567890           | Persona Tres Ejemplo| Activo        | 2024-08-21          | Ecolombia 2.0 | 2024-08      |

---

## 7. Valor de Negocio y Capacidades Analíticas

Este pipeline de datos no es solo una solución técnica; es una herramienta estratégica que potencia la inteligencia de negocio y la gestión de proyectos.

### 7.1 Lo que se Muestra

El sistema consolida y presenta una visión unificada de los datos operativos de múltiples programas. Esto incluye:
*   **Datos de Caracterización**: Perfiles demográficos, socioeconómicos y educativos de los participantes.
*   **Datos de Convocatoria y Seguimiento**: Información sobre el proceso de inscripción, estado de los participantes en las fases del programa, y progreso en la formación.
*   **Datos de Empleabilidad**: Seguimiento de postulaciones, remisiones, colocaciones laborales y resultados de inserción.
*   **Datos de Satisfacción**: Feedback de los participantes sobre la calidad de los programas y servicios.
*   **Datos Históricos**: Instantáneas mensuales de la evolución de los indicadores clave.

### 7.2 Lo que Permite Medir

*   **Eficacia de los Programas**: Tasas de conversión en convocatorias, tasas de finalización de formación, tasas de empleabilidad.
*   **Impacto Social**: Número de beneficiarios, perfiles de población atendida, mejora en condiciones de empleabilidad.
*   **Rendimiento Operacional**: Tiempos de ciclo en procesos, eficiencia en la gestión de participantes.
*   **Satisfacción del Usuario**: Net Promoter Score (NPS), niveles de satisfacción con diferentes componentes del programa.
*   **Evolución Temporal**: Tendencias en todos los indicadores a lo largo del tiempo, gracias a los apéndices históricos.

### 7.3 Lo que Permite Diagnosticar

*   **Cuellos de Botella**: Identificar fases del programa con baja retención o conversión.
*   **Problemas de Calidad de Datos**: Detectar inconsistencias, valores atípicos o datos faltantes en las fuentes originales (Google Sheets) a través de los scripts de perfilado y validación.
*   **Ineficiencias en la Recolección de Datos**: Señalar áreas donde la entrada manual de datos es propensa a errores o ambigüedades.
*   **Desviaciones del Plan**: Comparar el progreso real con los objetivos establecidos para cada programa.
*   **Necesidades de Formación**: Identificar brechas en las habilidades de los participantes o en la oferta formativa.

### 7.4 Lo que Permite Resolver

*   **Silos de Información**: Unificar datos dispersos en múltiples hojas de cálculo en un único Data Warehouse.
*   **Inconsistencias de Datos**: Aplicar reglas de limpieza y normalización estandarizadas para asegurar la coherencia.
*   **Retrasos en la Generación de Informes**: Automatizar la ingesta de datos, reduciendo el tiempo de preparación para el análisis.
*   **Decisiones Basadas en Datos Obsoletos**: Proporcionar datos actualizados y validados de forma regular.
*   **Errores Humanos**: Minimizar la intervención manual en el proceso de ETL.

### 7.5 Lo que Permite Acotar

*   **Riesgos de Calidad de Datos**: La validación de esquemas y el perfilado de datos limitan la entrada de información errónea o mal estructurada.
*   **Ambigüedad en las Definiciones**: La normalización de columnas y la estandarización de tipos de datos acotan la interpretación de los campos.
*   **Costos Operacionales**: La automatización reduce la necesidad de recursos humanos dedicados a tareas repetitivas de ETL.
*   **Alcance de los Problemas**: Al diagnosticar rápidamente las fallas, se puede acotar el impacto de los errores en el sistema.

### 7.6 Lo que Permite Optimizar

*   **Procesos de Reporte y Análisis**: Al tener datos limpios y estructurados en BigQuery, la creación de dashboards y análisis ad-hoc es más rápida y fiable.
*   **Asignación de Recursos**: Identificar dónde los recursos (humanos, financieros) están generando el mayor impacto o dónde se necesitan más.
*   **Estrategias de Intervención**: Ajustar los programas de formación o empleabilidad basándose en el rendimiento y la satisfacción de los participantes.
*   **Experiencia del Participante**: Mejorar los puntos de contacto y servicios al entender mejor las necesidades y el feedback de los usuarios.
*   **Eficiencia del Pipeline**: El orquestador `trigger.py` optimiza la ejecución de los scripts, garantizando que el proceso sea robusto y eficiente.

### 7.7 Lo que Permite Estandarizar

*   **Modelos de Datos**: Crear un modelo de datos consistente y unificado en BigQuery para todos los proyectos.
*   **Procesos ETL**: Establecer un pipeline de ingesta, limpieza y carga uniforme para nuevas fuentes de datos.
*   **Métricas e Indicadores**: Definir métricas clave de manera consistente en todos los programas, permitiendo comparaciones significativas.
*   **Calidad de Datos**: Implementar un conjunto de reglas de limpieza y validación que se aplican de forma homogénea.
*   **Documentación y Gobernanza**: Al tener un proceso automatizado y bien definido, se facilita la documentación y la gobernanza de los datos.

### 7.8 Lo que Permite Repensar

*   **Estrategias de Recolección de Datos**: Al identificar problemas recurrentes en las fuentes, se puede repensar cómo se recopila la información desde el origen.
*   **Diseño de Programas**: Utilizar los insights generados para rediseñar o mejorar los programas de formación y empleabilidad, haciéndolos más efectivos y alineados con las necesidades del mercado.
*   **Interacción con los Participantes**: Repensar cómo se interactúa con los beneficiarios basándose en los datos de satisfacción y seguimiento.
*   **Infraestructura de Datos**: Evaluar la necesidad de herramientas adicionales o cambios en la arquitectura para soportar un crecimiento futuro.
*   **Cultura de Datos**: Fomentar una cultura donde las decisiones se basan en datos fiables y accesibles, transformando la organización en una entidad más orientada a datos.============================================================
Repositorio Asociado: Kairos
============================================================
# 📊 Instagram Analytics Dashboard: Semillero Kairós

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-23F18F?style=for-the-badge&logo=plotly&logoColor=white)
![Project Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Este repositorio alberga una solución integral para el análisis y visualización de métricas de rendimiento de Instagram, específicamente diseñada para el "Semillero Kairós". La herramienta procesa datos brutos de insights de Instagram y los presenta a través de un dashboard interactivo, facilitando la toma de decisiones estratégicas en la gestión de contenido y la optimización de la presencia digital.

## 📝 Tabla de Contenidos

1.  [Visión General del Proyecto](#1-visión-general-del-proyecto)
2.  [Valor de Negocio y Preguntas Clave](#2-valor-de-negocio-y-preguntas-clave)
3.  [Arquitectura del Sistema](#3-arquitectura-del-sistema)
4.  [Pipeline de Datos y Payload](#4-pipeline-de-datos-y-payload)
    *   [Origen de Datos](#41-origen-de-datos)
    *   [Procesamiento de Datos (`Instagram_Insight.py`)](#42-procesamiento-de-datos-instagram_insightpy)
    *   [Salida de Datos Procesados](#43-salida-de-datos-procesados)
    *   [Consumo en el Dashboard (`Dashboard.py`)](#44-consumo-en-el-dashboard-dashboardpy)
5.  [Configuración del Entorno](#5-configuración-del-entorno)
    *   [Dependencias a Nivel de Sistema Operativo](#51-dependencias-a-nivel-de-sistema-operativo)
    *   [Dependencias de Python](#52-dependencias-de-python)
    *   [Configuración con Dev Containers](#53-configuración-con-dev-containers)
6.  [Características Clave y Detalles Técnicos del Dashboard](#6-características-clave-y-detalles-técnicos-del-dashboard)
    *   [Preprocesamiento y Caching](#61-preprocesamiento-y-caching)
    *   [Key Performance Indicators (KPIs)](#62-key-performance-indicators-kpis)
    *   [Análisis de Tendencias Temporales](#63-análisis-de-tendencias-temporales)
    *   [Análisis de Dispersión y Outliers](#64-análisis-de-dispersión-y-outliers)
    *   [Rendimiento por Publicación](#65-rendimiento-por-publicación)
    *   [Dispersión Mensual y Efectividad por Tipo de Publicación](#66-dispersión-mensual-y-efectividad-por-tipo-de-publicación)
    *   [Análisis de Prime Time](#67-análisis-de-prime-time)
    *   [Tabla de Datos Interactiva](#68-tabla-de-datos-interactiva)
7.  [Uso](#7-uso)
8.  [Contribuciones](#8-contribuciones)
9.  [Licencia](#9-licencia)

---

## 1. Visión General del Proyecto

Este proyecto proporciona una solución de Business Intelligence para el análisis de datos de Instagram. Consiste en un script de procesamiento de datos que transforma los informes brutos de Instagram en un formato estructurado y un dashboard interactivo, construido con Streamlit y Plotly, que visualiza las métricas clave de rendimiento. El objetivo es ofrecer una visión clara y accionable sobre el impacto del contenido publicado, la interacción de la audiencia y la eficiencia de la estrategia de publicación.

## 2. Valor de Negocio y Preguntas Clave

Este dashboard está diseñado para responder a preguntas críticas de negocio y proporcionar valor estratégico:

*   **¿Qué se muestra?**
    *   Métricas agregadas de rendimiento (Visualizaciones, Alcance, Me gusta, Comentarios, Guardados, Compartidos, Seguimientos).
    *   Tendencias temporales de las métricas clave.
    *   Relación entre diferentes métricas de interacción.
    *   Rendimiento individual de cada publicación.
    *   Distribución de la interacción a lo largo del tiempo (meses, horas).
    *   Efectividad comparativa entre diferentes tipos de publicaciones.

*   **¿Qué permite medir?**
    *   **Engagement Rate:** A través de la relación entre likes, comentarios, guardados, compartidos y el alcance/visualizaciones.
    *   **Alcance y Visibilidad:** Cuántas personas únicas ven el contenido y cuántas veces es visto.
    *   **Longevidad del Contenido:** Cómo el alcance se mantiene o evoluciona con el tiempo desde la publicación.
    *   **Eficacia del Contenido:** Qué tipos de publicaciones generan mayor interacción y conversión.
    *   **Momentos Óptimos de Publicación (Prime Time):** Las horas del día con mayor interacción y alcance.

*   **¿Qué permite diagnosticar?**
    *   **Contenido de Bajo Rendimiento:** Identificar publicaciones con métricas por debajo del promedio.
    *   **Outliers de Interacción:** Detectar publicaciones excepcionalmente exitosas o fallidas.
    *   **Patrones de Descenso/Ascenso:** Observar tendencias en el rendimiento que pueden indicar cambios en la estrategia o en la audiencia.
    *   **Ineficiencias en la Estrategia de Contenido:** Determinar si ciertos tipos de publicaciones no están resonando con la audiencia.

*   **¿Qué permite resolver, acotar, optimizar, estandarizar y repensar?**
    *   **Resolver:** Problemas de baja interacción o alcance al identificar las causas subyacentes (tipo de contenido, hora de publicación, descripción).
    *   **Acotar:** El público objetivo y los temas de contenido más relevantes, enfocando los esfuerzos donde generan mayor impacto.
    *   **Optimizar:** La estrategia de contenido, los horarios de publicación y los formatos de contenido para maximizar el engagement y el alcance.
    *   **Estandarizar:** El proceso de monitoreo y reporte de métricas de Instagram, asegurando una evaluación consistente del rendimiento.
    *   **Repensar:**
        *   **Estrategia de Contenido:** Cuestionar la efectividad de los formatos actuales y explorar nuevos enfoques basados en datos. Por ejemplo, si los Reels tienen una alta efectividad pero bajo alcance, ¿cómo se puede aumentar su visibilidad?
        *   **Calendario Editorial:** Reevaluar los días y horas de publicación para alinearlos con los picos de actividad de la audiencia.
        *   **Narrativa y Llamadas a la Acción:** Analizar qué descripciones y CTAs generan más comentarios o guardados, y replicar esas prácticas.
        *   **Inversión en Contenido:** Justificar la asignación de recursos a la creación de ciertos tipos de contenido basándose en su retorno de interacción.
        *   **Benchmarking Interno:** Establecer puntos de referencia de rendimiento para diferentes tipos de publicaciones y monitorear el progreso a lo largo del tiempo.

En resumen, este proyecto transforma datos brutos en inteligencia accionable, permitiendo a los gestores de contenido tomar decisiones informadas para potenciar la presencia de "Semillero Kairós" en Instagram.

## 3. Arquitectura del Sistema

La arquitectura del proyecto se compone de dos módulos principales que operan en una secuencia lógica:

1.  **Módulo de Extracción y Transformación (ETL): `Instagram_Insight.py`**
    *   **Función:** Este script es responsable de cargar los datos brutos exportados directamente desde Instagram Insights (en formato CSV), realizar una limpieza y transformación inicial, y estructurarlos en un formato optimizado para el análisis.
    *   **Tecnología:** Python con la librería `pandas`.
    *   **Salida:** Genera un archivo CSV (`insight_kairos.csv`) que sirve como fuente de datos limpia para el dashboard.

2.  **Módulo de Visualización y Análisis Interactivo: `Dashboard.py`**
    *   **Función:** Este script consume el archivo `insight_kairos.csv` y construye un dashboard interactivo utilizando Streamlit. Permite a los usuarios explorar las métricas de rendimiento a través de diversos gráficos y filtros, facilitando el análisis de tendencias y la identificación de insights.
    *   **Tecnología:** Python con las librerías `streamlit`, `pandas`, `plotly.express`, `plotly.graph_objects` y `textwrap`.
    *   **Interfaz:** Una aplicación web interactiva accesible a través del navegador.

**Flujo de Datos:**

`Datos Brutos de Instagram (CSV)` --(`Instagram_Insight.py`)--> `insight_kairos.csv` --(`Dashboard.py`)--> `Dashboard Interactivo`

## 4. Pipeline de Datos y Payload

### 4.1. Origen de Datos

El pipeline se inicia con un archivo CSV exportado directamente desde la sección de Instagram Insights. Este archivo contiene métricas detalladas para las publicaciones de una cuenta específica durante un período determinado.

**Ejemplo de Nombre de Archivo de Origen:** `Mar-26-2025_Mar-26-2026_949104527769166.csv`

### 4.2. Procesamiento de Datos (`Instagram_Insight.py`)

El script `Instagram_Insight.py` ejecuta las siguientes transformaciones:

1.  **Carga de Datos:** Lee el archivo CSV de origen.
2.  **Selección de Columnas:** Filtra y selecciona un subconjunto específico de columnas relevantes para el análisis, descartando información redundante o no necesaria.
    ```python
    headers_necesarios = ['Nombre de la cuenta', 'Descripción', 
                          'Hora de publicación', 'Enlace permanente','Tipo de publicación', 'Visualizaciones', 
                          'Alcance', 'Me gusta', 'Veces que se compartió','Seguimientos', 'Comentarios', 'Veces que se guardó']
    analyitics_kairos = datos[headers_necesarios]
    ```
3.  **Renombrado de Columnas:** Estandariza los nombres de algunas columnas para mayor claridad y consistencia.
    ```python
    analyitics_kairos = analyitics_kairos.rename(columns={'Identificador de la publicación': 'ID Publicación', 
                                                          'Identificador de la cuenta': 'ID Cuenta', 
                                                          'Hora de publicación': 'Fecha Post'})
    ```
4.  **Conversión de Fechas y Horas:** Transforma la columna `Fecha Post` a formato datetime, extrayendo la fecha y la hora en columnas separadas para facilitar el análisis temporal.
    ```python
    analyitics_kairos['Fecha Post'] = pd.to_datetime(analyitics_kairos['Fecha Post'], errors='coerce')
    analyitics_kairos['Fecha'] = analyitics_kairos['Fecha Post'].dt.date
    analyitics_kairos['Hora Post'] = analyitics_kairos['Fecha Post'].dt.time
    analyitics_kairos.drop(columns=['Fecha Post'], inplace=True)
    ```
5.  **Manejo de Valores Nulos:** Rellena los valores nulos en la columna `Seguimientos` con cero, asumiendo que un valor nulo implica la ausencia de nuevos seguidores.
    ```python
    analyitics_kairos['Seguimientos'] = analyitics_kairos['Seguimientos'].fillna(0)
    ```
6.  **Limpieza de Descripción:** Extrae solo la primera línea de la columna `Descripción`, ya que las descripciones de Instagram a menudo contienen múltiples líneas que pueden ser excesivas para la visualización directa.
    ```python
    analyitics_kairos['Descripción'] = (analyitics_kairos['Descripción'].str.split('\n').str[0])
    ```
7.  **Exportación:** Guarda el DataFrame procesado en un nuevo archivo CSV.
    ```python
    analyitics_kairos.to_csv("insight_kairos.csv")
    ```

### 4.3. Salida de Datos Procesados

El script `Instagram_Insight.py` genera el archivo `insight_kairos.csv`. A continuación, se muestra un ejemplo de la estructura de este archivo:

```csv
"","Nombre de la cuenta","Descripción","Enlace permanente","Tipo de publicación","Visualizaciones","Alcance","Me gusta","Veces que se compartió","Seguimientos","Comentarios","Veces que se guardó","Fecha","Hora Post"
0,"Usuario 1","Descripción de la publicación 1","https://instagram.com/p/ABCDEF","IMAGEN",1500,1200,80,5,10,3,12,"2023-01-15","14:30:00"
1,"Usuario 1","Descripción de la publicación 2","https://instagram.com/p/GHIJKL","VIDEO",2500,2000,150,12,25,8,20,"2023-01-16","10:00:00"
2,"Usuario 1","Descripción de la publicación 3","https://instagram.com/p/MNOPQR","CARRUSEL",3000,2500,200,18,30,15,25,"2023-01-17","18:45:00"
3,"Usuario 1","Descripción de la publicación 4","https://instagram.com/p/STUVWX","REEL",4000,3500,300,25,40,20,35,"2023-01-18","09:15:00"
```

### 4.4. Consumo en el Dashboard (`Dashboard.py`)

El dashboard carga el archivo `insight_kairos.csv` y realiza transformaciones adicionales para la visualización:

1.  **Carga y Caching:** Utiliza `@st.cache_data` para cargar eficientemente el CSV y evitar recargas innecesarias.
2.  **Limpieza de Columna `Unnamed: 0`:** Elimina la columna de índice generada por `to_csv`.
3.  **Conversión a Datetime y Extracción de Componentes:** Convierte la columna `Fecha` a tipo datetime y extrae el año (`Año`), el mes en español (`Mes_Esp`) y la hora (`Hora`) para filtros y agrupaciones.
4.  **Generación de Descripciones para Hover y Ejes:** Crea versiones truncadas y formateadas de la descripción para mejorar la legibilidad en tooltips y ejes de gráficos.
5.  **Cálculo de `Días activo`:** Determina la antigüedad de cada publicación desde la fecha actual.

Estas transformaciones preparan los datos para ser consumidos por los diversos componentes visuales del dashboard.

## 5. Configuración del Entorno

Para ejecutar este proyecto, se recomienda utilizar un entorno de desarrollo aislado. La configuración proporcionada con `devcontainer.json` simplifica este proceso.

### 5.1. Dependencias a Nivel de Sistema Operativo

El archivo `.devcontainer/devcontainer.json` incluye una sección `updateContentCommand` que verifica la existencia de un archivo `packages.txt`. Si este archivo existe, se utilizará para instalar dependencias a nivel de sistema operativo (ej. `apt install`). Para este proyecto específico, no se requieren dependencias de SO adicionales más allá de las que ya incluye la imagen base de Python.

### 5.2. Dependencias de Python

Las librerías de Python necesarias se gestionan a través de un archivo `requirements.txt` (implícito en el `devcontainer.json` aunque no proporcionado directamente en el código). Las principales librerías son:

*   `pandas`: Para manipulación y análisis de datos.
*   `streamlit`: Para la construcción del dashboard interactivo.
*   `plotly`: Para la generación de gráficos interactivos y estéticos.
*   `textwrap`: Utilizado para formatear texto en las descripciones de las publicaciones.

Para instalar estas dependencias manualmente (fuera de un dev container):

```bash
pip install pandas streamlit plotly textwrap
```

### 5.3. Configuración con Dev Containers

El proyecto está configurado para ser ejecutado fácilmente en un Dev Container (por ejemplo, con VS Code Dev Containers o GitHub Codespaces).

El archivo `.devcontainer/devcontainer.json` define:

*   **Imagen Base:** `mcr.microsoft.com/devcontainers/python:1-3.11-bookworm` (Python 3.11 en Debian Bookworm).
*   **Extensiones VS Code:** `ms-python.python`, `ms-python.vscode-pylance`.
*   **Comandos de Inicialización:**
    *   `updateContentCommand`: Instala dependencias de `packages.txt` (si existe) y `requirements.txt` (si existe), y `streamlit`.
    *   `postAttachCommand`: Inicia automáticamente el dashboard de Streamlit al adjuntar al contenedor.
        ```json
        "postAttachCommand": {
          "server": "streamlit run Dashboard.py --server.enableCORS false --server.enableXsrfProtection false"
        }
        ```
*   **Configuración de Puertos:** Redirecciona el puerto 8501 (puerto por defecto de Streamlit) y lo abre automáticamente en una vista previa.

**Para iniciar el entorno con Dev Containers:**

1.  Asegúrate de tener Docker instalado y funcionando.
2.  Abre el proyecto en VS Code.
3.  VS Code detectará el archivo `.devcontainer/devcontainer.json` y te preguntará si deseas "Reopen in Container". Acepta.
4.  El contenedor se construirá y el dashboard se iniciará automáticamente, abriendo una vista previa en tu navegador o en VS Code.

## 6. Características Clave y Detalles Técnicos del Dashboard

El `Dashboard.py` es el corazón de la visualización, utilizando Streamlit para la interfaz y Plotly para los gráficos interactivos.

### 6.1. Preprocesamiento y Caching

La función `load()` se encarga de cargar y preprocesar los datos. La directiva `@st.cache_data` es crucial para optimizar el rendimiento, ya que almacena en caché el DataFrame resultante. Esto evita que la carga y el procesamiento de datos se repitan cada vez que el usuario interactúa con los filtros, mejorando significativamente la fluidez del dashboard.

```python
@st.cache_data
def load():
    df = pd.read_csv(PATH)
    # ... (transformaciones de fecha, hora, descripción, etc.)
    return df

df = load()
base_df = df.copy() # Para cálculos de porcentaje sobre el total histórico
```

### 6.2. Key Performance Indicators (KPIs)

Se presentan cuatro KPIs principales (Visualizaciones, Alcance, Me gusta, Comentarios) en tarjetas personalizadas con CSS. Cada KPI muestra el valor total filtrado y su porcentaje respecto al total histórico de la base de datos, proporcionando un contexto inmediato del rendimiento.

```python
# Ejemplo de función KPI
def kpi(col, name, field):
    val = df[field].sum()
    total = base_df[field].sum()
    percent = (val / total * 100) if total != 0 else 0

    col.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">{name}</div>
        <div class="kpi-value">{int(val):,}</div>
        <div class="kpi-percent">{percent:.1f}% del histórico global</div>
    </div>
    """, unsafe_allow_html=True)

kpi(c1, "Visualizaciones", "Visualizaciones")
# ... otros KPIs
```
La implementación de CSS personalizado (`st.markdown("""<style>...""")`) permite un diseño estético y coherente para las tarjetas KPI, mejorando la experiencia visual del usuario.

### 6.3. Análisis de Tendencias Temporales

Un gráfico de líneas interactivo muestra la evolución de las Visualizaciones, Alcance y Me gusta a lo largo del tiempo. Utiliza `plotly.graph_objects.Scatter` con `mode="lines+markers+text"` para resaltar los puntos de datos y sus valores, facilitando la identificación de picos y valles de rendimiento.

```python
fig_evol = go.Figure()
palette = ["#3b82f6", "#a855f7", "#ec4899"] 
metrics = ["Visualizaciones", "Alcance", "Me gusta"]

for i, m in enumerate(metrics):
    fig_evol.add_trace(go.Scatter(
        x=df_time["Fecha"], y=df_time[m], name=m,
        mode="lines+markers+text", 
        text=[f"<b>{int(v)}</b>" if v > 0 else "" for v in df_time[m]],
        textposition="top center",
        textfont=dict(size=12, color=palette[i]),
        line=dict(shape="spline", width=4, color=palette[i]),
        marker=dict(size=8, line=dict(width=2, color="white"))
    ))
fig_evol.update_layout(template="plotly_dark", height=450, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0))
```
El uso de `shape="spline"` en las líneas suaviza la visualización de las tendencias, mientras que la leyenda horizontal y la alineación a la izquierda optimizan el espacio.

### 6.4. Análisis de Dispersión y Outliers

Se utilizan gráficos de dispersión (`plotly.express.scatter`) para visualizar la relación entre métricas como Alcance, Me gusta, Comentarios y Visualizaciones. La inclusión de `trendline="ols"` (Ordinary Least Squares) permite identificar rápidamente correlaciones y detectar publicaciones que se desvían significativamente de la tendencia (posibles outliers de alto o bajo rendimiento).

```python
fig1 = px.scatter(
    df, x="Alcance", y="Me gusta", size="Visualizaciones", color="Me gusta",
    color_continuous_scale="Plasma", hover_name="Desc_Hover", trendline="ols",
    hover_data={"Desc_Hover": False, "Visualizaciones": True, "Me gusta": True},
    template="plotly_dark"
)
```
Un gráfico adicional de dispersión analiza la "Longevidad" del contenido, correlacionando `Días activo` con `Alcance`, lo que permite entender cómo el tiempo afecta la visibilidad de las publicaciones.

### 6.5. Rendimiento por Publicación

Un gráfico de barras horizontales (`plotly.express.bar`) permite comparar el rendimiento de las publicaciones individuales según una métrica seleccionada (Alcance, Me gusta, Comentarios, Visualizaciones). La capacidad de seleccionar la métrica a evaluar (`st.selectbox`) añade interactividad y flexibilidad al análisis.

```python
metric = st.selectbox("Métrica a evaluar", ["Alcance", "Me gusta", "Comentarios", "Visualizaciones"], index=0)
fig_bar = px.bar(
    df.sort_values(metric, ascending=True).tail(12), # Muestra las 12 mejores
    x=metric, y="Desc_Eje", orientation="h", color=metric,
    color_continuous_scale=["#1e40af", "#3b82f6", "#5eead4"], 
    text=metric,
    template="plotly_dark"
)
```
La visualización de las 12 publicaciones con mejor rendimiento (`.tail(12)`) es una estrategia efectiva para destacar el contenido más exitoso.

### 6.6. Dispersión Mensual y Efectividad por Tipo de Publicación

*   **Boxplot de Visualizaciones por Mes:** Un gráfico de caja (`plotly.express.box`) muestra la distribución de las visualizaciones por mes. Esto ayuda a identificar la variabilidad y los valores atípicos en el rendimiento mensual, lo que puede indicar estacionalidad o eventos específicos.
    ```python
    fig_box = px.box(
        df, x="Mes_Esp", y="Visualizaciones", color="Mes_Esp",
        color_discrete_sequence=px.colors.sequential.Plasma,
        template="plotly_dark", category_orders={"Mes_Esp": meses_presentes}
    )
    ```
*   **Efectividad por Tipo de Publicación:** Un gráfico combinado de barras y líneas (`plotly.subplots.make_subplots`) compara el alcance promedio de diferentes tipos de publicaciones con su porcentaje de efectividad (likes + comentarios / alcance). Esto es fundamental para optimizar la estrategia de contenido, identificando qué formatos generan mayor interacción.
    ```python
    df_tipo["Efectividad %"] = ((df_tipo["Me gusta"] + df_tipo["Comentarios"]) / df_tipo["Alcance"]) * 100
    fig_tipo = make_subplots(specs=[[{"secondary_y": True}]])
    # ... (adición de trazas de barras y scatter)
    ```
    La utilización de un eje Y secundario permite comparar métricas con escalas muy diferentes (Alcance vs. Porcentaje de Efectividad) en un solo gráfico.

### 6.7. Análisis de Prime Time

Un gráfico combinado (`plotly.subplots.make_subplots`) analiza las interacciones (Guardados, Compartidos) y porcentajes clave (% Alcance Total, % Conversión Likes/Vistas) por hora de publicación. Esto es crucial para identificar los "prime times" donde la audiencia está más activa y receptiva.

```python
fig_hora = make_subplots(specs=[[{"secondary_y": True}]])
# ... (adición de trazas de barras para Guardados/Compartidos y scatter para porcentajes)
fig_hora.update_yaxes(title_text="Total Interacciones", secondary_y=False)
fig_hora.update_yaxes(title_text="Porcentaje (%)", secondary_y=True)
```
Este gráfico utiliza un `barmode="stack"` para los guardados y compartidos, y líneas para los porcentajes, ofreciendo una visión completa del comportamiento horario.

### 6.8. Tabla de Datos Interactiva

Finalmente, se presenta una tabla interactiva del DataFrame procesado, permitiendo a los usuarios explorar los datos subyacentes. La tabla se estiliza con un `background_gradient` en las columnas de métricas para resaltar visualmente los valores más altos, facilitando la identificación rápida de publicaciones destacadas.

```python
df_styled = df_mostrar.style.background_gradient(
    cmap='PuRd', subset=cols_existentes
).format(precision=0, subset=cols_existentes)
st.dataframe(df_styled, use_container_width=True, height=400)
```
El uso de `st.dataframe` con estilizado de Pandas es una forma efectiva de presentar datos tabulares de manera atractiva y funcional.

## 7. Uso

Para utilizar el dashboard:

1.  **Preparar los datos:** Asegúrate de tener el archivo `insight_kairos.csv` en la raíz del proyecto. Si no lo tienes, ejecuta el script `Instagram_Insight.py` con tu archivo de datos brutos de Instagram Insights (renombrado a `Mar-26-2025_Mar-26-2026_949104527769166.csv` o ajustando la ruta en el script).
    ```bash
    python Instagram_Insight.py
    ```
2.  **Ejecutar el dashboard:**
    *   **Con Dev Containers (recomendado):** Sigue los pasos en la sección [Configuración con Dev Containers](#53-configuración-con-dev-containers). El dashboard se iniciará automáticamente.
    *   **Manualmente:** Abre tu terminal en la raíz del proyecto y ejecuta:
        ```bash
        streamlit run Dashboard.py
        ```
        Esto abrirá el dashboard en tu navegador web, generalmente en `http://localhost:8501`.

Una vez abierto, puedes interactuar con los filtros de la barra lateral para segmentar los datos por año, rango de fechas, mes, tipo de publicación y descripción, y observar cómo los gráficos se actualizan dinámicamente.

## 8. Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor, sigue estos pasos:

1.  Haz un fork del repositorio.
2.  Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3.  Realiza tus cambios y commitea (`git commit -am 'Añadir nueva funcionalidad'`).
4.  Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5.  Abre un Pull Request.

## 9. Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.============================================================
Repositorio Asociado: Vacantes-J-venes-a-la-E
============================================================
# Automated Job Market Intelligence Pipeline (elempleo.com)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/documentation/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/docs/)
[![Google Sheets API](https://img.shields.io/badge/Google%20Sheets%20API-4285F4?style=for-the-badge&logo=google-sheets&logoColor=white)](https://developers.google.com/sheets/api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green.svg?style=for-the-badge)](https://github.com/)

Este repositorio contiene un pipeline automatizado de extracción, transformación, enriquecimiento y carga de datos (ETL) diseñado para recopilar inteligencia de mercado laboral desde el portal de empleo `elempleo.com`. El sistema extrae de forma programática ofertas de trabajo bajo criterios específicos, realiza un raspado profundo de segundo nivel para enriquecer los registros, filtra la información mediante expresiones regulares y sincroniza los resultados en tiempo real con una hoja de cálculo en Google Sheets y un archivo CSV local.

---

## Índice

1. [Valor de Negocio y Objetivos Analíticos](#1-valor-de-negocio-y-objetivos-analíticos)
2. [Arquitectura del Sistema y Flujo de Datos](#2-arquitectura-del-sistema-y-flujo-de-datos)
3. [Requisitos del Sistema y Dependencias](#3-requisitos-del-sistema-y-dependencias)
4. [Configuración e Instalación](#4-configuración-e-instalación)
5. [Análisis Detallado del Código](#5-análisis-detallado-del-coódigo)
6. [Estructura de Datos de Salida (Payload)](#6-estructura-de-datos-de-salida-payload)
7. [Estrategia de Optimización y Robustez](#7-estrategia-de-optimización-y-robustez)

---

## 1. Valor de Negocio y Objetivos Analíticos

Este desarrollo resuelve la necesidad de monitorear de forma sistemática el mercado laboral para perfiles técnicos y operativos en Bogotá, eliminando la recolección manual de datos y proporcionando una base de datos estructurada para la toma de decisiones estratégicas.

### Impacto y Capacidades de Diagnóstico

*   **Medición de la Oferta Salarial Real**: Al filtrar ofertas con "Salario confidencial", el pipeline permite calcular promedios, medianas y desviaciones estándar de los salarios reales ofrecidos en el mercado para los sectores de "Mercadeo y Ventas" y "Auxiliar Administrativo".
*   **Diagnóstico de Requisitos Educativos**: Permite diagnosticar si las empresas están sobreexigiendo requisitos académicos para roles operativos, correlacionando el nivel educativo exigido ("técnico", "media", "bachiller") con la compensación económica ofrecida.
*   **Resolución de Asimetría de Información**: Proporciona a las áreas de recursos humanos o analistas de políticas públicas un panorama claro y actualizado de la competitividad de sus vacantes frente al mercado activo.
*   **Acotación de Perfiles No Viables**: Excluye automáticamente contratos de aprendizaje y salarios no declarados, asegurando que el análisis se concentre únicamente en ofertas de empleo formal y directo.
*   **Optimización del Sourcing**: Automatiza la detección de nuevas ofertas ordenadas por fecha de publicación, permitiendo a los reclutadores o buscadores de empleo reaccionar en menos de 24 horas ante nuevas publicaciones.
*   **Estandarización de Datos No Estructurados**: Transforma descripciones de texto libre y metadatos embebidos en el DOM (como variables de Google Analytics 4) en un esquema de datos relacional y limpio.
*   **Repensar la Captura de Datos**: En lugar de depender de APIs costosas o limitadas, el script aprovecha los payloads de telemetría interna (`data-ga4-offerdata`) que la misma plataforma utiliza, garantizando la obtención de datos estructurados con un mínimo de llamadas al DOM.

---

## 2. Arquitectura del Sistema y Flujo de Datos

El pipeline sigue una arquitectura lineal de cinco etapas (Extracción, Filtrado Inicial, Enriquecimiento, Filtrado Avanzado y Carga):

```
+-----------------------------------------------------------------------+
|                           1. EXTRACCIÓN                               |
| - Inicializa Selenium (Headless Chrome)                               |
| - Aplica filtros de salario vía URL                                   |
| - Extrae tarjetas de vacantes y parsea JSON de GA4 del DOM            |
+----------------------------------+------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                        2. FILTRADO INICIAL                            |
| - Remueve "Contrato de aprendizaje"                                   |
| - Remueve "Salario confidencial"                                      |
| - Elimina registros duplicados                                        |
+----------------------------------+------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                        3. ENRIQUECIMIENTO                             |
| - Navega de forma iterativa a la URL de cada vacante                  |
| - Extrae: Descripción detallada, Nivel Educativo y Fecha Publicación  |
| - Parsea fechas relativas/locales usando 'dateparser'                 |
+----------------------------------+------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                        4. FILTRADO AVANZADO                           |
| - Filtra por nivel educativo usando Regex (técnico, media, bachiller) |
| - Ordena cronológicamente de forma descendente                        |
+----------------------------------+------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                            5. CARGA (LPT)                             |
| - Exporta dataset enriquecido a CSV local                             |
| - Autentica con Google Drive & Sheets API vía Service Account         |
| - Limpia y actualiza la hoja de cálculo "VACANTES"                    |
+-----------------------------------------------------------------------+
```

---

## 3. Requisitos del Sistema y Dependencias

Para ejecutar este pipeline, el entorno de ejecución debe contar con dependencias tanto a nivel de sistema operativo como a nivel de lenguaje de programación.

### Requisitos a Nivel de Sistema Operativo

1.  **Google Chrome Browser**: Debe estar instalado en el sistema operativo. En entornos Linux (servidores/CI-CD), se requiere la instalación de Chrome y sus dependencias de renderizado de fuentes.
2.  **Google Chrome Driver**: Requerido para que Selenium interactúe con el navegador. Debe corresponder exactamente con la versión de Google Chrome instalada. *Nota: Las versiones recientes de Selenium gestionan esto automáticamente mediante Selenium Manager, pero se recomienda asegurar la disponibilidad del binario en el PATH en entornos restringidos.*
3.  **Certificados CA**: Necesarios para establecer conexiones seguras HTTPS con Google APIs y el portal de empleo.

### Dependencias de Python

Las librerías requeridas están especificadas en el archivo `requirements.txt`:

```text
selenium
pandas
python-dotenv
gspread
oauth2client
dateparser
```

---

## 4. Configuración e Instalación

### Paso 1: Clonar el repositorio y preparar el entorno virtual

```bash
git clone https://github.com/tu-usuario/job-market-intelligence-pipeline.git
cd job-market-intelligence-pipeline
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Paso 2: Configurar las Credenciales de Google Cloud Platform (GCP)

1.  Vaya a la consola de Google Cloud.
2.  Habilite la **Google Drive API** y la **Google Sheets API**.
3.  Cree una **Cuenta de Servicio (Service Account)** y descargue la clave privada en formato JSON.
4.  Guarde este archivo en la raíz del proyecto con el nombre `gcp-credentials.json` (asegúrese de que esté incluido en su `.gitignore`).
5.  Comparta su hoja de cálculo de Google Sheets con el correo electrónico de la cuenta de servicio generada (ej. `mi-servicio@applied-plexus.iam.gserviceaccount.com`) otorgándole permisos de **Editor**.

### Paso 3: Configurar las Variables de Entorno

Cree un archivo `.env` en la raíz del proyecto con la siguiente estructura:

```env
Sheets_JAE=ID_DE_TU_HOJA_DE_CALCULO_GOOGLE_SHEETS
```

*Nota: El ID de la hoja de cálculo se encuentra en la URL de la misma: `https://docs.google.com/spreadsheets/d/ID_DE_TU_HOJA_DE_CALCULO/edit`*

---

## 5. Análisis Detallado del Código

### 1. Extracción de Vacantes y Consumo de Telemetría Interna

La función `extraccion_vacantes` utiliza Selenium en modo headless para evitar la sobrecarga de renderizado de interfaz gráfica. En lugar de parsear cada elemento visual de la tarjeta de empleo, el script accede al atributo `data-ga4-offerdata`. Este atributo contiene un objeto JSON estructurado con los metadatos de la oferta, lo que garantiza una extracción limpia y previene fallos por cambios menores en el diseño HTML (CSS).

```python
# Fragmento clave de extracción de metadatos estructurados
json_data = vacante.get_attribute("data-ga4-offerdata")
if json_data:
    datos_por_oferta = json.loads(json_data)
    datos_totales.append({
        "Vacante": datos_por_oferta.get("title", ""),
        "Empresa": datos_por_oferta.get("company", "Empresa Confidencial"),
        "Ubicación": datos_por_oferta.get("location", ""),
        "Cargo_Equivalente": datos_por_oferta.get("equivalentPositions", ""),
        "Tipo_Contrato": tipo_contrato,
        "Salario": datos_por_oferta.get("salary", "Sin información salarial"),
        "Link_Oferta": link_info_vacante,                    
    })
```

### 2. Enriquecimiento de Datos y Normalización de Fechas

Una vez consolidada la lista de URLs de vacantes válidas, el pipeline realiza una navegación profunda a cada enlace para extraer la descripción completa, el nivel educativo y la fecha de publicación. 

El uso de `dateparser` es crítico aquí, ya que las fechas de publicación en portales de empleo suelen expresarse en lenguaje natural relativo (ej. "Publicado hace 2 días", "Publicado ayer"). `dateparser` normaliza estas cadenas a objetos de tipo `datetime` estándar, permitiendo su posterior ordenamiento cronológico.

```python
# Extracción de fecha y parseo de lenguaje natural a formato ISO
Fecha_publicacion_vacante = Wait_10_Sec.until(
    EC.presence_of_element_located(
        (By.XPATH, '//p[contains(@class, "publish-date-info")]')
    )
)
# Remueve ruido de texto y parsea la fecha
Fecha_publicacion = dateparser.parse(
    Fecha_publicacion_vacante.text.replace("Publicado", "")
).strftime('%Y-%m-%d')
```

### 3. Filtrado Avanzado por Expresiones Regulares

Para acotar el universo de datos a perfiles técnicos y operativos, se aplica un filtro basado en expresiones regulares sobre la columna `Nivel`. Esto descarta perfiles profesionales, especializados o tecnólogos si no cumplen con el criterio de búsqueda.

```python
# Filtrado por niveles educativos específicos (Técnico, Educación Media, Bachillerato)
CSV = CSV[CSV['Nivel'].str.contains(r't[eé]cnic[oa]|media|bachi', case=False, na=False)]
```

### 4. Sincronización con Google Sheets API

La integración con Google Sheets se realiza mediante `gspread`. Se limpia la hoja de destino por completo para evitar colisiones de datos antiguos y se realiza una actualización masiva en una sola llamada de red (`update`), optimizando la cuota de peticiones de la API de Google.

```python
# Preparación de matriz de datos (incluyendo cabeceras) para actualización masiva
CSV_TO_SHEETS = [Datos_Vacantes_Seleccionadas.columns.values.tolist()] + Datos_Vacantes_Seleccionadas.values.tolist()

# Limpieza y escritura atómica
Hoja_de_Trabajo.clear()
Hoja_de_Trabajo.update(range_name="A1", values=CSV_TO_SHEETS)
```

---

## 6. Estructura de Datos de Salida (Payload)

El pipeline genera un archivo estructurado (tanto en formato CSV como en la hoja de cálculo de Google) que cumple con el siguiente esquema de datos:

### Ejemplo de Salida (JSON Representation)

```json
[
  {
    "Vacante": "Auxiliar de Operaciones y Mercadeo",
    "Empresa": "Empresa de Logística y Distribución S.A.S.",
    "Ubicación": "Bogotá",
    "Cargo_Equivalente": "Auxiliar de mercadeo, Auxiliar administrativo",
    "Tipo_Contrato": "Término Indefinido",
    "Salario": "1500000",
    "Link_Oferta": "https://www.elempleo.com/co/ofertas-empleo/auxiliar-de-operaciones-y-mercadeo/1882746190",
    "Programa_Asociado": "Mercadeo y Ventas",
    "Descripción": "Se requiere bachiller o técnico con experiencia mínima de 1 año en procesos de apoyo logístico, inventarios, atención al cliente y soporte administrativo en puntos de venta...",
    "Nivel": "Técnico",
    "Fecha Publicación": "2023-10-27"
  },
  {
    "Vacante": "Auxiliar de Archivo y Correspondencia",
    "Empresa": "Servicios Temporales Empresa 1",
    "Ubicación": "Bogotá",
    "Cargo_Equivalente": "Auxiliar de oficina, Auxiliar de archivo",
    "Tipo_Contrato": "Obra o Labor",
    "Salario": "1300000",
    "Link_Oferta": "https://www.elempleo.com/co/ofertas-empleo/auxiliar-de-archivo-y-correspondencia/1882745540",
    "Programa_Asociado": "Auxiliar Administrativo",
    "Descripción": "Importante compañía requiere bachiller con experiencia en gestión documental, radicación de correspondencia y atención de conmutador...",
    "Nivel": "Educación Media / Bachillerato",
    "Fecha Publicación": "2023-10-26"
  }
]
```

---

## 7. Estrategia de Optimización y Robustez

*   **Headless Execution**: El uso de `--headless` reduce drásticamente el consumo de memoria RAM y CPU en el servidor de ejecución, permitiendo correr este script en instancias de cómputo pequeñas (como AWS EC2 t2.micro o Google Cloud Compute Engine f1-micro).
*   **Explicit Waits**: En lugar de utilizar pausas estáticas (`time.sleep`), el script implementa `WebDriverWait` combinado con `expected_conditions`. Esto asegura que el script continúe la ejecución tan pronto como el elemento DOM esté disponible, optimizando el tiempo total de ejecución del pipeline.
*   **Manejo de Excepciones Granular**: Cada bloque crítico (extracción de contrato, parseo de JSON, navegación profunda) está envuelto en estructuras `try-except`. Si una vacante específica presenta una estructura corrupta o un error de carga, el pipeline la ignora y continúa con el procesamiento de las demás, garantizando la resiliencia del proceso global.
*   **Filtrado de Ruido en Origen**: Al aplicar filtros de salario directamente en los parámetros de la URL (`Flitro_salarios`), se reduce el volumen de datos innecesarios transferidos por la red, optimizando el ancho de banda y el procesamiento local de Pandas.