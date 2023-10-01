import os

import weaviate
from langchain.chains import RetrievalQA
from langchain.chains.retrieval_qa.base import BaseRetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate


def __init_rag_chain(index_name: str) -> BaseRetrievalQA:
    llm = ChatOpenAI(openai_api_key=os.getenv('OPEN_AI_API_KEY'), model_name="gpt-4")

    vector_store = __init_langchain_vector_store(index_name)

    return RetrievalQA.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        return_source_documents=True
    )


def __init_langchain_vector_store(index_name: str, attributes: list = None) -> Weaviate:
    if attributes is None:
        attributes = []
    openai_embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv('OPEN_AI_API_KEY'),
        model="text-embedding-ada-002"
    )

    client = __init_weaviate_client()

    return Weaviate(client=client,
                    embedding=openai_embeddings,
                    index_name=index_name,
                    text_key="text",
                    attributes=attributes,
                    by_text=False)


def __init_weaviate_client() -> weaviate.Client:
    weaviate_url = os.getenv('WEAVIATE_CLUSTER_URL')

    auth_config = weaviate.auth.AuthApiKey(
        api_key=os.getenv('WEAVIATE_API_KEY'),
    )

    return weaviate.Client(
        url=weaviate_url,
        auth_client_secret=auth_config,
        additional_headers={
            "X-OpenAI-Api-Key": os.getenv('OPEN_AI_API_KEY')
        }
    )
