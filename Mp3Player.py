from tkinter import *
from pygame import mixer
from tkinter import filedialog
import os
import tkinter.messagebox

from tkinter.filedialog import askopenfilename,asksaveasfilename 
from mutagen.mp3 import MP3

root=Tk()
root.geometry('400x420')
root.title('Mp3player')
# root.config(bg='#000')
root.resizable(False,False)
root.iconbitmap('m.ico')

menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar)


top=PhotoImage(file='a.png')
top_img=Label(root,image=top)
top_img.place(x=100,y=10)

mixer.init()

#%%
def Open():
    global filename
    filename=askopenfilename()

# create the file_menu
file_menu = Menu(menubar,tearoff=0)
file_menu.add_command(label='Open',command=Open)
file_menu.add_command(label='Exit',command=root.destroy)
menubar.add_cascade(label="File",menu=file_menu)

#%%

def show_details():
    music_name["text"]="Playing music" +' - '+os.path.basename(filename)
    filedata=os.path.splitext(filename)
    
    if filedata[1] == '.mp3':
        audio = MP3(filename)
        total_length = audio.info.length
    mins,secs = divmod(total_length,60)
    mins = round(mins)
    secs = round(secs)
    timeformat = "{:02d}:{:02d}".format(mins,secs)
    music_lenght["text"]="Total Length" + '  -  ' + timeformat

music_name=Label(root,bg='#fff',width=50).place(x=100,y=180)
music_length=Label(root,bg='orange',width=50).place(x=100,y=220)

        
#%%        
        
def playmusic():
    global paused
    if paused:
        mixer.music.unpause()
        statusbar['text']='Resume Music'
        paused=FALSE
    else:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text']="Playing music" +' - '+os.path.basename(filename)
            print(filename)
            show_details()
        except:
            tkinter.messagebox.showerror("Error",'File not found')

#Create play button
play_img=PhotoImage(file='p.png')
play_button=Button(root,image=play_img,command=playmusic)
play_button.place(x=130,y=250)

#%%

def stopmusic():
    mixer.music.stop()
    statusbar['text']='Stop Music'

#Create Stop button
stop_img=PhotoImage(file='s.png')
stop_button=Button(root,image=stop_img,command=stopmusic) 
stop_button.place(x=200,y=250)



#%%
paused= FALSE
def pause_music():
    global paused
    paused=True
    mixer.music.pause()
    statusbar['text']='Pause Music'
    
#Create pause button
pause_img=PhotoImage(file='p1.png')
pause_button=Button(root,image=pause_img,command=pause_music)
pause_button.place(x=58,y=250)

#%%
def rewind_music():
    playmusic()
    statusbar['text']='Rewind Music'

#Create rewind button
rewind_img=PhotoImage(file='r.png')
rewind_button=Button(root,image=rewind_img,command=rewind_music)
rewind_button.place(x=270,y=250)



#%%
muted=FALSE
def mutemusic():
    global muted
    if muted:
        mixer.music.set_volume(0.7)
        volumebtn.configure(image=volumephoto)
        scale.set(70)
        muted=FALSE
    else:
        mixer.music.set_volume(0)
        volumebtn.configure(image=mutephoto)
        scale.set(0)
        muted=TRUE

mutephoto=PhotoImage(file='m2.png')
volumephoto=PhotoImage(file='v.png')
volumebtn=Button(root,image=volumephoto,command=mutemusic)
volumebtn.place(x=180,y=330)

#%%

def set_vol(val):
    volume=int(val)/100

scale=Scale(root,from_=0,to=100,orient=HORIZONTAL,bd=0,command=set_vol)
scale.set(60)
scale.place(x=240,y=330)


statusbar=Label(root,text="Welcome to Music Player",fg='#fff',relief='solid',anchor=W).pack(side=BOTTOM,fill=X)

root.mainloop()

