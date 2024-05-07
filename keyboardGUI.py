def SetCurrentChar(_Char):
    try:
        global BtnDict, Char
        print(f"called: {_Char}")
        BtnDict[_Char].configure(bg='blue')
        BtnDict[Char].configure(bg='white')
        Char = _Char
    except Exception:
        print(Exception)


def ShowKeyboard():
    import tkinter as tk
    window = tk.Tk()
    
    global Char, BtnDict
    Char = 'a'
    BtnDict = {}
    KeyboardStr = "abc0de1fgh2ij3kln4mo5pqr56tu7vwx78z9"
    Keyboard = ["delete", "enter", "backspace"]
    
    for i in KeyboardStr:
        Keyboard.append(i)
    
    
    for i in Keyboard:
        BtnDict.update({i : tk.Label(window, text=i, font=("Arial", 10))})
        BtnDict[i].pack()
        
    print(f"data: {BtnDict} {Keyboard}")
    window.mainloop()