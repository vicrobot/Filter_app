#! /usr/bin/env python3
#that above is python's path where it is installed;

import os
import sys
import inspect
from tkinter import *
from tkinter import font
#from PIL import ImageTk, Image
from functools import partial
#import shutil
from tkinter import messagebox as mb


img = ['.png','.jpg','.svg','.jpeg','.exif','.tiff','.gif','.bmp','.jfif','.ppm','.pgm','.pbm','.pnm','.webp','.heif','.bat','.bpg']
vid = ['.mp4','.mkv','.m4a', '.m4v', '.f4v', '.f4a', '.m4b', '.m4r', '.f4b', '.mov','.3gp', '.3gp2', '.3g2', '.3gpp','.3gpp2','.ogg','.oga','.ogv','.ogx','.wmv', '.wma', '.asf','.webm','.flv','.ts']
var = ""
flagoff = 0


def is_vid(st):
    for i in vid:
        if i in st: return True
    else: return False

def is_img(st):
    for i in img:
        if i in st: return True
    else: return False

def cutnpst(v1, v2, v3):
    os.rename(v2+'/'+v1,mkname(v3+'/'+v1))

def mkname(name):
    num = 0
    woo = name
    while os.path.exists(woo):
        num += 0
        woo = woo + str(num)
    return woo

class Not_A_Directory(BaseException): pass

def okay(e):
    global var, flagoff
    string = e.get()
    var = str(string).rstrip()
    if not os.path.isdir(var):
        try: raise Not_A_Directory
        except: mb.showinfo(title = 'Notice', message = 'Not A Directory   ')
        return
    foo()
    path1 = mkname(var+"/videos")
    path2 = mkname(var+"/images")
    os.mkdir(path1)
    os.mkdir(path2)
    for i in os.listdir(var):
        if os.path.isfile(var +'/'+ str(i)):
            if is_vid(i):
                cutnpst(i,var,path1)
            if is_img(i):
                cutnpst(i,var,path2)
    flagoff = 1

def foo():
    global b, b1
    b.destroy()
    b1.pack(side = 'bottom')
    b1.place()

def foo1():
    global flagoff
    if flagoff: sys.exit()

def info():
    helpstr = 'An Application for \nsorting out image \nand video files of \nspecified directory   '
    mb.showinfo(title = 'Notice', message = helpstr)

if __name__ == "__main__":

    root = Tk()                              # the main object
    root.title('Filter App')                 # the title
    v = inspect.getfile(inspect.currentframe()).partition('/run.py')
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=v[0] + '/Pictures/filter.png'))
    os.chdir('/')
    #img = ImageTk.PhotoImage(Image.open("images.png"))

    #font
    courier20 = font.Font(family="Courier",size=20,weight="bold")
    courier30 = font.Font(family="Courier",size=30,weight="bold")

    #Entry
    e = Entry(root,bg = '#9ce1e2',bd = 6, font = courier20)  # an Entry object
    e.pack()                                                             # set and display
    e.place()

    #Label
    L = Label(root, text="Give Path",fg = '#013e8e',font = courier30)
    L.pack( side = 'top')
    L.place()

    #help panel
    panel = Button(root, text = '?', command  = info,fg = '#6a7ad1',font = courier20 )
    panel.pack(side = 'right')

    #Button
    b = Button(root,text='OKAY',command=lambda arg = e: okay(arg), width = 15, height = 2,fg = '#6a7ad1',
    activeforeground = '#013e8e',font = courier20 ) # a button object
    b.pack(side = 'bottom')                                                  # set and display
    b.place()

    b1 = Button(root,text='DONE',command=foo1, width = 15, height = 2,fg = '#6a7ad1',
    activeforeground = '#013e8e',font = courier20 ) # a button object
    root.mainloop()
