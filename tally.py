from tkinter import *
import os
import sys
# create a GUI window 
root = Tk() 

 
    # set the background colour of GUI window 
root.configure(background='BLACK') 
  
    # set the title of GUI window 
root.title("TALLY CONNECTOR | HOME") 
  
    # set the configuration of GUI window 
root.geometry("500x300") 

def run():
    os.system('summary.py')
  
def quit1():
    root.destroy()

def function():
    os.system('stock_summary.py')

def run1():
    os.system('transaction.py')
  
def function1():
    os.system('stock_transaction.py')

def main():
    os.system('TallyConnector.py')
    
def run_function_quit1():
     quit1()
     function()
     run()

def run1_function1_quit1():
     quit1()
     function1()
     run()
     
def main_quit1():
     quit1()
     main()
       # fot heading
heading = Label(root, text="TALLY CONNECTION", bg="lightgrey", pady="10" ,  width=20,font =( 
  'Verdana', 20))
heading.pack(fill=X, pady=10,padx=15)


name = Label(root, text="Your result is: Please start Tally at port 9002.", bg="lightgrey", pady="10", width=20,font =( 
  'Verdana', 10))
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


button1 = Button(root, text='Back to home', command=main_quit1

                 ,font =( 
  'Verdana', 10))
button1.pack(side=LEFT,fill=X,padx=10)

root.mainloop()

     

