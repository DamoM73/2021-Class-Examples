import tkinter as tk

# **** Create window ****
root = tk.Tk()
root.geometry("300x200")
root.title("Introduction Activity 2")

# **** Create window conent ****
top_left = tk.Label(text="O")
top_left.grid(row=0,column=0)

top_centre = tk.Label(text="X")
top_centre.grid(row=0,column=1)

top_right = tk.Label(text="O")
top_right.grid(row=0,column=2)

middle_left = tk.Label(text="X")
middle_left.grid(row=1,column=0)

middle_centre = tk.Label(text="X")
middle_centre.grid(row=1,column=1)

middle_right = tk.Label(text="O")
middle_right.grid(row=1,column=2)

bottom_left = tk.Label(text="X")
bottom_left.grid(row=2,column=0)

bottom_centre = tk.Label(text="O")
bottom_centre.grid(row=2,column=1)

bottom_right = tk.Label(text="X")
bottom_right.grid(row=2,column=2)

# **** Run window loop ****
root.mainloop()