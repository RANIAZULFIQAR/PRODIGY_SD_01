import tkinter as tk
from tkinter import messagebox
class Conversion:
    def converting(self, read, read2):
        if read2 == 'celsius' or read2 == 'C':
            k = 273 + read
            f = (read * 9/5) + 32
            return k, f
        
        elif read2 == 'fahrenheit' or read2 == 'F':
            c = (read - 32) * 5/9
            k = 273 + c
            return c, k
        
        elif read2 == 'kelvin' or read2 == 'K':
            c = read - 273
            f = (c * 9/5) + 32
            return c, f
        
        else:
            return None, None

def on_convert():
    try:
        temperature = int(entry_temp.get())
        unit = entry_unit.get()
        k, other = converter.converting(temperature, unit)
        
        if k is None:
            messagebox.showerror("Error", "Invalid unit entered!")
        else:
            if unit.lower() == 'c' or unit.lower() == 'celsius':
                result.set(f"{temperature} Celsius is {k} Kelvin and {other} Fahrenheit.")
            elif unit.lower() == 'f' or unit.lower() == 'fahrenheit':
                result.set(f"{temperature} Fahrenheit is {other} Celsius and {k} Kelvin.")
            elif unit.lower() == 'k' or unit.lower() == 'kelvin':
                result.set(f"{temperature} Kelvin is {other} Celsius and {k} Fahrenheit.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the temperature.")

def on_exit():
    root.destroy()

# Set up the GUI
root = tk.Tk()
root.title("Temperature Converter")

# Create an instance of the Conversion class
converter = Conversion()

# Create the input fields and labels
tk.Label(root, text="Enter Temperature:").grid(row=0, column=0, padx=10, pady=10)
entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter Unit (C/F/K):").grid(row=1, column=0, padx=10, pady=10)
entry_unit = tk.Entry(root)
entry_unit.grid(row=1, column=1, padx=10, pady=10)

# Create a button to trigger the conversion
btn_convert = tk.Button(root, text="Convert", command=on_convert)
btn_convert.grid(row=2, column=0, columnspan=2, pady=10)

# Create a label to display the result
result = tk.StringVar()
tk.Label(root, textvariable=result).grid(row=3, column=0, columnspan=2, pady=10)

# Add an Exit button
btn_exit = tk.Button(root, text="Exit", command=on_exit)
btn_exit.grid(row=4, column=0, columnspan=2, pady=10)

# Start the GUI loop
root.mainloop()
