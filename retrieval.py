from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from reranker import rerank_documents
import os
from dotenv import load_dotenv

load_dotenv()

EMBEDDINGS = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

COLLECTION_MAP = {
    "FAQs": "faqs",
    "Knowledge Base Articles": "knowledge_base_articles",
    "Product Documentation": "product_documentation",
}

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")


def get_vector_store(collection_name: str):
    return QdrantVectorStore.from_existing_collection(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        collection_name=collection_name,
        embedding=EMBEDDINGS,
    )


def retrieve_documents(query: str, collection_label: str, top_k: int | None = None, return_all: bool = False, **kwargs):
    collection_name = COLLECTION_MAP.get(collection_label)
    if not collection_name:
        raise ValueError(f"Unsupported collection label: {collection_label}")

    if top_k is None:
        top_k = kwargs.pop("k", 5)
    if kwargs:
        unexpected = ", ".join(sorted(kwargs))
        raise TypeError(f"retrieve_documents() got unexpected keyword argument(s): {unexpected}")

    top_k = max(1, int(top_k))
    vector_store = get_vector_store(collection_name)
    retrieved_docs = vector_store.similarity_search(query=query, k=top_k)
    reranked_docs = rerank_documents(query=query, documents=retrieved_docs, top_k=5)

    if return_all:
        return retrieved_docs[:top_k], reranked_docs
    return reranked_docs

