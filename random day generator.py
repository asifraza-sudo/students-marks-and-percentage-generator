import tkinter as tk
import random


months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December",
          "Sunny July", "Relaxing August", "Adventure September", "Cozy December"]

activities = ["beach getaway", "mountain retreat", "city exploration", 
              "cultural immersion", "spa relaxation", "road trip", "cruise adventure"]


occasions = ["birthday", "anniversary", "honeymoon", "family vacation", "solo adventure"]

def generate_vacation_suggestion():
    random_month = random.choice(months)
    
    if random_month in ["September", "April", "June", "November", "Adventure September"]:
        random_day = random.randint(1, 30)
    elif random_month == "February":
        random_day = random.randint(1, 28) 
    else:
        random_day = random.randint(1, 31)
    
    random_activity = random.choice(activities)
    random_occasion = random.choice(occasions)
    
    suggestion_label.config(text=f"How about planning your {random_occasion} for {random_month} {random_day}s?\n"
                                f"You could enjoy a {random_activity}!")

root = tk.Tk()
root.title("Vacation Suggestion Generator")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

suggestion_label = tk.Label(frame, text="", font=("Helvetica", 14), wraplength=400, justify="center")
suggestion_label.pack(pady=20)

generate_button = tk.Button(frame, text="Generate Suggestion", command=generate_vacation_suggestion, font=("Helvetica", 12))
generate_button.pack(pady=10)

quit_button = tk.Button(frame, text="Quit", command=root.quit, font=("Helvetica", 12), bg="red", fg="white")
quit_button.pack(pady=10)

root.mainloop()
