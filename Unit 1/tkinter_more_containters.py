import tkinter as tk

# **** Create Window ****
root = tk.Tk()
root.geometry("300x200")
root.title("Contact Details")

# **** Add window content ****

# ** adding frames **
# both the red and the yellow frame go inside the root window
red_frame = tk.Frame(root)
red_frame.grid(row=0,column=0)

yellow_frame = tk.Frame(root)
yellow_frame.grid(row=1,column=0)

# the blue, purple and grey frames go inside the yellow frame
blue_frame = tk.LabelFrame(yellow_frame, text="Personal")
blue_frame.grid(row=0,column=0) # note: each frame has its own grid

purple_frame = tk.LabelFrame(yellow_frame, text="Phone")
purple_frame.grid(row=0,column=1)

grey_frame = tk.LabelFrame(yellow_frame,text="email")
grey_frame.grid(row=1,column=0,columnspan=2)

#*** adding labels
tk.Label(red_frame, text="Contact Details").pack()

tk.Label(blue_frame, text="First name").grid(row=0,column=0)
tk.Label(blue_frame, text="Michelle").grid(row=0,column=1)
tk.Label(blue_frame, text="Last name").grid(row=1,column=0)
tk.Label(blue_frame, text="Davis").grid(row=1,column=1)
tk.Label(blue_frame, text="Birthday").grid(row=2,column=0)
tk.Label(blue_frame, text="12/03/82").grid(row=2,column=1)

tk.Label(purple_frame, text="Home").grid(row=0,column=0)
tk.Label(purple_frame, text="07 3452 8915").grid(row=0,column=1)
tk.Label(purple_frame, text="Mobile").grid(row=1,column=0)
tk.Label(purple_frame, text="0423 861").grid(row=1,column=1)
tk.Label(purple_frame, text="Fax").grid(row=2,column=0)
tk.Label(purple_frame, text="").grid(row=2,column=1)

tk.Label(grey_frame, text="michelle_davis@gmail.com").pack()

# **** Run window loop ****
root.mainloop()