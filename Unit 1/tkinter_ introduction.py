import tkinter as tk

# **** Create window ****
root = tk.Tk()
root.geometry("300x200")
root.title("Introduction Activity 1")

# **** Add window content ****
label_one = tk.Label(root, text="Damien Murtagh")
label_one.pack()

label_two = tk.Label(root, text="Ancient")
label_two.pack()

label_three = tk.Label(root, text="None")
label_three.pack()

# **** Run window loop ****
root.mainloop()