from langchain_community.document_loaders.directory import DirectoryLoader
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os

# Configuración
DATA_PATH = "../data"
CHROMA_PATH = "../chroma"
#MODEL_NAME = "llama3"
MODEL_NAME = "solar"
#MODEL_NAME = "openhermes"

# 1. Cargar documentos .md desde la carpeta /data
loader = DirectoryLoader(DATA_PATH, glob="**/*.md", show_progress=True)
documents = loader.load()

# 2. Normalizar el texto a minúsculas para mejorar el matching
for doc in documents:
    doc.page_content = doc.page_content.lower()

# 3. Dividir el texto en fragmentos
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)

# 4. Crear embeddings con Ollama
embedding = OllamaEmbeddings(model=MODEL_NAME)

# 5. Guardar en Chroma (la persistencia es automática en Chroma >= 0.4.x)
vectordb = Chroma.from_documents(documents=chunks, embedding=embedding, persist_directory=CHROMA_PATH)

print(f"✅ Se indexaron {len(chunks)} fragmentos en Chroma.")
