from tkinter import *
import os

oracleLocation=os.path.abspath(__file__).replace('main.py','Oracle12c/sqlplus.exe')

def runOracle():
    os.startfile(oracleLocation)

root = Tk()
text = Text(root)
text.pack()
runOracle()
root.mainloop()