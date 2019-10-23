from tkinter import *
import os
import sys
import requests, re, time
import tally

def perfromTallyConnector():
    # create a GUI window 
    root = Tk()

    # set the background colour o
    #f GUI window 
    root.configure(background='BLACK') 
  
        # set the title of GUI window 
    root.title("TALLY CONNECTOR | HOME") 
  
        # set the configuration of GUI window 
    root.geometry("500x300")

    url = 'http://localhost:9002'
    payload = {'some': 'data'}
    headers = {'content-type': 'text/plain'}
  
    def run():
        tally.performTally()
    
    
    def quit1():
        root.destroy()

    def function():
        r = requests.get('http://localhost:9002')
        r.status_code 

    def run_function_quit1():
        quit1()
        function()
        run()
   

    heading = Label(root, text="TALLY CONNECTION", bg="lightgrey", pady="10" , width=20,
                    font =('Verdana', 15))
    heading.pack(fill=X, pady=10,padx=15)

    button = Button(root, text='Connect Tally', width=20,pady="10", command = run_function_quit1,
                    font =('Verdana', 15))
    #button = Button(root,command = quit1)
    #button.configure(command=run_quit)
    button.pack()


    root.mainloop()

