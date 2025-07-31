import os
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA

MODEL_NAME = "llama3"

def main():
    embedding = OllamaEmbeddings(model=MODEL_NAME)
    vectordb = Chroma(persist_directory="../chroma", embedding_function=embedding)
    retriever = vectordb.as_retriever()

    llm = OllamaLLM(model=MODEL_NAME)

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    while True:
        query = input("Pregunta (o 'salir' para terminar): ")
        if query.lower() == "salir":
            break
        respuesta = qa.invoke({"query": query})
        print("Respuesta:", respuesta)

if __name__ == "__main__":
    main()
