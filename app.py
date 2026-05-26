import streamlit as st

from pdf_loader import load_pdf

from vector_store import (
    create_chunks,
    create_vector_store,
    search_chunks
)

from rag_pipeline import generate_answer


st.set_page_config(
    page_title="Research Paper Assistant",
    layout="wide"
)

st.title("📚 AI Research Paper Assistant")

st.write(
    "Upload a research paper and ask questions."
)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Reading PDF..."):

        text = load_pdf(uploaded_file)

    st.success("PDF text extracted!")

    with st.spinner("Creating embeddings..."):

        chunks = create_chunks(text)

        create_vector_store(chunks)

    st.success("Vector database created!")

    question = st.text_input(
        "Ask question from paper"
    )

    if question:

        with st.spinner("Searching relevant content..."):

            relevant_chunks = search_chunks(question,top_k=1)

            context = " ".join(relevant_chunks)

        with st.spinner("Generating answer..."):

            answer = generate_answer(
                question,
                context
            )

        st.subheader("Answer")

        st.write(answer)

        st.subheader("Retrieved Context")

        for chunk in relevant_chunks:

            st.info(chunk)