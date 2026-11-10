from config import llm,embedding,engine

user_question="""
What is your name and How long can customers export their data after cancelling?"""

def company_kb(user_question):
    return engine.similarity_search(user_question,k=3)

def chatbot(user_question):
    search_content=company_kb(user_question=user_question)
    
    system_prompt = f"""
    Your name is Asta, you are a helpful assistance for the users,
    answer in crisp, polietly and professionally with the context given for you

    user asked this:{user_question}
    the context you have is {search_content}
    """

    response=llm.invoke(system_prompt)
    return response.content

answer=chatbot(user_question)
print(answer)

"""Here for the simple user questions, Hi, how are you.. for these 
it will use the vector search so its time consuming in future will intergrate
with the tool option [Refer: agentic_rag.py]"""