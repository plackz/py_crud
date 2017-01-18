import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

# make the GUI window not resizable
# win.resizable(0, 0)

# modified button click callback function
def clickMe():
    action.configure(text='Hello ' + name.get() + ' ' + numberChosen.get())

# position button in second row, second column (zero-based)
    action.grid(column=2, row=1)


# changing our label
aLabel = ttk.Label(win, text="Enter a name:")
aLabel.grid(column=0, row=0)

# adding a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# adding a button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)

# combobox widget
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')       # cannot input values into the combo box
# numberChosen = ttk.Combobox(win, width=12, textvariable=number)   # can input values into the combo box
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

nameEntered.focus()                     # Place cursor into name Entry

# action.configure(state='disabled')      # Disable the Button Widget

win.mainloop()

