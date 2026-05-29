from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os

embedding_model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def create_chunks(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80
    )

    chunks = splitter.split_text(text)

    return chunks


def create_vector_store(chunks):

    embeddings = embedding_model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    if not os.path.exists("vector_db"):
        os.makedirs("vector_db")

    faiss.write_index(
        index,
        "vector_db/faiss_index.index"
    )

    with open(
        "vector_db/chunks.pkl",
        "wb"
    ) as f:

        pickle.dump(chunks, f)

def search_chunks(query, top_k=3):

    index = faiss.read_index(
        "vector_db/faiss_index.index"
    )

    with open(
        "vector_db/chunks.pkl",
        "rb"
    ) as f:

        chunks = pickle.load(f)

    query_embedding = embedding_model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding),
        top_k
    )

    results = []

    for i in indices[0]:

        if i < len(chunks):

            chunk = chunks[i]

            # remove noisy chunks
            if (
                len(chunk) > 300
                and "Figure" not in chunk
                and "Table" not in chunk
                and "<EOS>" not in chunk
                and "Layer" not in chunk
                and "Input-Input" not in chunk
            ):

                results.append(chunk)

    return results