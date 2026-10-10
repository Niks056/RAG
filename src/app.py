""" Run python src/app.py to see the output """

from data_loader import load_all_documents
from embeddings import EmbeddingPipeline
from vectorstore import FaissVectorStore
from search import RAGSearch


## Example Usage

if __name__=="__main__": 
    #docs =load_all_documents("data")
    store=FaissVectorStore("faiss_store")
    #store.build_from_documents(docs)
    #print(chunkvectors)
    store.load()
    
    rag_search =RAGSearch()
    query= "What is attention mechanism?"
    summary= rag_search.search_and_summarize(query, top_k=3)
    print("Summary:",summary)