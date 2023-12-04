import gradio as gr
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap, RunnablePassthrough
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

def setup_langchain():
    loader = TextLoader("./regras_workshop.txt")
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(docs, embedding_function)
    retriever = vectorstore.as_retriever()

    prompt = ChatPromptTemplate.from_template("""
    Answer the question based only on the following context:
    {context}

    Question: {question}

    """)

    model = Ollama(model="dolphin2.2-mistral")

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
    )

    return chain

def main():
    langchain_chain = setup_langchain()

    iface = gr.Interface(
        fn=langchain_chain.stream,
        inputs=["text"],
        outputs="text",
        live=True,
        title="LangChain Chat",
        description="Answer questions based on context using LangChain",

    )

    iface.launch()

if __name__ == "__main__":
    main()