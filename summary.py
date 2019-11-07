from tkinter import *
import os
import sys

def performSummary():
    # create a GUI window 
    root = Tk()

    # set the background colour of GUI window 
    root.configure(background='BLACK') 
  
        # set the title of GUI window 
    root.title("TALLY CONNECTOR | HOME") 
  
        # set the configuration of GUI window 
    root.geometry("500x300") 
  
    def run():
        performTally()

    def quit1():
        root.destroy()
    def run_quit1():
        quit1()
        run()

    heading = Label(root, text="Site Status", bg="lightgrey", pady="10" , width=20,font =('Verdana', 15))
    heading.pack(fill=X, pady=10,padx=15)
    #when connection will establish
    name = Label(root, text="Data is saved ", bg="lightblue", pady="10" , width=20,font =('Verdana', 15))
    name.pack(fill=X, pady=10,padx=15)
    button = Button(root, text='Go back',pady="5", command = run_quit1 ,font =('Verdana', 15))
    #button = Button(root,command = quit1)
    #button.configure(command=run_quit)
    button.pack(side=LEFT,fill=X, pady=5,padx=5)


    root.mainloop()
