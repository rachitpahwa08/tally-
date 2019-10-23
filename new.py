
from tkinter import *
import os
import sys
import requests, re, time
from bs4 import BeautifulSoup
root= Tk() 
 
  
    # set the title of GUI window 
root.title("TALLY CONNECTOR | HOME") 
  
    # set the configuration of GUI window 
root.geometry("500x300")
canvas1 = Canvas(root, width = 500, height = 450)
canvas1.pack()


label1 = Label(root, text='License number: ')
canvas1.create_window(100, 100, window=label1)

entry1 = Entry (root)
canvas1.create_window(270, 100, window=entry1)
def run():
    r = requests.get('http://localhost:9002')
    r.status_code

def quit1():
    root.destroy()
      

def f():
    quit1()
    tally(b)
    run()
def values(): 
    global number
    number = float(entry1.get()) 
    
    if number == 123456:
       button = Button (root, text='Connect Tally',command=f,bg='yellow') 
       #label_button = tk.Label(root, text= button, bg='yellow')
       canvas1.create_window(270, 200, window=button)
    
    else:
       Submit = ("Incorrect lincense number")  
       label_Submit = Label(root, text= Submit, bg='yellow')
       canvas1.create_window(270, 200, window=label_Submit)


button1 = Button (root, text='Submit',command=values, bg='orange') # button to call the 'values' command above 
canvas1.create_window(270, 150, window=button1)


def tally(b):
    b=None

      
    #os.system('tally.py')
heading = Label(root, text="TALLY CONNECTION", bg="lightgrey", pady="10" ,  width=20,font =('Verdana', 20))
heading.pack(fill=X, pady=10,padx=15)


name = Label(root, text="Your result is: Please start Tally at port 9002.", bg="lightgrey", pady="10", width=20,font =('Verdana', 10))
name.pack(fill=X, pady=5,padx=5)


frame = Frame(root)
frame.pack()

button = Button(frame, 
                   text="Get transactions data.", bg="blue",pady="10",padx="10",
                   fg="white",
                   command=run_function_quit1)
button.pack(side=LEFT,fill=X, pady=5,padx=5)
slogan = Button(frame,
                   text="Get site status.",bg="blue",fg="white",pady="10",padx="10",
                   command=run1_function1_quit1)
slogan.pack(side=LEFT,fill=X, pady=5,padx=5)


button1 = Button(root, text='Back to home', command=main_quit1 ,font =('Verdana', 10))
button1.pack(side=LEFT,fill=X,padx=10)


root.mainloop()
