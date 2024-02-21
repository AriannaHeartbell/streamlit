import streamlit as st
from PIL import Image
import fitz  #pip install pymupdf 필요



# 제목
st.title('Streamlit Tutorial')


with st.expander("UI 다루기"):
    # 버튼
    if st.button('클릭하세요!'):
       user_input = st.text_input("문자열을 입력해주세요", "Streamlit은 정말 멋져요!")
       st.write(f'입력한 내용: {user_input}')

    # 체크박스
    if st.checkbox('보이기/숨기기'):
       st.write("체크박스가 활성화되었어요!")

    # 셀렉트박스
    option = st.selectbox('좋아하는 숫자를 고르세요', list(range(1, 11)))
    st.write('선택한 숫자:', option)

    # 슬라이더
    age = st.slider('나이', 0, 100, 25)
    st.write("나이는", age, "살이에요")

    # 하이퍼링크
    st.markdown('[ChatGPT 참조](https://chat.openai.com/share/521db437-f259-453b-99fd-b3ca4c85376c)')


with st.expander("이미지 업로드 기능"):

    # 이미지 업로드
    uploaded_file = st.file_uploader("이미지 파일을 업로드하세요", type=['jpg', 'png'])
    if uploaded_file is not None:
       image = Image.open(uploaded_file)
       st.image(image, caption='업로드한 이미지', use_column_width=True)

with st.expander("음악 업로드 기능"): 

    # 음악 업로드
    uploaded_audio_file = st.file_uploader("음악 파일을 업로드하세요", type=['mp3', 'wav'])
    if uploaded_audio_file is not None:
       st.audio(uploaded_audio_file.read(), format='audio/wav')

with st.expander("텍스트 업로드 기능"): 
    
    # 텍스트 파일 업로드
    uploaded_text_file = st.file_uploader("텍스트 파일을 업로드하세요", type=['txt'])
    if uploaded_text_file is not None:
    # 파일 내용을 문자열로 읽기
      string_data = uploaded_text_file.getvalue().decode("utf-8")
      st.text_area("파일 내용", string_data, height=250)

with st.expander("pdf 업로드 기능"): 

    # PDF 파일 업로드
    uploaded_pdf_file = st.file_uploader("PDF 파일을 업로드하세요", type=['pdf'])
    if uploaded_pdf_file is not None:
      doc = fitz.open("pdf", uploaded_pdf_file.read())  # PDF 파일 로드
      text = ""
      for page in doc:  # 각 페이지별로 텍스트 추출
        text += page.get_text()
      st.text_area("PDF 파일 내용", text, height=300)






# 파일 실행
# streamlit run app.py