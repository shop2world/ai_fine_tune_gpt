from openai import OpenAI

# 여기에 자신의 API 키를 넣어주세요
api_key = ""

# OpenAI 객체 생성 시 API 키 전달
client = OpenAI(api_key=api_key)

response = client.fine_tuning.jobs.create(
  training_file="file-NueqxsufQJBc7AaCWONveTpH", 
  model="gpt-3.5-turbo"
)

print(response)
