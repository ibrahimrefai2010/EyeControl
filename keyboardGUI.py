def SetCurrentChar(_position):
    position = _position
    print(position)

def ShowKeyboard():
    import tkinter as tk
    window = tk.Tk()
    
    global Char
    Char = ''
    BtnDict = {}
    Keyboard = "abc0de1fgh2ij3kln4mo5pqr56tu7vwx78z9"
    for i in Keyboard:
        BtnDict.update({i : tk.Label(window, text=i)})
        BtnDict[i].pack()
        
    window.mainloop()