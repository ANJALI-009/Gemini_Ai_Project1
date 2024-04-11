import google.generativeai as genai
genai.configure(api_key="AIzaSyBfQ_-qlXokkIUbxZd8jnXCHAIPj1c1c2c")
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("What is the meaning of life?")
print(response.text)

