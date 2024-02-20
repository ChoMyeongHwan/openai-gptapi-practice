####### lib 설치 ##########
# pip install openai
# pip install streamlit
###########################
# 실행 : streamlit run dalle.py
###########################
import streamlit as st
import io
import base64
from openai import OpenAI
from PIL import Image
from env import openai_key 
import os  # os 모듈 추가

client = OpenAI(
    api_key = openai_key.api_key
)

def get_image(prompt):
    response = get_image_info(prompt)  # DALLE로부터 Base64 형태의 이미지를 얻음.
    image_data = base64.b64decode(response)  # Base64로 쓰여진 데이터를 이미지 형태로 변환
    image = Image.open(io.BytesIO(image_data))  # '파일처럼' 만들어진 이미지 데이터를 컴퓨터에서 볼 수 있도록 Open
    return image

def get_image_info(prompt): 
    response = client.images.generate(
    model="dall-e-3",  # 모델은 DALLE 버전3 (현 최신 버전)
    prompt=prompt,  # 사용자의 프롬프트
    size="1024x1024",  # 이미지의 크기
    quality="standard",  # 이미지 퀄리티는 '표준'
    response_format='b64_json',  # 이때 Base64 형태의 이미지를 전달한다.
    n=1,
    )
    return response.data[0].b64_json

st.title("그림 그리는 AI 화가 서비스 👨‍🎨")

st.image('https://wikidocs.net/images/page/215361/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%ED%99%94%EA%B0%80.png', width=200)

st.text("🎨 Tell me the picture you want. I'll draw it for you!")

input_text = st.text_area("원하는 이미지의 설명을 영어로 적어보세요.", height=200)

def save_image(image, folder='saved_images'):
    if not os.path.exists(folder):
        os.makedirs(folder)  # 폴더가 없으면 생성

    files = os.listdir(folder)  # 폴더 내 파일 목록을 가져옴
    file_count = len(files)  # 파일 개수를 세어서
    next_file_number = file_count + 1  # 다음 파일 번호를 결정
    
    image_path = os.path.join(folder, f"saved_img{next_file_number}.png")  # 저장할 경로와 파일 이름 설정
    image.save(image_path)  # 이미지 저장
    return image_path  # 저장된 이미지 경로를 반환

# 사용자의 입력으로부터 이미지를 전달받고 저장하는 코드
if st.button("Painting"):
    if input_text:
        try:
            dalle_image = get_image(input_text)
            image_path = save_image(dalle_image)  # 이미지를 저장하고 경로를 받음
            st.image(dalle_image)
            st.success(f"이미지 저장 경로 : {image_path}")  # 사용자에게 이미지 저장 위치를 알림
        except:
            st.error("요청 오류가 발생했습니다")
    else:
        st.warning("텍스트를 입력하세요")

# ---------------------------------------------------------------------------------------------------------
# ####### lib 설치 ##########
# # pip install openai
# # pip install streamlit
# ###########################
# # 실행 : streamlit run dalle.py
# ###########################
# import streamlit as st
# import io
# import base64
# from openai import OpenAI
# from PIL import Image
# from env import openai_key 

# client = OpenAI(
#     api_key = openai_key.api_key
# )

# def get_image(prompt):
#     response = get_image_info(prompt) # DALLE로부터 Base64 형태의 이미지를 얻음.
#     image_data = base64.b64decode(response) # Base64로 쓰여진 데이터를 이미지 형태로 변환
#     image = Image.open(io.BytesIO(image_data)) # '파일처럼' 만들어진 이미지 데이터를 컴퓨터에서 볼 수 있도록 Open
#     return image

# # DALLE가 이미지를 반환하는 함수.
# def get_image_info(prompt): 
#     response = client.images.generate(
#     model="dall-e-3", # 모델은 DALLE 버전3 (현 최신 버전)
#     prompt=prompt, # 사용자의 프롬프트
#     size="1024x1024", # 이미지의 크기
#     quality="standard", # 이미지 퀄리티는 '표준'
#     response_format='b64_json', # 이때 Base64 형태의 이미지를 전달한다.
#     n=1,
#     )
#     return response.data[0].b64_json

# st.title("그림 그리는 AI 화가 서비스 👨‍🎨")

# st.image('https://wikidocs.net/images/page/215361/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%ED%99%94%EA%B0%80.png', width=200)

# st.text("🎨 Tell me the picture you want. I'll draw it for you!")

# input_text = st.text_area("원하는 이미지의 설명을 영어로 적어보세요.", height=200)

# # Painting이라는 버튼을 클릭하면 True
# if st.button("Painting"):

#     # 이미지 프롬프트가 작성된 경우 True
#     if input_text:
#         try:
#             # 사용자의 입력으로부터 이미지를 전달받는다.
#             dalle_image = get_image(input_text)

#             # st.image()를 통해 이미지를 시각화.
#             st.image(dalle_image)
#         except:
#             st.error("요청 오류가 발생했습니다")
#     # 만약 이미지 프롬프트가 작성되지 않았다면
#     else:
#         st.warning("텍스트를 입력하세요")
