import speech_recognition as sr
from gtts import gTTS
import os
import openai

openai.api_key='sk-xxxx'
# Initialize the recognizer
r = sr.Recognizer()
while True:
    # Use the Raspberry Pi's default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        # Recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        print("You said:", text)
    
        # Convert text to speech using gTTS
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
    
        # Play the generated speech output using mpg321
        os.system("mpg321 output.mp3")
        
        # Send input to OpenAI API
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{text}"}])
        response_text = response.choices[0].message.content
        print(response_text)
            # Convert text to speech using gTTS
        tts = gTTS(text=response_text, lang='en')
        tts.save("output.mp3")
    
        # Play the generated speech output using mpg321
        os.system("mpg321 output.mp3")
    
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print("Sorry, I encountered an error while trying to process your request:", str(e))
