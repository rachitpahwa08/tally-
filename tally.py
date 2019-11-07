  
from tkinter import *
import os
import sys
from stock_summary import perfromStock_Summary
from stock_transaction import performStockTransaction
import requests
from tkinter import messagebox
#from TallyConnector import perfromTallyConnector
#import summary,stock_summary,transaction,stock_transaction,TallyConnector
# create a GUI window 
def performTally():
    root = Tk() 

 
    # set the background colour of GUI window 
    root.configure(background='BLACK') 
  
    # set the title of GUI window 
    root.title("TALLY CONNECTOR | HOME") 
  
    # set the configuration of GUI window 
    root.geometry("500x300") 

    
    def checkConnection():
       try:
            r = requests.get('http://localhost:9002')
            return r.status_code
       except:
           return 0
    def quit1():
        root.destroy()

    def function():
        print(perfromStock_Summary())
        messagebox.showinfo("Success", "File Uploaded to cloud")

  
    def function1():
        print(performStockTransaction())
        messagebox.showinfo("Success", "File Uploaded to cloud")

    def main():
        perfromTallyConnector()
    
    def run_function_quit1():
        #quit1()
        function()
        #performTally()
        #run()

    def run1_function1_quit1():
        #quit1()
        function1()
        #performTally()
        #run()
     
    def main_quit1():
        quit1()
        main()
        # fot heading
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
            performTally()
    
    
        def quit1():
            root.destroy() 

        def run_function_quit1():
            quit1()
            #function()
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

    heading = Label(root, text="TALLY CONNECTION", bg="lightgrey", pady="10" ,  width=20,font =( 'Verdana', 20))
    heading.pack(fill=X, pady=10,padx=15)


    if(checkConnection()==200):
        name = Label(root, text="Your result is: Tally is successfully connected to port 9002.", bg="lightgrey", pady="10", width=20,font =( 'Verdana', 10))
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


        button1 = Button(root, text='Back to home', command=main_quit1,font =('Verdana', 10))
        button1.pack(side=LEFT,fill=X,padx=10)

        root.mainloop()
    else:
        name = Label(root, text="Your result is: Please start Tally at port 9002.", bg="lightgrey", pady="10", width=20,font =( 'Verdana', 10))
        name.pack(fill=X, pady=5,padx=5)

        frame = Frame(root)
        frame.pack()

        button = Button(frame, 
                           text="Get transactions data.", bg="blue",pady="10",padx="10",
                           fg="white",
                           command=run_function_quit1)
        button.pack(side=LEFT,fill=X, pady=5,padx=5)
        button["state"]="disabled"
        slogan = Button(frame,
                           text="Get site status.",bg="blue",fg="white",pady="10",padx="10",
                           command=run1_function1_quit1)
        slogan.pack(side=LEFT,fill=X, pady=5,padx=5)


        button1 = Button(root, text='Back to home', command=main_quit1,font =('Verdana', 10))
        button1.pack(side=LEFT,fill=X,padx=10)
        slogan["state"]="disabled"

        root.mainloop()

