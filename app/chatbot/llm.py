import os

import torch
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


load_dotenv()

MODEL_NAME = os.getenv(
    "HF_MODEL_NAME",
    "google/flan-t5-small"
)

HF_TOKEN = os.getenv("HF_TOKEN")

_tokenizer = None
_model = None


def get_model():

    global _tokenizer
    global _model

    if _tokenizer is None or _model is None:

        _tokenizer = AutoTokenizer.from_pretrained(
            MODEL_NAME,
            token=HF_TOKEN if HF_TOKEN else None
        )

        _model = AutoModelForSeq2SeqLM.from_pretrained(
            MODEL_NAME,
            token=HF_TOKEN if HF_TOKEN else None
        )

        _model.eval()

    return _tokenizer, _model


def ask_llm(context, question):
    context = context.strip()

    if len(context) > 2500:
        context = context[:2500]

    prompt = f"""
You are a Samsung smartphone information assistant.

Answer the user's question using ONLY the information in the context.

IMPORTANT RULES:

1. Answer ONLY what the user asked.
2. Do not mention unrelated phone specifications.
3. Do not answer about a different Samsung phone.
4. If the requested information is not clearly available in the context, say:
   "The information is not available in the database."
5. Give a short, direct answer.
6. Do not include the source URL unless the user asks for it.

Context:
{context}

User Question:
{question}

Answer:
"""

    tokenizer, model = get_model()

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=768
    )

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_new_tokens=140,
            num_beams=4,
            do_sample=False
        )

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    ).strip()

    return answer
