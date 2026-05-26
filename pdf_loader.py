import fitz
import re


def is_valid_line(line):

    line = line.strip()

    # remove short/noisy lines
    if len(line) < 40:
        return False

    # remove figure/table captions
    bad_patterns = [
        "Figure",
        "Table",
        "<EOS>",
        "<pad>",
        "Layer",
        "Input-Input",
        "attention heads",
        "Best viewed in color",
    ]

    for pattern in bad_patterns:
        if pattern in line:
            return False

    return True


def clean_text(text):

    text = re.sub(r'\s+', ' ', text)

    text = re.sub(r'\S+@\S+', '', text)

    text = re.sub(r'http\S+', '', text)

    return text


def load_pdf(uploaded_file):

    pdf = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    extracted_lines = []

    for page in pdf:

        text = page.get_text()

        lines = text.split("\n")

        for line in lines:

            if is_valid_line(line):

                extracted_lines.append(line)

    final_text = " ".join(extracted_lines)

    final_text = clean_text(final_text)

    return final_text