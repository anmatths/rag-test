# Pasos para configurar un sistema RAG local con Ollama y LangChain

Este archivo resume los pasos necesarios para crear un sistema RAG (Retrieval-Augmented Generation) usando Ollama, LangChain y ChromaDB, con documentos en formato Markdown.

---

## 1. Requisitos

- Tener Ollama instalado (`https://ollama.com/download`)
- Tener Python 3.10+ y `venv` disponibles
- Tener un modelo compatible instalado con Ollama (por ejemplo `llama3`)
- Tener Git instalado si se clona un repositorio
  
### Comandos para actualizar:
sudo apt update && sudo apt upgrade -y

### Comandos para instalar ollama:
#### opcion con snap
1. sudo snap install ollama

#### alternativa
1. sudo apt install curl -y
1. curl -fsSL https://ollama.com/install.sh | sh
1. ollama --version

### Comandos para descargar un modelo
1. ollama pull llama3 *descarga llama3*
2. ollama pull solar *descarga solar*
3. ollama pull openhermes *descarga hermes, muy bueno para rag*

### Probar ollama
ollama run llama3
---

## 2. Clonar el proyecto base o usar uno propio

```bash
git clone https://github.com/langchain-ai/langchain.git
cd langchain
```

(O crear una carpeta propia, ejemplo `[carpeta_proyecto]/backend`)

---

## 3. Estructura de carpetas propio

```
[Carpeta_proyecto]]/
├── backend/
│   ├── ingest.py
│   ├── query.py
│   ├── requirements.txt
├── data/
│   └── documento.md
├── chroma/   # Se genera automáticamente
```

---

## 4. Crear entorno virtual e instalar dependencias

```bash
apt install python3.10-venv
cd backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Si falta algún paquete, instalarlo manualmente:

```bash
pip install langchain langchain-community langchain-chroma langchain-ollama chromadb
```

---

## 5. Agregar un documento de ejemplo

Guardar en `data/documento.md` un archivo como este:

```markdown
# Ejemplo de documento

Este es un archivo markdown de prueba para nuestro sistema RAG.

El color favorito de Matias es el azul y siempre piensa en el número 41.3 porque le recuerda a PI pero al revés.
```

---

## 6. Ingestar los datos

```bash
python ingest.py
```

Este script carga el contenido del archivo `.md`, lo divide en fragmentos y los indexa usando ChromaDB y embeddings de Ollama.

---

## 7. Consultar usando RAG

```bash
python query.py
```

El sistema usará el modelo de Ollama (ej. `llama3`) para responder en base a los documentos indexados.

---

## Notas

- Asegurate de tener corriendo Ollama con el modelo adecuado (`ollama run llama3`)
- Si cambia el nombre del modelo, también cambiarlo en los scripts
- Para acelerar las respuestas, se recomienda hardware con GPU y suficiente RAM

---

