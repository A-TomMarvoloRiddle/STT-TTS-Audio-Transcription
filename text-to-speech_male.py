import win32com.client as wc

# Calling the Dispatch method of the module which interact with Microsoft Speech SDK
speaker = wc.Dispatch("SAPI.SpVoice")

print("\nHi, I am Apaar's Robo Speaker")
speaker.Speak("Hi, I am Apaar's Robo Speaker")

while True:
    s=input("\nWhat do you want me to say: \n")
    if s=='bye':
        print('Bye Bye!')
        speaker.Speak("Bye Bye!")
        break
    speaker.Speak(s)
