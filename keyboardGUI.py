def SetCurrentChar(position):
    Char = position

def ShowKeyboard():
    import tkinter as tk
    import Tracker
    window = tk.Tk()
    
    global Char
    Char = ''
    BtnDict = {}
    Keyboard = "abc0de1fgh2ij3kln4mo5pqr56tu7vwx78z9"
    for i in Keyboard:
        BtnDict.update({i : tk.Label(window, text=i)})
        BtnDict[i].pack()
        
    window.mainloop()