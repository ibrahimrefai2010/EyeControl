import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode('dark')

root = ctk.CTk()
root.title("EyeMouse calibration")
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))


root.mainloop()