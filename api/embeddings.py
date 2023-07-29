""" Note: This isn't part of the API, just used to generate embeddings for lookups. """

import re
from typing import List

import openai
from config import OPENAI_API_KEY
from config import QDRANT_API_KEY, QDRANT_URL
from qdrant_client import QdrantClient
from qdrant_client.http.models import Batch
from qdrant_client.models import Distance, VectorParams
from glob import glob


def clean_text(text: str) -> str:
    # Replace all newline characters with spaces
    # text = text.replace("\n", " ")

    # Replace multiple spaces with a single space
    text = re.sub(r"\s+", " ", text).strip()

    return text


def get_documents():
    clean_texts = []
    for file in glob("knowledgebase/*.txt"):
        print(f"Processing file {file}")
        with open(file, "r") as f:
            text = f.read()
            docs = text.split("\n")
            docs = [clean_text(doc) for doc in docs if not doc.startswith("#$#") and len(doc) > 0]
            clean_texts.extend(docs)
    return clean_texts


def init_vs():
    collection_name = "wyl-dev"
    documents = []
    ids = []
    vectors = []
    payloads = []
    for num, doc in enumerate(get_documents()):
        print(f"Processing document {num}")
        doc = clean_text(doc)
        documents.append(doc)

        openai.api_key = OPENAI_API_KEY
        response = openai.Embedding.create(
            input=doc,
            model="text-embedding-ada-002",
        )
        ids.append(num)
        vectors.append(response["data"][0]["embedding"])  # type: ignore
        payloads.append({"source": "TODO", "text": doc})

    qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, prefer_grpc=True)
    qdrant_client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
    )
    res = qdrant_client.upsert(
        collection_name=collection_name,
        points=Batch(
            ids=ids,
            vectors=vectors,
            payloads=payloads,
        ),
    )
    print(res)


def query_vs(q: str, k: int = 3, threshold: float = 0.76) -> List[str]:
    qdrant_client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        prefer_grpc=True,
    )

    openai.api_key = OPENAI_API_KEY
    response = openai.Embedding.create(
        input=q,
        model="text-embedding-ada-002",
    )
    query_vector = response["data"][0]["embedding"]  # type: ignore

    res = qdrant_client.search(
        collection_name="wyl-dev",
        query_vector=query_vector,
        limit=k,
        distance=Distance.COSINE,
        append_payload=True,
        with_vectors=False,
        score_threshold=threshold,
    )
    filtered_docs = [doc.payload["text"] for doc in res]  # type: ignore
    return filtered_docs


async def main():
    init_vs()

    # docs = query_vs(
    #     "best programming language",
    #     3,
    #     0.76,
    # )
    # print(docs)
    docs = get_documents()
    print(docs)
    # jsonable_result = jsonable_encoder(docs)
    # print(json.dumps(jsonable_result, indent=2))


if __name__ == "__main__":
    import asyncio

    # queries = "best programming language"
    # res = query_vs(queries, 3, 0.76)
    # print(res)

    asyncio.run(main())
