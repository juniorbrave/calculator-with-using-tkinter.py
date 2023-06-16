#import tkinter for buttons and drop down menus;
import tkinter as tk
from tkinter import ttk

#for the calculate functions;
def calculate():
    try:
        deg1 = float(entry1.get())
        deg2 = float(entry2.get())
        operator = operator_combo.get()

        if operator == "+ (Sum.)":
            result = deg1 + deg2
        elif operator == "- (Min.)":
            result = deg1 - deg2
        elif operator == "* (Tim.)":
            result = deg1 * deg2
        elif operator == "/ (Div.)":
            result = deg1 / deg2
        else:
            result = "Invalid Operator"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Incorrect Entry")


root = tk.Tk()
root.title("Calculate 1.0.0 Alpha")

# Entries
entry1 = ttk.Entry(root)
entry1.pack()

entry2 = ttk.Entry(root)
entry2.pack()

# Operator w dropdown menus
operators = ["+ (Sum.)", "- (Min.)", "* (Tim.)", "/ (Div.)"]
operator_combo = ttk.Combobox(root, values=operators)
operator_combo.pack()

# Calculate button
calculate_button = ttk.Button(root, text="Can u calculate 4 me pls :)", command=calculate)
calculate_button.pack()

# Result tag
result_label = ttk.Label(root, text="Result : ")
result_label.pack()

root.mainloop()


print('A.M.E ')
print('Still learning... ¯\_(ツ)_/¯')