from tkinter import *
from tkinter import ttk
import fselect


#UI Start here
root = Tk()
label = ttk.Label(root, text = "Hello")
label.pack()
button = ttk.Button(root)
button.pack()
logo = PhotoImage(file ="E:\\Projects\\Minor Project\\data\\bt_select.png")
button.config(image = logo)
entry = ttk.Entry(root, width = 50)
entry.pack()
button.config(command = fselect.fst)
entry.insert(0, 'none')
entry.state(['readonly'])

root.mainloop()
