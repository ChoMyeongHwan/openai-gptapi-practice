# pip install python-dotenv -> 설치 모듈
from dotenv import load_dotenv
from openai import OpenAI

import os

# load .env -> 권장되는 방식
load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")
# print(API_KEY)
client = OpenAI(
    # api_key="키값"
    api_key=API_KEY,
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "너는 IT전문가야."},
    {"role": "user", "content": "전세계서 가장 많이 사용하는 프로그래밍 언어 top5를 얘기해줘"}
  ]
)

print(completion.choices[0].message)