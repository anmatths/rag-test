import os
import datetime
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Configuración
MODEL_NAME = "solar"  # Cambiar si se desea usar otro modelo compatible con Ollama
CHROMA_PATH = "../chroma"
OUTPUT_DIR = "./respuestas"
TOP_K = 6

# Prompt para el RAG
CUSTOM_PROMPT_TEMPLATE = """
Eres un asistente útil que responde en base al siguiente contexto. Si no puedes encontrar una respuesta clara, responde "No lo sé" de forma amable.

Contexto:
{context}

Pregunta:
{question}

Respuesta:
"""

# Prompt para reformatear la conversación como Markdown limpio
REFORMAT_PROMPT_TEMPLATE = """
Reescribe la siguiente pregunta y respuesta en formato Markdown, estructurado y claro, como si fuera parte de una base de conocimientos. 
No inventes contenido. Usa encabezados adecuados, listas si es necesario y conserva el estilo conciso.

Pregunta:
{pregunta}

Respuesta:
{respuesta}
"""

def guardar_respuesta_reformateada(llm, pregunta, respuesta, output_dir=OUTPUT_DIR):
    # Formar el prompt
    prompt = REFORMAT_PROMPT_TEMPLATE.format(pregunta=pregunta, respuesta=respuesta)

    # Invocar al modelo
    try:
        reformateado = llm.invoke(prompt)
    except Exception as e:
        print(f"❌ Error al reformatear con LLM: {e}")
        return

    # Crear carpeta de salida si no existe
    os.makedirs(output_dir, exist_ok=True)

    # Generar nombre de archivo seguro
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_title = "_".join(pregunta.strip().lower().split())[:50]
    filename = os.path.join(output_dir, f"{timestamp}_{safe_title}.md")

    # Guardar
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(reformateado)
        print(f"📝 Conversación guardada en: {filename}")
    except Exception as e:
        print(f"❌ Error al guardar archivo: {e}")

def main():
    # Embeddings y vectorstore
    embedding = OllamaEmbeddings(model=MODEL_NAME)
    vectordb = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding)

    # Configurar retriever
    retriever = vectordb.as_retriever(search_kwargs={"k": TOP_K})

    # Instanciar LLM
    llm = OllamaLLM(model=MODEL_NAME)

    # Prompt para RAG
    prompt = PromptTemplate(
        template=CUSTOM_PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )

    # Crear la cadena de QA
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    print("🤖 Sistema RAG activo. Escribí tu pregunta o 'salir' para terminar.")

    while True:
        query = input("\nPregunta: ").strip()
        if query.lower() == "salir":
            print("👋 ¡Hasta luego!")
            break

        if not query:
            continue

        try:
            # Ejecutar consulta
            result = qa.invoke({"question": query})
            respuesta = result["result"]

            # Mostrar respuesta
            print("\n💬 Respuesta:\n", respuesta)

            # Guardar la conversación reescrita como Markdown
            guardar_respuesta_reformateada(llm, query, respuesta)

        except Exception as e:
            print(f"❌ Error durante la consulta: {e}")

if __name__ == "__main__":
    main()
