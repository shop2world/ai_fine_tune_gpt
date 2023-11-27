from openai import OpenAI

# 여기에 자신의 API 키를 넣어주세요
api_key = ""

# OpenAI 객체 생성 시 API 키 전달
client = OpenAI(api_key=api_key)

# 파일 생성 및 fine-tune 목적으로 업로드
response = client.files.create(
    file=open("openbible_data.jsonl", "rb"),
    purpose="fine-tune"
)

print(response)
