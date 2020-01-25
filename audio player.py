##importing libraries
import pygame
import tkinter as tkr
import os
from tkinter import filedialog

## create window
player = tkr.Tk()

##editing player windows
player.title("Music Player")
player.geometry('300x700')

##pygame init
pygame.init()
pygame.mixer.init()

##volume controller
volumelevel = tkr.Scale(player,from_=0.0, to_=1.0, orient = tkr.HORIZONTAL, resolution = 0.1)


#action
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volumelevel.get())
    print(pygame.mixer.music.get_volume())
    print(volumelevel.get())
def ExitPlayer():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
def file_dialog():
    player.withdraw
    file_dir = filedialog.askdirectory(initialdir='/', title="Please select a directory")
    os.chdir(file_dir)
    songlist = os.listdir(file_dir)
    # for song in os.listdir(file_dir):
    #     if song.endswith("*.mp3"):
    #         songlist.extend(song)
    return songlist

# ##playlist register
# file_dir=r"C:\Users\Gaumati Khan\PycharmProjects\untitled\songs"
# os.chdir(file_dir)
# songlist = os.listdir(file_dir)


##playlist input
songlist = file_dialog()
playlist = tkr.Listbox(player, highlightcolor="Green", selectmode=tkr.SINGLE)
print(songlist)
pos = 0
for item in songlist:
    playlist.insert(pos, item)
    pos = pos+1



##song_name
# label1 = tkr.LabelFrame(player, text="Song Name")
# label1.pack(fill="both", expand="yes")
# contents1 = tkr.Label(label1, text=file)
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable = var)

##buttons
button1 = tkr.Button(player, width= 5, height =3, text="Play", command=play)
button2 = tkr.Button(player, width= 5, height =3, text="Stop", command=ExitPlayer)
button3 = tkr.Button(player, width= 5, height =3, text="Pause", command=pause)
button4 = tkr.Button(player, width= 5, height =3, text="Unpause", command=unpause)
button5 = tkr.Button(player, width= 5, height =3, text="Choose Directory", command=file_dialog)

##widgets
songtitle.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
button5.pack(fill="x")
volumelevel.pack(fill="x")
playlist.pack(fill="both",expand="yes")


##activate
tkr.mainloop()
