import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from agent import process_input

recognizer =sr.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang="te")
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")


while True:
    with sr.Microphone() as source:
        print("speak in Telugu")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="te-IN")
            print("You said:", text)

            response = process_input(text)
            print("Agent:", response)
            speak(response)

        except:
            speak("క్షమించండి, మళ్లీ చెప్పండి")



