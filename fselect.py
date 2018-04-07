import tkinter as tk
from tkinter import filedialog
import hashlib
import os
from colorama import Fore
import db_handler

#clear function
clear = lambda: os.system('cls')

def fst():
    clear()
    root = tk.Tk()
    root.withdraw()
    file_loc = filedialog.askopenfilename()
    print("File dir: " +file_loc)
    md5code = hashlib.md5(open(file_loc, 'rb').read()).hexdigest()
    print("MD5 " +md5code)
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

#fst()
#db_handler.showData()
