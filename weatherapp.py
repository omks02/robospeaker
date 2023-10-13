import requests
import json
import win32com.client as wincom
print("Hello ! This Is A Python based Weather Api --- Created by. - Om Kshirsagar")
city = input("Enter The Name Of City : \n")
url = f"http://api.weatherapi.com/v1/current.json?key=30c093580c284738a5752301231310&q={city}"

r = requests.get(url)
#print(r.text)
#print(type(r.text))

dic = json.loads(r.text)
w= dic['current']['temp_c']
c=dic['location']['country']
s=dic['location']['region']
print(w)
speak = wincom.Dispatch("SAPI.SpVoice")
text = (f"The Current weather temperature in {city} is {w} Which Is in Country {c} & In State Of {s}")
print(text)
speak.Speak(text)
print("We Have Used The Weather Api & Json For This Project")

