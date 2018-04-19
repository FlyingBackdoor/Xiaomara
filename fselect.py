import tkinter as tk
from tkinter import filedialog
from hashlib import md5
from os import system
import db_handler

#clear function
clear = lambda: system('cls')

#My solution for saving md5 code as a file to use it for other purpose.
def save_data_in_disk(md5):
    file = open("data//temp", mode='w+')
    file.write(md5)
    file.seek(0)
    file.close()

#Select file dynamically using tkinter filedialog
def fst():
    clear()
    root = tk.Tk()
    root.withdraw()
    file_loc = filedialog.askopenfilename()
    print("File dir: " +file_loc)
    md5code = md5(open(file_loc, 'rb').read()).hexdigest()
    print("MD5 " +md5code)
    save_data_in_disk(md5code)
    foo = db_handler.search(md5code)
    if foo is True:
        pass
    else:
        kwd = input('Do you want to save in Database (y/n) : ')
        if kwd is 'y' or kwd is 'Y':
            db_handler.insrtIntoDB(md5code, file_loc)
        else:
            pass
    return str(md5code)

#read md5 code from local file.
def get_data():
    file = open("data//temp", mode='r')
    md5 = str(file.read())
    return md5

#fst()
#save_data_in_disk('c')
#print(get_data())
#db_handler.showData()
