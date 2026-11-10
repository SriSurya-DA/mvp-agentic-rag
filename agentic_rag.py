from config import llm, embedding, engine
from langchain.tools import tool
from langchain.agents import create_agent

user_question="hi, return policy"

@tool
def company_kb(user_question):
  #prompt
  "Need to use for the company knowledge base"
  print("Running Tool...")
  return engine.similarity_search(user_question,k=3)

def chatbot(user_question):
      
    system_prompt = f"""
    Your name is Asta, you are a helpful assistance for the users,
    answer in crisp, polietly and professionally with the context given for you
    """
  
    agent=create_agent(
       model=llm,
       system_prompt=system_prompt,
       tools=[company_kb]
    )
    response=agent.invoke({'messages':user_question})
    return response["messages"][-1].content
  
answer=chatbot(user_question)
print(answer)
  
