from langchain_community.document_loaders import PyPDFLoader

#file_path = "KS_Abhiram_CSE.pdf"

def read_pdf(file_path):
    loader = PyPDFLoader(file_path)

    documents = loader.load()
    return documents
