# Developed by mdrehan4all (Md Rehan)

import os
import openai
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 0.7)
    engine.say(str(text))
    engine.runAndWait()

speak('Hello World')

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: What is Moon"

def myfn(q):
    response = openai.Completion.create(
        model="text-davinci-003",
        #model="text-ada-001",
        #model="text-curie-001",
        prompt="\n\nHuman: "+str(q)+"\nAI: ",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response

recording = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        recording.adjust_for_ambient_noise(source, duration=0.9)
        print("Please Say something:")
        audio = recording.listen(source)
    try:
        text = recording.recognize_google(audio)
        print("You said: \n" + text)
        #speak(text)
        r = myfn(text)
        print(r["choices"][0]["text"])
        speak(r["choices"][0]["text"])
    except Exception as e:
        print(e)