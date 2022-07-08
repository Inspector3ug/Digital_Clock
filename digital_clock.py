from tkinter import *
from time import strftime

root = Tk()
root.call('wm', 'attributes', '.', '-topmost', '1')
root.geometry("285x60")
root.resizable(0,0)
root.title('Python Digital Clock')
def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)
mark = Label(root, 
            font = ('calibri', 36, 'bold'),
            pady=150,
            foreground = 'black')
mark.pack(anchor = 'center')
time()
 
mainloop() 