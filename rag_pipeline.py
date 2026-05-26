from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

def generate_answer(question, context):

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    result = generator(
        prompt,
        max_new_tokens=100,
        temperature=0.2,
        do_sample=True
    )

    generated_text = result[0]["generated_text"]

    # remove prompt from output
    answer = generated_text.split("Answer:")[-1].strip()

    return answer