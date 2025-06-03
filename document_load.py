from langchain_community.document_loaders import PyPDFLoader
import re
import tempfile

def clean_text(text):
    lines = text.splitlines()
    cleaned_lines = [line for line in lines if not re.fullmatch(r"[\s\|\-]*", line)]
    text = "\n".join(cleaned_lines)
    text = text.replace("|", " ")
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()


def get_resume(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    loader = PyPDFLoader(tmp_path)
    documents = loader.load()
    text = "\n".join([doc.page_content for doc in documents])
    return clean_text(text)
