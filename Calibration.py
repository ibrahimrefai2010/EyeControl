def tksleep(seconds):
    from PIL import ImageTk, Image
    import tkinter as tk
    
    ms = int(seconds * 1000)
    root = tk._get_default_root('sleep')
    var = tk.IntVar(root)
    root.after(ms, var.set, 1)
    root.wait_variable(var)

def Calibrate():
    from PIL import ImageTk, Image
    import tkinter as tk
    import main
    #ctk.set_appearance_mode('light')

    root = tk.Tk()
    root.title("EyeMouse calibration")
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    Instruction_label = tk.Label(root, text="Follow the Target with your eyes\n DO NOT move while using the app", font=("Arial", 40))
    Instruction_label.place(x=(root.winfo_screenwidth()/2 - 400), y = (root.winfo_screenheight() / 2 - 40), in_=root)

    tksleep(5) #stop for 5 seconds
    
    Instruction_label.destroy()

    image_path = "Target.png"
    img = Image.open(image_path)

    size = 120
    resized_img = img.resize((size, size))

    # Create a PhotoImage from the resized image
    photo_img = ImageTk.PhotoImage(resized_img)



    image_label = tk.Label(root, image=photo_img)
    image_label.place(x=10, y=10, in_=root)



    root.mainloop()
Calibrate()