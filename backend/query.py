from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

#MODEL_NAME = "llama3"
MODEL_NAME = "solar"
#MODEL_NAME = "openhermes"

CHROMA_PATH = "../chroma"

# Prompt personalizado para RAG
CUSTOM_PROMPT_TEMPLATE = """
Eres un asistente útil que responde en base al siguiente contexto. Si no puedes encontrar una respuesta clara, responde "No lo sé" de forma amable.

Contexto:
{context}

Pregunta:
{question}

Respuesta:
"""

def main():
    # Embeddings y vectorstore
    embedding = OllamaEmbeddings(model=MODEL_NAME)
    vectordb = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding)

    # Configurar retriever
    retriever = vectordb.as_retriever(search_kwargs={"k": 8})

    # Instanciar LLM
    llm = OllamaLLM(model=MODEL_NAME)

    # Definir el prompt
    prompt = PromptTemplate(
        template=CUSTOM_PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )

    # Crear el chain
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    while True:
        query = input("\nPregunta (o 'salir' para terminar): ")
        if query.lower() == "salir":
            break

        # Normalizar la query
        query = query.lower()

        # Ejecutar consulta
        result = qa.invoke({"query": query})

        print("💬 Respuesta:\n", result["result"])

if __name__ == "__main__":
    main()
