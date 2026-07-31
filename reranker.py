from functools import lru_cache

from sentence_transformers import CrossEncoder


@lru_cache(maxsize=1)
def get_reranker():
    return CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank_documents(query: str, documents, top_k: int = 5):
    if not documents:
        return []

    reranker = get_reranker()
    pairs = [[query, doc.page_content] for doc in documents]
    scores = reranker.predict(pairs)

    ranked = sorted(
        zip(documents, scores),
        key=lambda item: item[1],
        reverse=True,
    )
    return [doc for doc, _ in ranked[:top_k]]
