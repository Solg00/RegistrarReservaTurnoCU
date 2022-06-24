"""HELLO BUDDY! You might use this module to run some tests or leave comments for your fellow Programmers to see"""
from struct import pack
from textwrap import fill
from tkinter import *
from tkinter import ttk

root = Tk()

def clear_window():
    '''Destroy elements of a frame'''
    for widget in ws.winfo_children():
        widget.destroy()
def openwin():
    clear_window()
    L = Label(ws,text='Hey world')
    L2 = Label(ws,text='BYE BYE')
    L.grid(row=0,column=0)
    L2.grid(row=0,column=1)

ws = Frame(root)
ws.pack()
L = Label(ws,text='1')
L2 = Label(ws,text='2')
sp = ttk.Separator(ws, orient=HORIZONTAL)
sp.grid(row=1,columnspan=2,sticky='ew') #Stick from east to west
L.grid(row=0,column=0)
L2.grid(row=0,column=1)


root.mainloop()