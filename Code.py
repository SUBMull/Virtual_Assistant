import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pw
import wikipedia as w

ear = sr.Recognizer()
Machine = pt.init()
voices = Machine.getProperty('voices')
Machine.setProperty('voice', voices[1].id)


def respond(talk):
    Machine.say(talk)
    Machine.runAndWait()


def commands():
    try:
        with sr.Microphone() as main_source:
            print('How can I help?')
            voice = ear.listen(main_source)
            command = ear.recognize_google(voice)
            command = command.lower()
            if 'meme' in command:
                command = command.replace('meme', '')
                print(command)
    except:
        pass
    return command


def run():
    command = commands()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        respond('playing ' + song)
        pw.playonyt(song)
    elif 'what' in command:
        Data = command.replace('what', '')
        Information = w.summary(Data, 1)
        print(Information)
        respond(Information)

    else:
        respond('I could not hear you, please say the command again.')

while True:
    run()
