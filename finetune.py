from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

api_key = ""
#model_name = "gpt-3.5-turbo"
model_name = ""
chat = ChatOpenAI(model=model_name, openai_api_key=api_key)

messages = [
    HumanMessage(content="이 세상은 누가 만들었나?")
]

response = chat(messages)
print(response.content)
