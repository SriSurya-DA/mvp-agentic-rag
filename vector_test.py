from config import engine

search=engine.similarity_search("phone number",k=1)
#k is chunk count
print(search)
