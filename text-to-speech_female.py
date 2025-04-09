#text-to-speech using pyttsx3 for female voice 
import pyttsx3

#Making a convertor object/engine 
con=pyttsx3.init()

#getProperty can also be used see the 'rate' & 'volume' using getProperty to get list of voices in system's Registry Directory
voices = con.getProperty('voices')

#using setProperty to set the voice 
con.setProperty('voice', voices[1].id)
con.setProperty('rate', 150)

print("\nHi, I am Apaar's Robo Speaker")
con.say("Hi, I am Apaar's Robo Speaker")

#using runAndWait() to let it complete speaking & only then move further
con.runAndWait()

while True:
    s=input("\nWhat do you want me to speak:\n")
    if s == 'bye':
        print("Bye Bye!")
        con.say("Bye Bye")
        con.runAndWait()
        break
    con.say(s)
    con.runAndWait()
