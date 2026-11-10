#LLM Model, Embedding Model, Chroma Engine
#--------------------------------

#LLM Model

from langchain_groq import ChatGroq
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

from dotenv import load_dotenv
import os

load_dotenv(override=True)

llm=ChatGroq(
        model="openai/gpt-oss-120b",
)

# -------------------------------------------------------

# Embedding Model
# using GoogleAI Studio

gen_ai_key=os.getenv("GOOGLE_API_KEY")
embedding=GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",api_key=gen_ai_key
)

#-------------------------------------------------------

#Vector Store
# Chroma_Engine

engine=Chroma(
    embedding_function=embedding,
    collection_name="MVP-RAG",
    persist_directory="chroma.db"
)