import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


documents = []
vectors = []


def phone_to_document(phone):

    return f"""
Samsung Phone: {phone.name}

Display:
{phone.display}

Resolution:
{phone.resolution}

Refresh Rate:
{phone.refresh_rate}

Processor:
{phone.chipset}

RAM:
{phone.ram}

Storage:
{phone.storage}

Main Camera:
{phone.main_camera}

Ultrawide Camera:
{phone.ultrawide_camera}

Telephoto Camera:
{phone.telephoto_camera}

Selfie Camera:
{phone.selfie_camera}

Video:
{phone.video}

Battery:
{phone.battery}

Charging:
{phone.charging}

Operating System:
{phone.operating_system}

Weight:
{phone.weight}

Price:
{phone.price}
"""


def build_index(phones):

    global documents
    global vectors

    documents = [
        phone_to_document(phone)
        for phone in phones
    ]

    vectors = model.encode(
        documents,
        convert_to_numpy=True
    )

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        np.array(vectors).astype(
            "float32"
        )
    )

    return index


def search(index, question, k=3):

    query_vector = model.encode(
        [question],
        convert_to_numpy=True
    ).astype("float32")

    distances, indices = index.search(
        query_vector,
        k
    )

    results = []

    for i in indices[0]:

        if i < len(documents):
            results.append(
                documents[i]
            )

    return results