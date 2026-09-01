import faiss
import numpy as np


documents = []
vectors = []
_model = None


def get_embedding_model():
    global _model

    if _model is None:
        from sentence_transformers import SentenceTransformer

        _model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return _model


def phone_to_document(phone):
    """
    Convert a Phone database object into
    a text document for the RAG system.
    """

    return f"""
Samsung Phone: {phone.name}

Release Date:
{phone.release_date}

Status:
{phone.status}

Source:
{phone.source_url}

Network:
Technology: {phone.technology}
2G Bands: {phone.two_g_bands}
3G Bands: {phone.three_g_bands}
4G Bands: {phone.four_g_bands}
5G Bands: {phone.five_g_bands}
Speed: {phone.speed}

Design:
Dimensions: {phone.dimensions}
Weight: {phone.weight}
Build: {phone.build}
SIM: {phone.sim}
IP Rating: {phone.ip_rating}

Display:
Display Type: {phone.display_type}
Display Size: {phone.display_size}
Resolution: {phone.display_resolution}
Protection: {phone.display_protection}
Refresh Rate: {phone.display_refresh_rate}
Brightness: {phone.display_brightness}

Software:
Operating System: {phone.os}

Performance:
Chipset: {phone.chipset}
CPU: {phone.cpu}
GPU: {phone.gpu}

Memory:
RAM: {phone.ram}
Storage: {phone.storage}
Card Slot: {phone.card_slot}

Camera:
Main Camera: {phone.main_camera}
Ultrawide Camera: {phone.ultrawide_camera}
Telephoto Camera: {phone.telephoto_camera}
Depth Camera: {phone.depth_camera}
Camera Features: {phone.main_camera_features}
Main Camera Video: {phone.main_camera_video}

Selfie Camera:
{phone.selfie_camera}

Selfie Video:
{phone.selfie_video}

Audio:
Loudspeaker: {phone.loudspeaker}
Headphone Jack: {phone.headphone_jack}

Connectivity:
WLAN: {phone.wlan}
Bluetooth: {phone.bluetooth}
GPS: {phone.gps}
NFC: {phone.nfc}
Radio: {phone.radio}
USB: {phone.usb}

Sensors:
{phone.sensors}

Battery:
Capacity: {phone.battery}
Charging: {phone.charging}
Wireless Charging: {phone.wireless_charging}

Colors:
{phone.colors}

Price:
{phone.price}

Models:
{phone.models}
"""


def build_index(phones):

    global documents
    global vectors

    # Make sure there are phones
    if not phones:
        raise ValueError(
            "No phones found in the database."
        )

    # Convert database records to text documents
    documents = [
        phone_to_document(phone)
        for phone in phones
    ]

    # Generate embeddings
    model = get_embedding_model()

    vectors = model.encode(
        documents,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    # Make sure vectors have the correct shape
    vectors = np.asarray(
        vectors,
        dtype="float32"
    )

    if vectors.ndim == 1:
        vectors = vectors.reshape(1, -1)

    dimension = vectors.shape[1]

    # Create FAISS index
    index = faiss.IndexFlatIP(
        dimension
    )

    # Add vectors
    index.add(vectors)

    print(
        f"FAISS index created successfully."
    )

    print(
        f"Documents: {len(documents)}"
    )

    print(
        f"Vector dimension: {dimension}"
    )

    return index


def search(index, question, k=3):

    if index is None:
        return []

    if not documents:
        return []

    # Don't request more results than documents available
    k = min(k, len(documents))

    # Convert question into embedding
    model = get_embedding_model()

    query_vector = model.encode(
        [question],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    query_vector = np.asarray(
        query_vector,
        dtype="float32"
    )

    # Search FAISS
    distances, indices = index.search(
        query_vector,
        k
    )

    results = []

    for i in indices[0]:

        if 0 <= i < len(documents):

            results.append(
                documents[i]
            )

    return results
