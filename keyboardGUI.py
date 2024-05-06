def SetCurrentChar(_Char):
    global BtnDict, Char
    print(f"called: {_Char}")
    BtnDict[_Char].configure(bg='blue')
    BtnDict[Char].configure(bg='white')
    Char = _Char

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
        BtnDict.update({Keyboard[i] : tk.Label(window, text=Keyboard[i], font=("Arial", 10))})
        BtnDict[Keyboard[i]].pack()
    
    window.mainloop()