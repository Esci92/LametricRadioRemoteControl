import requests
import json
import time
from tkinter import Tk
from tkinter import Button
from tkinter import PhotoImage
from tkinter import messagebox

headersaut = 'Basic "Your API Lametric Token"'
IP = "Your IP Address" 
port = ":8080"
radiowidget = IP + port + "/api/v2/device/apps/com.lametric.radio/widgets/589ed1b3fcdaa5180bf4848e55ba8061/actions"
audiocontrol = IP + port + "/api/v2/device/audio"

top = Tk()
top.geometry("167x112")


def Play():
    payload = {'id': "radio.play"}
    headers = {'Authorization': headersaut}
    requests.post(radiowidget, json=payload, headers=headers)


def Stop():
    payload = {'id': "radio.stop"}
    headers = {'Authorization': headersaut}
    requests.post(radiowidget, json=payload, headers=headers)


def Next():
    payload = {'id': "radio.next"}
    headers = {'Authorization': headersaut}
    requests.post(radiowidget, json=payload, headers=headers)


def Prev():
    payload = {'id': "radio.prev"}
    headers = {'Authorization': headersaut}
    requests.post(radiowidget, json=payload, headers=headers)


def Plus():
    headers = {'Authorization': headersaut}
    r = requests.get(audiocontrol, headers=headers)
    getVolume = (r.text)
    oldVolume= getVolume[-4] + getVolume[-3]
    newVolume = int(oldVolume) + 5
    if (newVolume > 100 ):
        newVolume = 100
    newVolume = str(newVolume)
    payload = {'volume': newVolume}
    requests.put(audiocontrol, json=payload, headers=headers)

def Minus():
    headers = {'Authorization': headersaut}
    r = requests.get(audiocontrol, headers=headers)
    getVolume = (r.text)
    oldVolume= getVolume[-4] + getVolume[-3]
    newVolume = int(oldVolume) - 5
    if (newVolume < 0 ):
        newVolume = 0
    newVolume = str(newVolume)
    payload = {'volume': newVolume}
    requests.put(audiocontrol, json=payload, headers=headers)



playB = Button(top, text="Play", command=Play)
stopB = Button(top, text="Stop", command=Stop)
nextB = Button(top, text="Next", command=Next)
prevB = Button(top, text="Prev", command=Prev)
AudipB = Button(top, text="+", command=Plus)
AudimB = Button(top, text="-", command=Minus)


photosAudipB = PhotoImage(file="plus.png")
AudipB.config(image=photosAudipB, width="50", height="50")
AudipB.grid(row=0, column=2)

photosAudimB = PhotoImage(file="minus.png")
AudimB.config(image=photosAudimB, width="50", height="50")
AudimB.grid(row=0, column=0)

photostopB = PhotoImage(file="stop.png")
stopB.config(image=photostopB, width="50", height="50")
stopB.grid(row=0, column=1)

photoprevB = PhotoImage(file="prev.png")
prevB.config(image=photoprevB, width="50", height="50")
prevB.grid(row=1, column=0)

photoplayB = PhotoImage(file="play.png")
playB.config(image=photoplayB, width="50", height="50")
playB.grid(row=1, column=1)

photonextB = PhotoImage(file="next.png")
nextB.config(image=photonextB, width="50", height="50")
nextB.grid(row=1, column=2)

top.mainloop()

//by Christian Escolano