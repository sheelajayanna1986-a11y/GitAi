from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()
from langgraph.prebuilt import create_react_agent




class QuizResponse(BaseModel):
   question: str
   answer: str


agent = create_react_agent(
   model="groq:llama-3.3-70b-versatile", 
   tools=[], 
   response_format = QuizResponse
)


config = {"configurable": {"thread_id": "1"}}
response = agent.invoke(
   {"messages": [{"role": "user", "content": "Get few questionand answers on oracle sql"}]},
   config 
)
print(response)
print("------------------------------")
print(response["structured_response"])


print("Question------------------------------")
print(response["structured_response"].question)


print("Answer------------------------------")
print(response["structured_response"].answer)
