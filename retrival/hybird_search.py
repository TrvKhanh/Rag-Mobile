from typing import List
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain.vectorstores import Chroma
from langchain_core.documents import Document

class HybridSearch:
    def __init__(self, topk: int, path: str, document: List[Document], collection_name: str):
        self.k = topk

        self.bm25 = BM25Retriever.from_documents(document)
        self.bm25.k = self.k

        self.vector_stores = Chroma(
            persist_directory=path,
            collection_name=collection_name
        )
        self.vector_retriever = self.vector_stores.as_retriever(
            search_type="similarity",
            search_kwargs={"k": self.k}
        )

        self.hybrid_retriever = EnsembleRetriever(
            retrievers=[self.bm25, self.vector_retriever],
            weights=[0.3, 0.7],
            mode="reciprocal_rerank"
        )

    def query(self, query: str) -> Document:
        return self.hybrid_retriever.invoke(query)
