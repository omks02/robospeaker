import win32com.client as wincom 

print("Hello ! This Is A Python based Robo-Speaker --- Created by. - Om Kshirsagar")

while True:
    text = input("Enter What You Want To Speak :")
    if "q" in text:
        speak = wincom.Dispatch("SAPI.SpVoice")
        text=("Bye Bye Friend ! ")
        speak.Speak(text)
        print("Bye Bye Friend ! ")
        break
    speak = wincom.Dispatch("SAPI.SpVoice")
    speak.Speak(text)
    