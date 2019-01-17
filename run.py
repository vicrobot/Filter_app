import os
import sys
from tkinter import *
from tkinter import font
from functools import partial
import shutil


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
        except: print('Not A Directory')
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

if __name__ == "__main__":

    root = Tk()                              # the main object
    root.title('Filter App')                 # the title

    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='june.png'))
    os.chdir('/')


    #font
    helv36 = font.Font(family="Helvetica",size=20,weight="bold")
    helv37 = font.Font(family="Sans_monospace",size=30,weight="normal")

    #Entry
    e = Entry(root,bg = '#9ce1e2',bd = 6, font = helv36)  # an Entry object
    e.pack()                                                             # set and display
    e.place()

    #Label
    L = Label(root, text="Give Path",fg = '#013e8e',font = helv37)
    L.pack( side = 'top')
    L.place()

    #Button
    b = Button(root,text='OKAY',command=lambda arg = e: okay(arg), width = 15, height = 2,fg = '#6a7ad1',
    activeforeground = '#013e8e',font =helv36 ) # a button object
    b.pack(side = 'bottom')                                                  # set and display
    b.place()

    b1 = Button(root,text='DONE',command=foo1, width = 15, height = 2,fg = '#6a7ad1',
    activeforeground = '#013e8e',font =helv36 ) # a button object
    root.mainloop()
