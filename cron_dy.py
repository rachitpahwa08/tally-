from tkinter import * 
import csv
import os
import sys
import requests, re, time
from tally import performTally

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master=master
        self.pack()
        self.output()
    
    def output(self):
        Label(text='Hour:').pack(side=LEFT,padx=5,pady=5)
        self.e = Entry(self.master, width=10)
        self.e.pack(side=LEFT,padx=5,pady=5)

        Label(text='Minutes:').pack(side=LEFT,padx=5,pady=5)
        self.a = Entry(self.master, width=10)
        self.a.pack(side=LEFT,padx=5,pady=5)

        self.b = Button(self.master, text='Submit', command=self.writeToFile,bg='orange')
        self.b.pack(side=RIGHT,padx=5,pady=5)

        self.c = Button(self.master, text='Connect tally', command=self.back,bg='yellow')
        self.c.pack(side=RIGHT,padx=15,pady=15)

    def writeToFile(self):
        with open('cron.csv', 'r+') as f:
            f.truncate()
            w=csv.writer(f, quoting=csv.QUOTE_ALL)
            s=self.e.get()+","+self.a.get()
            w.writerow([s])

    
    def quit1(self):
        self.master.destroy()
    def run(self):
        r = requests.get('http://localhost:9002')
        r.status_code
    def back(self):
        self.quit1()
        tally()
        self.run()


def tally():
    performTally()

 



def performCron_dy():
    root=Tk()
    root.title('Tally|cron')
    root.geometry('500x100')
    app=App(master=root)
    app.mainloop()
    root.mainloop()
