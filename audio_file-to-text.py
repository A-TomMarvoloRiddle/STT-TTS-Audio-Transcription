#program to recognise sudio from file & saving it in a text file
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

#storing wav file in variable
audiof = "C:\\Users\\Apaar\\Documents\\Sound Recordings\\Recording.wav"

with sr.AudioFile(audiof) as source:
    audio = recognizer.record(source)  # Read the entire audio file
    text = recognizer.recognize_google(audio)  # Perform speech recognition

print("\nRecognized Text:", text, '\n')

with open('file_audio.txt','a+') as file:
    file.write(text)

