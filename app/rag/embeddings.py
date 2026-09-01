_model = None


def get_embedding_model():
    global _model

    if _model is None:
        from sentence_transformers import SentenceTransformer

        _model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return _model


def create_embedding(text):
    model = get_embedding_model()

    return model.encode(
        text,
        convert_to_numpy=True
    )
