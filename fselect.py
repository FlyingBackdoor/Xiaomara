import tkinter as tk
from tkinter import filedialog
import hashlib
import os
import db_handler

#clear function
clear = lambda: os.system('cls')

def save_data_in_disk(md5):
    file = open("data//temp", mode='w+')
    file.write(md5)
    file.seek(0)
    file.close()

def fst():
    clear()
    root = tk.Tk()
    root.withdraw()
    file_loc = filedialog.askopenfilename()
    print("File dir: " +file_loc)
    md5code = hashlib.md5(open(file_loc, 'rb').read()).hexdigest()
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

def get_data():
    file = open("data//temp", mode='r')
    md5 = str(file.read())
    return md5

#fst()
#save_data_in_disk('c')
#print(get_data())
#db_handler.showData()
