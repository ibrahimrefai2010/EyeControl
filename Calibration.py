import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode('dark')

root = ctk.CTk()
root.title("EyeMouse calibration")
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

image_path = "path/to/your/image.png"
img = ImageTk.PhotoImage(Image.open(image_path))

image_label = ctk.Label(root, image=img)

root.mainloop()