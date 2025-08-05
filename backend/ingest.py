from langchain_community.document_loaders.directory import DirectoryLoader
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os
import shutil

# Configuración
DATA_PATH = "../data"
CHROMA_PATH = "../chroma"
MODEL_NAME = "solar"  # Cambiar a "llama3", "openhermes", etc. si querés
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# ⚠️ Verificar si el índice ya existe
if os.path.exists(CHROMA_PATH):
    print(f"⚠️ El índice ya existe en {CHROMA_PATH}.")
    respuesta = input("¿Querés reindexar desde cero? (s/n): ").strip().lower()
    if respuesta == "s":
        print("🗑️ Borrando índice anterior...")
        shutil.rmtree(CHROMA_PATH)
    else:
        print("❌ Cancelado por el usuario. No se realizó la indexación.")
        exit()

# 1. Cargar documentos .md desde la carpeta /data
loader = DirectoryLoader(DATA_PATH, glob="**/*.md", show_progress=True)
documents = loader.load()

if not documents:
    print("❌ No se encontraron documentos en la carpeta /data.")
    exit()

# 2. Normalizar el texto: minúsculas, sin espacios innecesarios, saltos de línea unificados
for doc in documents:
    content = doc.page_content
    content = content.lower().strip().replace("\r\n", "\n").replace("\t", " ")
    doc.page_content = content

# 3. Dividir el texto en fragmentos
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)
chunks = text_splitter.split_documents(documents)

# 4. Crear embeddings con Ollama
embedding = OllamaEmbeddings(model=MODEL_NAME)

# 5. Guardar en Chroma (con persistencia local automática)
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory=CHROMA_PATH
)

print(f"✅ Se indexaron {len(chunks)} fragmentos en Chroma.")
