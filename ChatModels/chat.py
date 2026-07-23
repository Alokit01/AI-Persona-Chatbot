from dotenv import load_dotenv


load_dotenv()
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage 
# model = init_chat_model("groq:llama-3.1-8b-instant") # I used groq here for my model 
# model = init_chat_model("mistral-medium-3-5",temperature =0)
model = init_chat_model("mistral-medium-3-5")
message=[
    SystemMessage(content="you are an funny ai agent")
]
print("______________Welcome Type 0 to end this application____________")
while True:
    prompt = input("You : ")
    message.append(HumanMessage(content=prompt))
    if prompt=="0":
        break
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("Bot : ",response.content)

print(message)