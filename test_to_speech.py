import tkinter as tk
from gtts import gTTS
import os
from pygame import mixer 
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root,width=40) 
canvas1.create_window(200, 30, window=entry1)

def texttospeech ():  
    x1 = entry1.get()
    language = 'en'
    myobj = gTTS(text=x1, lang=language, slow=False) 
    myobj.save("welcome.mp3")
     
    mixer.init()
    mixer.music.load('wellcome.mp3')
    mixer.music.play()
    
    label1 = tk.Label(root, text= x1)
    canvas1.create_window(200, 100, window=label1)
    
button1 = tk.Button(text='Click to read the given text', command=texttospeech)
canvas1.create_window(200, 70, window=button1)

root.mainloop()