# Repository Documentation Automation with LLMs

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub%20API-Integration-informational?style=flat-square&logo=github&logoColor=white)
![Groq API](https://img.shields.io/badge/Groq%20API-Llama-green?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyQzIgMTcuNTIgNi40OCAyMiAxMiAyMkMxNy41MiAyMiAyMiAxNy41MiAyMiAxMkMyMiA2LjQ4IDE3LjUyIDIgMTIgMlpNMTIgNEwxNiA4SDhMMTIgNFpNMTggMTJMMTQuNSAxNS41TDE4IDE5VjEyWk02IDEyVjE5TDEwLjUgMTUuNUw2IDEyWk0xMiAxNkw4IDE5SDE2TDEyIDE2WiIgZmlsbD0id2hpdGUiLz4KPC9zdmc+&logoColor=white)
![Google Gemini API](https://img.shields.io/badge/Google%20Gemini%20API-AI%20Platform-orange?style=flat-square&logo=google&logoColor=white)
![Project Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-Unspecified-lightgrey?style=flat-square)

This repository hosts an automated system designed to generate and update `README.md` documentation for GitHub projects using Large Language Models (LLMs). The solution addresses the critical need to maintain consistent and up-to-date documentation in agile, multi-repository development environments.

---

## Table of Contents

*   [1. Project Overview](#1-project-overview)
*   [2. System Architecture](#2-system-architecture)
*   [3. Code Structure](#3-code-structure)
*   [4. Environment Setup](#4-environment-setup)
    *   [4.1. Operating System Level Dependencies](#41-operating-system-level-dependencies)
    *   [4.2. Python Dependencies](#42-python-dependencies)
    *   [4.3. Environment Variables](#43-environment-variables)
*   [5. Core Logic and Pipeline](#5-core-logic-and-pipeline)
    *   [5.1. Execution Flow](#51-execution-flow)
    *   [5.2. Payload and Prompts](#52-payload-and-prompts)
*   [6. Added Value and Technical Justification](#6-added-value-and-technical-justification)
    *   [6.1. Addressing Business Needs](#61-addressing-business-needs)
    *   [6.2. Technology Justification](#62-technology-justification)
*   [7. Output Examples](#7-output-examples)
    *   [7.1. `Consolidado_Documentación.txt` File](#71-consolidadodocumentacióntxt-file)
    *   [7.2. Generated `README.md` Content](#72-generated-readmemd-content)
*   [8. Contribution](#8-contribution)
*   [9. License](#9-license)

---

## 1. Project Overview

This project implements an automation system for generating and updating `README.md` files in GitHub repositories. It leverages the capabilities of Large Language Models (LLMs) to analyze the content of a repository's source code and synthesize structured and relevant documentation. The solution is designed to operate autonomously, iterating over a GitHub user's repositories, identifying those that require documentation or updates, and applying a process for README generation and translation.

The main objective is to standardize documentation, reduce developers' manual workload, and ensure that essential project information is always available and up-to-date, in both Spanish and English.

## 2. System Architecture

The system architecture is client-server, where the Python script acts as a client, interacting with GitHub APIs and LLM APIs (Groq and Google Gemini) as external services.

```
+---------------------+       +---------------------+
|                     |       |                     |
|  Python Script      |       |  GitHub API         |
|  (`main.py` /       |------>|  (PyGithub)         |
|   `Groq_Deepsek_backup.py`)|       |                     |
|                     |       +---------------------+
|  - Loads .env       |                 |
|  - Authentication   |                 |
|  - Reads `Consolidado_Documentación.txt` |                 |
|  - Iterates Repositories |                 |
|  - Extracts Code    |                 |
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
|  - Generates READMEs|<----------------+
|  - Translates READMEs|<----------------+
|  - Updates Repositories |
|  - Updates `Consolidado_Documentación.txt` |
+---------------------+
```

**Key Components:**

*   **Main Script (`main.py` or `Groq_Deepsek_backup.py`):** Orchestrates the entire process. It handles authentication, interaction with GitHub, `prompt` preparation for LLMs, invocation of LLM APIs, response handling, and repository updates.
*   **GitHub API (via `PyGithub`):** Allows the script to authenticate, list repositories, access their content (files and directories), and create or update files (`README.md`, `README_English.md`).
*   **Groq API (via `openai` client):** Provides access to high-performance language models (e.g., Llama-3) for text generation. Used for the initial creation of the `README.md` in Spanish and its subsequent translation.
*   **Google Gemini API (via `google-generativeai`):** Offers an alternative or complement to Groq for text generation, using models like `gemini-2.5-flash`. It is also used for README creation and translation.
*   **`Consolidado_Documentación.txt` File:** Acts as a persistent record of repositories that have already been processed, preventing unnecessary re-processing and optimizing API resource usage.

## 3. Code Structure

The project consists of two main Python files that implement the same logic but use different LLM providers, allowing for flexibility or A/B testing between them.

*   **`Groq_Deepsek_backup.py`**:
    *   Uses the Groq API to interact with models like `llama-3.3-70b-versatile`.
    *   Implements the `consultar_ia` function to interact with the Groq API.
    *   The rest of the logic (repository iteration, code extraction, prompt generation, error handling, translation, and GitHub update) is identical to `main.py`.

*   **`main.py`**:
    *   Uses the Google Gemini API to interact with models like `gemini-2.5-flash`.
    *   Interaction with Gemini is done directly via the `AI_User.models.generate_content` client.
    *   The rest of the logic (repository iteration, code extraction, prompt generation, error handling, translation, and GitHub update) is identical to `Groq_Deepsek_backup.py`.

Both scripts share the following logical structure:

```python
# Load environment variables
import os
from dotenv import load_dotenv
load_dotenv(override=True)

# Authenticate with GitHub
from github import Github, Auth
Git_TOKEN = os.getenv("GIT_TOKEN")
auth = Auth.Token(Git_TOKEN)
Git = Github(auth=auth)
Git_User = Git.get_user()

# Authenticate with LLM API (Groq or Gemini)
# ... (different implementation depending on the file) ...

# Read already documented repositories
with open("Consolidado_Documentación.txt", "r") as Historico:
    Repos_documentados = Historico.read().split("\n")

# Iterate over user's repositories
Repos = Git_User.get_repos()
for repo in Repos:
    # Logic to skip already documented repositories
    if repo.name in Repos_documentados:
        continue

    # Accumulate content of relevant files (.py, .sql, .ipynb, .json)
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
                print(f"Error decoding {archivo.name}: {error}")

    if not acumulated_script:
        continue

    # Define instructions and prompt for README generation
    instrucciones = """You are a Senior Data Analyst & Automation Analyst. Create a professional README.md..."""
    prompt = f"""Generate the final README.md for this project...:\n\n{acumulated_script}"""

    # Call LLM API to generate README (with retries)
    respuesta = None
    for intento in range(max_intentos):
        try:
            # ... (Call to Groq or Gemini) ...
            break
        except Exception as error_api:
            time.sleep(60)

    if not respuesta:
        continue

    readme_final = respuesta.text if hasattr(respuesta, 'text') else respuesta # Handle Gemini vs Groq response

    # Define instructions and prompt for README translation
    instrucciones_traductor = f"You are an expert Senior Data Analyst & Automation Analyst and also an expert technical translator..."
    prompt_traduccion = f"""Generate the English translation of this documentation...: {readme_final}"""

    # Call LLM API to translate README (with retries)
    english_readme = None
    for intento in range(max_intentos):
        try:
            # ... (Call to Groq or Gemini) ...
            break
        except Exception as error_api:
            time.sleep(60)

    if not english_readme:
        continue

    english_readme = english_readme.text if hasattr(english_readme, 'text') else english_readme

    # Update or create README.md and README_English.md in the repository
    commit_msg_es = f"Docs: Auto-generated and automated README with contextualized agents with iterative codes for {repo.name}"
    commit_msg_en = f"Docs: Auto-generated and automated README with contextualized agents with iterative codes for {repo.name}"

    try:
        # Update/Create README.md (Spanish)
        # ...
    except Exception:
        # Create README.md (Spanish)
        # ...

    time.sleep(5)

    try:
        # Update/Create README_English.md (English)
        # ...
    except Exception:
        # Create README_English.md (English)
        # ...

    # Log documented repository
    with open("Consolidado_Documentación.txt", "a") as Documento:
        Documento.write("\n"+repo.name)

    time.sleep(5)

print("Documentation created/updated and finished successfully")
```

## 4. Environment Setup

To run this project, you need to set up the development environment with the appropriate dependencies and required environment variables.

### 4.1. Operating System Level Dependencies

This project does not require specific operating system level dependencies (such as FFmpeg, Tesseract, or hardware drivers) beyond a functional Python environment and internet access to communicate with external APIs.

### 4.2. Python Dependencies

The necessary Python libraries can be installed using `pip`. It is recommended to use a virtual environment to manage dependencies.

```bash
# Create a virtual environment (if you don't have one yet)
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install python-dotenv PyGithub openai google-generativeai
```

### 4.3. Environment Variables

The project uses environment variables to manage sensitive credentials, which is a recommended security practice. You must create a `.env` file in the project root with the following variables:

```ini
GIT_TOKEN="your_github_personal_access_token"
GROQ_KEY="your_groq_api_key"
API_GEMINI_KEY="your_google_gemini_api_key"
```

**Notes on tokens:**

*   **`GIT_TOKEN`**: A GitHub Personal Access Token (PAT) with the necessary permissions to read repositories (`repo` scope) and write files (`write:repo_hook`, `public_repo`, or full `repo` if needed for private repositories).
*   **`GROQ_KEY`**: The API key obtained from the Groq platform.
*   **`API_GEMINI_KEY`**: The API key obtained from Google AI Studio or Google Cloud for Gemini.

## 5. Core Logic and Pipeline

### 5.1. Execution Flow

The execution pipeline follows a defined sequence for each repository:

1.  **Initialization:** Loading environment variables and authenticating with GitHub and LLM providers.
2.  **Documented Repositories Log:** Reads the `Consolidado_Documentación.txt` file to get a list of repositories that have already been processed.
3.  **Repository Iteration:** Retrieves all repositories for the authenticated GitHub user.
4.  **Filtering:** For each repository, checks if it is already in the `Repos_documentados` list. If so, it skips it.
5.  **Code Extraction:** If the repository has not been documented, it recursively traverses its content. It accumulates the text from all files with `.py`, `.sql`, `.ipynb`, and `.json` extensions.
6.  **README Generation (Spanish):**
    *   Constructs a detailed `prompt` that includes specific instructions for README generation and the accumulated source code of the repository.
    *   Sends this `prompt` to the LLM API (Groq or Gemini).
    *   Implements a retry mechanism with waits to handle potential API errors or server saturation.
7.  **README Translation (English):**
    *   Once the Spanish README is obtained, it constructs a new `prompt` to request its translation into English, maintaining technical terminology.
    *   Sends this `prompt` to the LLM API.
    *   Also includes a retry mechanism.
8.  **GitHub Update:**
    *   Attempts to update the `README.md` (Spanish) file in the repository. If it does not exist, it creates it.
    *   Attempts to update the `README_English.md` (English) file in the repository. If it does not exist, it creates it.
    *   Each update/creation operation is performed with a descriptive commit message.
9.  **Logging:** Adds the repository name to the `Consolidado_Documentación.txt` file to mark it as documented.
10. **Pauses:** Introduces pauses (`time.sleep`) between API operations to avoid exceeding rate limits and to allow APIs to process requests.

### 5.2. Payload and Prompts

The main `payload` sent to the LLMs is a text string containing the instructions for README generation and the repository's source code.

**Example `instructions` (role: `system`):**

```
You are a Senior Data Analyst & Automation Analyst. Create a professional, comprehensive, and structured README.md for this repository based on the provided code.
Use Markdown and strictly adhere to the following requirements:
1. Include aesthetic 'Badges' at the beginning, and if they can link to the documentation, even better. IMPORTANT: DO NOT INCLUDE VERSIONS, ONLY THE TECHNOLOGY (e.g., Python version, license, project status).
1.1 If you can include badge images, fine; if not, then don't. It's important to clarify that if you need to document SQL projects, it's BigQuery.
2. Add a navigable Table of Contents with anchor links to each section to improve the developer experience.
3. Explain the architecture, dependencies, and core logic with their respective payload and pipeline.
4. In the configuration section, explicitly specify if operating system level dependencies are required (e.g., FFmpeg, Tesseract installation, drivers, etc.), not just the libraries of the programming language used.
5. If the code generates structured data outputs (JSON, dictionaries, CSV), include a small code block example showing the expected structure of that output to illustrate the results.
6. Be very technical and precise when detailing technologies and added value compared to other solutions (provided it does not include sensitive, confidential business, or personal information), emphasizing why certain libraries are used. Segment the code to explain the fundamental parts.
7. DO NOT reveal sensitive data, credentials, specific tokens or IDs, addresses, names, contacts under any circumstances. If proper nouns exist, replace them with generic terms or things like "User 1/Person 1/Company 1" and so on.
8. Maintain a purely technical, analytical, and direct tone. DO NOT USE EMOJIS ANYWHERE IN THE README. Avoid flattery and DO NOT write in a LinkedIn style (avoid overusing adversative sentences or cliché phrases).
9. Answer business questions, highlight the added value of the code, emphasize what is shown, what it allows to measure, diagnose, resolve, narrow down, optimize, standardize, and rethink (delve deeply into this matter).
```

**Example `prompt` (role: `user`):**

```
Generate the final README.md for this project, applying all requested structural guidelines (badges, table of contents, OS requirements, output examples). 
Here is the source code (it is accumulated in a single block, so analyze it in detail by file path to understand the integration). Likewise, address the business needs and research questions:

### File: Groq_Deepsek_backup.py ###
import os
import time
# ... content of Groq_Deepsek_backup.py file ...

### File: main.py ###
import os
import time
# ... content of main.py file ...
```

For translation, a similar `prompt` is used, but with specific instructions for translation and the already generated README text.

## 6. Added Value and Technical Justification

### 6.1. Addressing Business Needs

This documentation automation system addresses several critical needs in software development and project management:

*   **Resolves lack of documentation:** Eliminates the bottleneck of manual documentation, ensuring that each repository has an initial and updated `README.md`.
*   **Standardizes quality and structure:** By using an LLM with precise instructions, a consistent structure and uniform technical detail level are guaranteed across all READMEs, improving organizational coherence.
*   **Optimizes developer time:** Frees developers from the repetitive and often tedious task of writing documentation, allowing them to focus on code development.
*   **Narrows documentation scope:** Focuses on key source code files (`.py`, `.sql`, `.ipynb`, `.json`), ensuring documentation is relevant and directly linked to the code asset.
*   **Enables documentation coverage measurement:** The `Consolidado_Documentación.txt` file allows clear tracking of which repositories have been processed, facilitating metrics on documentation status.
*   **Diagnoses inconsistencies:** By programmatically generating documentation, code patterns or repository structures that hinder documentation can be identified, potentially leading to improvements in development practices.
*   **Rethinks documentation strategy:** Transforms documentation from a reactive, manual task into a proactive, automated, and scalable process. This encourages the integration of documentation into CI/CD workflows and positions LLMs as fundamental tools for technical knowledge management.
*   **Strategic added value:** Improves onboarding for new team members, facilitates knowledge transfer between projects, reduces technical debt associated with lack of documentation, and ultimately accelerates the software development lifecycle.

### 6.2. Technology Justification

*   **`python-dotenv`**: It is fundamental for secure credential management. It allows storing API tokens and keys in a local `.env` file, keeping them out of version control and protecting them from accidental exposure.
*   **`PyGithub`**: This library is the standard Python interface for the GitHub API. Its use greatly simplifies interaction with repositories, allowing operations such as listing repositories, accessing their content (files and directories), and making commits to create or update files. Its robustness and ease of use are key for automating GitHub tasks.
*   **`openai` (for Groq API)**: Although the library name is `openai`, it is used to interact with the Groq API, which is compatible with the OpenAI API specification. Groq is chosen for its exceptional performance and low latency, which is crucial for processing large volumes of code and generating responses quickly. Its ability to efficiently run state-of-the-art language models like Llama-3 makes it an attractive option for intensive text generation tasks.
*   **`google-generativeai` (for Google Gemini API)**: The inclusion of the Google Gemini API provides a strategic alternative or fallback mechanism. Gemini, with models like `gemini-2.5-flash`, offers powerful text understanding and generation capabilities, making it a robust and competitive option. The duality of LLM providers allows for comparing performance, response quality, and system resilience against potential single-provider outages.
*   **Retry handling and `time.sleep`**: Implementing retries with exponential (or fixed in this case) backoffs is a standard and critical practice when interacting with external APIs. It protects against transient network failures, API rate limits, and server saturation, ensuring the robustness and reliability of the automation pipeline.

## 7. Output Examples

The project generates two main types of outputs: a log file of documented repositories and the `README.md` and `README_English.md` files within each repository.

### 7.1. `Consolidado_Documentación.txt` File

This file is a simple plain text log, where each line contains the name of a repository that has been successfully processed.

```
repo-proyecto-a
mi-proyecto-de-datos
servicio-api-rest
analisis-ventas-q4
```

### 7.2. Generated `README.md` Content

The content of the `README.md` (and `README_English.md`) is a structured Markdown document, following the guidelines provided to the LLM. Below is an example of the expected structure, not the exact content, as this will vary depending on the repository's code.

```markdown
# Repository Name

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub%20API-Integration-informational?style=flat-square&logo=github&logoColor=white)
![Project Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-Unspecified-lightgrey?style=flat-square)

This repository contains a project dedicated to [Brief description of the project's purpose].

## Table of Contents

*   [1. Overview](#1-overview)
*   [2. Architecture](#2-architecture)
*   [3. Setup](#3-setup)
*   [4. Usage](#4-usage)
*   [5. Output Data Structure](#5-output-data-structure)
*   [6. Business Value](#6-business-value)

## 1. Overview

The main objective of this project is [Detailed explanation of the objective]. It focuses on [key areas, functionalities, etc.].

## 2. Architecture

The system follows a [client-server, microservices, monolithic, etc.] architecture. Key components include:
*   **Component A:** [Description]
*   **Component B:** [Description]

## 3. Setup

### 3.1. Operating System Level Dependencies

No specific operating system level dependencies are required beyond a standard Python environment and network access.

### 3.2. Python Dependencies

Install dependencies using pip:
```bash
pip install -r requirements.txt
```
(Or list specific libraries if no `requirements.txt` exists)

### 3.3. Environment Variables

Create a `.env` file in the project root with the following variables:
```ini
API_KEY="your_api_key"
DATABASE_URL="your_database_url"
```

## 4. Usage

To run the project:
```bash
python main.py
```
[More detailed instructions on how to use the project, command examples, etc.]

## 5. Output Data Structure

If the code generates structured data (e.g., JSON, CSV), an example will be shown here.
For instance, if a script generates JSON with analysis results:

```json
{
  "report_id": "REP-2023-10-26-001",
  "analysis_date": "2023-10-26",
  "metrics": {
    "total_records": 1500,
    "average_value": 45.75,
    "max_value": 120.00
  },
  "summary": "Analysis completed successfully for the specified period."
}
```

## 6. Business Value

This project adds value by [mentioning how the project solves a business problem, improves a process, etc.]. It allows to [measure, diagnose, resolve, narrow down, optimize, standardize, rethink] within the context of [business domain].

---
```

## 8. Contribution

Contributions are welcome. Please open an 'issue' to discuss any proposed changes or submit a 'pull request'.

## 9. License

This project does not specify an explicit license. It is recommended to add a `LICENSE` file to define the terms of use and distribution.