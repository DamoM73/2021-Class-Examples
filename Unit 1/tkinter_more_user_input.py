import tkinter as tk

def submit_values():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    birthday = birthday_entry.get()
    home_phone = home_phone_entry.get()
    mobile_phone = mobile_phone_entry.get()
    fax_number = fax_number_entry.get()
    email = email_entry.get()

    print(f"{first_name} {last_name}, born {birthday}")
    print(f"Home: {home_phone} Mobile: {mobile_phone} Fax: {fax_number}")
    print(f"Email: {email}")

# **** Create Window ****
root = tk.Tk()
root.geometry("400x200")
root.title("Contact Details")

# **** Add window content ****

# ** adding frames **
# both the red and the yellow frame go inside the root window
red_frame = tk.Frame(root)
red_frame.grid(row=0,column=0)

yellow_frame = tk.Frame(root)
yellow_frame.grid(row=1,column=0)

green_frame = tk.Frame(root)
green_frame.grid(row=2,column=0)

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
first_name_entry = tk.Entry(blue_frame)
first_name_entry.grid(row=0,column=1)

tk.Label(blue_frame, text="Last name").grid(row=1,column=0)
last_name_entry = tk.Entry(blue_frame)
last_name_entry.grid(row=1,column=1)

tk.Label(blue_frame, text="Birthday").grid(row=2,column=0)
birthday_entry = tk.Entry(blue_frame)
birthday_entry.grid(row=2,column=1)

tk.Label(purple_frame, text="Home").grid(row=0,column=0)
home_phone_entry = tk.Entry(purple_frame)
home_phone_entry.grid(row=0,column=1)

tk.Label(purple_frame, text="Mobile").grid(row=1,column=0)
mobile_phone_entry = tk.Entry(purple_frame)
mobile_phone_entry.grid(row=1,column=1)

tk.Label(purple_frame, text="Fax").grid(row=2,column=0)
fax_number_entry = tk.Entry(purple_frame)
fax_number_entry.grid(row=2,column=1)

email_entry = tk.Entry(grey_frame)
email_entry.pack()

tk.Button(green_frame, text="Submit", command=submit_values).pack()

# **** Run window loop ****
root.mainloop()