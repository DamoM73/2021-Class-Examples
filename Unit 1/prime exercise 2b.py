import tkinter as tk

def is_prime(candidate):
    # determines if candidate is a prime number
    dividend = 2
    while True:
        if candidate % dividend == 0:
            return False
        elif candidate - dividend == 1:
            return True
        else:
            dividend += 1

def find_next_prime(start):
    # looks for the next prime

    if start < 3:
        next_num = 3
    else:
        next_num = start

    while True:
        if is_prime(next_num):
            return next_num
        else:
            next_num += 1

def start_cmd():
    global running
    running = True

def stop_cmd():
    global running
    running = False

def reset_cmd():
    global running
    global highest_prime
    running = False
    highest_prime = 0
    num_label.config(text=str(highest_prime))
    

# ----- CREATE UI -----
# create window
root = tk.Tk()
root.geometry("600x400")
root.title("Prime Numbers")

# -- add window content ---
# heading label
tk.Label(root, text="Prime Nubmers", font=("Helvetica","30")).pack(expand="Y")

# number label
num_label = tk.Label(root, text="0", font=("Helvetica","30"))
num_label.pack(expand="Y")

# buttons
btn_frame = tk.Frame(root)
btn_frame.pack(expand="Y")

start_btn = tk.Button(btn_frame, text="Start", font=("Helvetica","20"), width=10, bg="GREEN", command=start_cmd)
start_btn.grid(row=0,column=0,padx=10)

stop_btn = tk.Button(btn_frame, text="Stop", font=("Helvetica","20"), width=10, bg="RED", command=stop_cmd)
stop_btn.grid(row=0,column=1,padx=10)

reset_btn = tk.Button(btn_frame, text="Reset", font=("Helvetica","20"), width=10, bg="ORANGE", command=reset_cmd)
reset_btn.grid(row=0,column=2,padx=10)

# ----- MAIN PROGRAM -----
highest_prime = 0
running = False
#root.mainloop()

while True:
    if running:
        highest_prime = find_next_prime(highest_prime + 1)
        print(highest_prime)
        num_label.config(text=str(highest_prime))
    root.update()
