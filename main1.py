
from dotenv import load_dotenv
load_dotenv()


from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()
agent = create_react_agent(
   model="groq:llama-3.3-70b-versatile", 
   tools=[], 
   checkpointer=checkpointer,
   prompt="You are a helpful assistant" 
)

config1 = {"configurable": {"thread_id": "1"}}
config2 = {"configurable": {"thread_id": "2"}}
# Run the agents
first_response = agent.invoke(
   {"messages": [{"role": "user", "content": "who is modi"}]},
   config1 
)
second_response = agent.invoke(
   {"messages": [{"role": "user", "content": "when was he born?"}]},
   config2
)
third_response = agent.invoke(
   {"messages": [{"role": "user", "content": "when was he born?"}]},
   config1
)


print(first_response.AIMessage)
print('-------------')
print(second_response.AIMessage)
print('-------------')
print(third_response.AIMessage)