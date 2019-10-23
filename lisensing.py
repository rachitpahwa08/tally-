import tkinter as tk
import os
import sys
import requests, re, time
from bs4 import BeautifulSoup
root= tk.Tk()

 
  
    # set the title of GUI window 
root.title("TALLY CONNECTOR | HOME") 
  
    # set the configuration of GUI window 
root.geometry("500x300")
canvas1 = tk.Canvas(root, width = 500, height = 450)
canvas1.pack()


label1 = tk.Label(root, text='License number: ')
canvas1.create_window(100, 100, window=label1)

entry1 = tk.Entry (root)
canvas1.create_window(270, 100, window=entry1)
def run():
    r = requests.get('http://localhost:9002')
    r.status_code 
def ru():
    os.system('tally.py')
def quit1():
    root.destroy()
def f():
    quit1()
    ru()
    run()
def cron():
    os.system('cron_dy.py')

def s():
    quit1()
    cron()

def values(): 
    global number
    number = float(entry1.get()) 
    
    if number == 123456:
       button = tk.Button (root, text='Connect Tally',command=f,bg='yellow') 
       #label_button = tk.Label(root, text= button, bg='yellow')
       canvas1.create_window(200, 200, window=button)
       button1 = tk.Button(root, text='Schedule time',command=s,bg='yellow')
       canvas1.create_window(300, 200, window=button1)
    
    else:
       Submit = ("Incorrect lincense number")  
       label_Submit = tk.Label(root, text= Submit, bg='yellow')
       canvas1.create_window(270, 200, window=label_Submit)


button1 = tk.Button (root, text='Submit',command=values, bg='orange') # button to call the 'values' command above 
canvas1.create_window(270, 150, window=button1)
 

root.mainloop()
