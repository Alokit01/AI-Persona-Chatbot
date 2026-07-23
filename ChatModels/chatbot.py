from dotenv import load_dotenv


load_dotenv()
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage 
# model = init_chat_model("groq:llama-3.1-8b-instant") # I used groq here for my model 
# model = init_chat_model("mistral-medium-3-5",temperature =0)
model = init_chat_model("mistral-medium-3-5")
print("press 1 for angry mode")
print("press 2 for funny mode")
print("press 3 for sad mode ")
choice=int(input("Choose the mode of chatbot : "))
if choice==1:
    mode="your are an angry agent. you respond aggressively and impatiently"
elif choice==2:
    mode="you are a very funny ai agent. you respond with humour and jokes"
elif choice==3:
    mode="you are a sad ai agent and give ans in very sad manner"
elif choice==4:
    mode="you are a serious and genious ai agent and give ans in very seroius manner"
elif choice==5:
    mode="you are a teacher ai agent and give ans in philoshopical manner"
elif choice==6:
    mode="you are a coder ai agent and do not entaintain any other message apart from coding question."

message=[
    SystemMessage(content=mode)
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

