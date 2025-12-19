import speech_recognition as sr
import pyttsx3

recognizer =sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    with sr.Microphone() as source:
        print("speak in Telugu...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="te-IN")
            print("You said:", text)

            speak(text)

        except:
            speak("క్షమించండి, మళ్లీ చెప్పండి")



