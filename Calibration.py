def tksleep(seconds):
    from PIL import ImageTk, Image
    import tkinter as tk
    
    ms = int(seconds * 1000)
    root = tk._get_default_root('sleep')
    var = tk.IntVar(root)
    root.after(ms, var.set, 1)
    root.wait_variable(var)
    
def get_screen_size():
  scr_width = root.winfo_screenwidth()
  scr_height = root.winfo_screenheight()
  print("Screen width:", scr_width, "Screen height:", scr_height)
  return (scr_width, scr_height)


def Calibrate():
    from PIL import ImageTk, Image
    import tkinter as tk
    import Tracker
    import ctypes
    import threading
    import keyboardGUI
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    global root
    root = tk.Tk()
    scr_width, scr_height = get_screen_size()
    root.title("EyeMouse calibration")
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    Instruction_label = tk.Label(root, text="Follow the Target with your eyes\n DO NOT reposition yourself while using the app", font=("Arial", 40))
    Instruction_label.place(x=(root.winfo_screenwidth() // 2 - 600), y=(root.winfo_screenheight() // 2 - 100), in_=root)

    tksleep(6)  # Stop for 6 seconds

    Instruction_label.destroy()

    image_path = "Target.png"
    img = Image.open(image_path)

    size = 120
    resized_img = img.resize((size, size))

    # Create a PhotoImage from the resized image
    photo_img = ImageTk.PhotoImage(resized_img)

    image_label = tk.Label(root, image=photo_img)
    image_label.place(x=(root.winfo_screenwidth() // 2 - size // 2), in_=root)

    tksleep(2)
    Tracker.store_Reading(1)
    tksleep(1)
    
    image_label.place(x=(root.winfo_screenwidth() // 2 - size // 2), y=(root.winfo_screenheight() - size), in_=root)
    
    tksleep(2)
    Tracker.store_Reading(2)
    tksleep(1)
    
    image_label.place(x=(scr_width - size), y=(scr_height // 2 - size // 2), in_=root)
    
    tksleep(2)
    Tracker.store_Reading(3)
    tksleep(1)
    
    image_label.place(x=0, y=(scr_height // 2 - size // 2), in_=root)
    
    tksleep(2)
    Tracker.store_Reading(4)
    tksleep(1)
    
    
    
    root.destroy()
    
    keyboardGUI.ShowKeyboard()
    Tracker.calibration = False




#Calibrate()