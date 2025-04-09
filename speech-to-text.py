#speech-to-text using speech_recognition and pyttsx3 & also saving in text file
import speech_recognition as sr
import pyttsx3 as ps

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text-to-speech
def Speak(command):
    # Initialize the engine
    engine = ps.init()
    engine.say(command)
    engine.runAndWait()

# Loop infinitely for user to speak
while True:   
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            #listens for the user's input
            audio2 = r.listen(source2)
            # Using google to recognize audio
            text= r.recognize_google(audio2)
            text = '\n' + text.lower() 
            print(text)
            #saving to recorded text in file
            file = open("text.txt",'a+')
            file.write(text)
            if text=='\ncode':
                Speak('File created. Bye Bye!')
                file.close()
                break
            '''print("Did you say ",MyText)
            SpeakText(MyText)'''
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown Error Occurred")
