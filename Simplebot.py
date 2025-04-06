import pyttsx3,speech_recognition as Sr,webbrowser as wb,wikipedia as wk


def spTxt():
    recog = Sr.Recognizer()
    with Sr.Microphone() as source:
        print("Listening!")
        recog.adjust_for_ambient_noise(source)
        audio = recog.listen(source)
        try:
            data = recog.recognize_google(audio)
            print(data)
            return data
        except Sr.UnknownValueError:
            return "again"


def speak(txt):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    engine.setProperty("volume",.8)
    engine.setProperty("rate",180)

    engine.say(txt)
    engine.runAndWait()

k = spTxt()



if __name__ == '__main__':
 
    if "friday" in k.lower():
        speak("Yes boss")
        z = spTxt().lower()
        if z == 'search website':
            speak("what do you want to search")
            toSearch = spTxt()
            if toSearch != 'again':
                    
                wb.open(f"https://www.google.com/search?q={toSearch}")
            else:
                speak("please run the code again")
        elif z == 'info':
            wk.set_lang('en')
            speak("what do you want to know about")
            toKnow = spTxt()
            if toKnow != 'again':
                result = wk.summary(toKnow)
                print(result)
                speak(result)
             
        else:
          speak("please run the code again")
       

    else:
        speak("please run the code again")


