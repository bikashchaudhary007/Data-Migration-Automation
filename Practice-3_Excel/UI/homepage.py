import tkinter as tk

def button_click():
    label.config(text="Button clicked!")

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Migration Automation")

# Set the width and height of the window
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create a label widget
label = tk.Label(window, text="Hello, GUI World!")
label.pack()

# Create a button widget
button = tk.Button(window, text="Click Me!", command=button_click)
button.pack()

# Start the GUI event loop
window.mainloop()
