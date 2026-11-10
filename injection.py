from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

#Data load
loader = PyPDFLoader("company_data.pdf")
text=loader.load()
#print(len(text))

# Chuncking
# RecursiveCharacterTextSplitter -- It will split line wise, sentence wise, paragraph wise

data_splitter=RecursiveCharacterTextSplitter(

    chunk_size=120,
    chunk_overlap=20
)

chunk=data_splitter.split_documents(text)
