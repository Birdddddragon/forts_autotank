from tkinter import *


root = Tk()

image = PhotoImage(file="SCR1.PNG")

root.wait_visibility(root)
root.wm_attributes("-fullscreen", 1)
root.wm_attributes("-transparentcolor", root['bg'])

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, width=root.winfo_width(), height=root.winfo_height())
canvas.pack()
canvas.create_image(850, 700, anchor=NW, image=image)

root.mainloop()
