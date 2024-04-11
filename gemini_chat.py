import google.generativeai as genai
genai.configure(api_key=" AIzaSyBfQ_-qlXokkIUbxZd8jnXCHAIPj1c1c2c")
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()
while True:
   message = input("You: ")
   response = chat.send_message(message)
   print("Gemini: " + response.text)