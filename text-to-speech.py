

from tkinter import *
from ttkthemes import themed_tk as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
import playsound
import random
from gtts import gTTS
import os
# root window
root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")
root.resizable(0,0)
root.configure(background="white")
root.title("Text To Speak")
# functions
def speak():
    audio_string = text.get(1.0,END)
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,1000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)
def save_audio():
    audio_string = text.get(1.0,END)
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,1000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    showinfo("python says","audio is saved as "+ str(audio_file))

# root widgets
text = scrolledtext.ScrolledText(root,width=30,height=10,wrap=WORD,padx=10,pady=10,borderwidth=5,relief=RIDGE)
text.grid(row=0,columnspan=3)
#buttons
listen_btn = ttk.Button(root,text="Listen",width=7,command=speak).grid(row=2,column=0,ipadx=2)
clear_btn = ttk.Button(root,text="Clear",width=7,command=lambda:text.delete(1.0,END))
clear_btn.grid(row=2,column=1,ipadx=2)
save_btn = ttk.Button(root,text="Save",width=7,command=save_audio).grid(row=2,column=2,ipadx=2)

root.mainloop()