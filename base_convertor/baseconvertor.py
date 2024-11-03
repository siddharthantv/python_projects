import tkinter as tk
from tkinter import messagebox

# Dictionary to map names to bases
BASE_MAP = {
    "Binary (2)": 2,
    "Octal (8)": 8,
    "Decimal (10)": 10,
    "Hexadecimal (16)": 16
}

def convert_base(number, from_base, to_base):
    try:
        # Convert number to base 10
        base10 = int(number, from_base)
        
        # Store the steps for conversion
        steps = [f"Convert {number} from base {from_base} to base 10:"]
        steps.append(f"Value in base 10: {base10}")
        
        # Convert base 10 number to the desired base
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        
        if base10 == 0:
            return "0", "\n".join(steps)
        
        steps.append(f"Convert {base10} from base 10 to base {to_base}:")
        while base10 > 0:
            remainder = base10 % to_base
            result = digits[remainder] + result
            steps.append(f"{base10} / {to_base} = {base10 // to_base} with remainder {remainder} ({digits[remainder]})")
            base10 //= to_base
        
        steps.append(f"Value in base {to_base}: {result}")
        return result, "\n".join(steps)
    except ValueError:
        return "Invalid input", "Invalid input"

def on_convert(*args):
    number = var_number.get()
    from_base = BASE_MAP[var_from_base.get()]
    
    binary_result, binary_steps = convert_base(number, from_base, 2)
    octal_result, octal_steps = convert_base(number, from_base, 8)
    decimal_result, decimal_steps = convert_base(number, from_base, 10)
    hexadecimal_result, hexadecimal_steps = convert_base(number, from_base, 16)
    
    label_binary_result.config(text=f"Binary (2): {binary_result}")
    label_octal_result.config(text=f"Octal (8): {octal_result}")
    label_decimal_result.config(text=f"Decimal (10): {decimal_result}")
    label_hexadecimal_result.config(text=f"Hexadecimal (16): {hexadecimal_result}")

    text_steps.config(state=tk.NORMAL)
    text_steps.delete(1.0, tk.END)
    
    # Insert steps with bold headers
    text_steps.insert(tk.END, "Binary (2) Steps:\n", "bold")
    text_steps.insert(tk.END, binary_steps + "\n\n")
    
    text_steps.insert(tk.END, "Octal (8) Steps:\n", "bold")
    text_steps.insert(tk.END, octal_steps + "\n\n")
    
    text_steps.insert(tk.END, "Decimal (10) Steps:\n", "bold")
    text_steps.insert(tk.END, decimal_steps + "\n\n")
    
    text_steps.insert(tk.END, "Hexadecimal (16) Steps:\n", "bold")
    text_steps.insert(tk.END, hexadecimal_steps + "\n\n")
    
    text_steps.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Number Base Converter")

# Create and place widgets
label_number = tk.Label(root, text="Number:")
label_number.grid(row=0, column=0, padx=10, pady=10)
var_number = tk.StringVar()
var_number.trace_add("write", on_convert)
entry_number = tk.Entry(root, textvariable=var_number)
entry_number.grid(row=0, column=1, padx=10, pady=10)

label_from_base = tk.Label(root, text="From Base:")
label_from_base.grid(row=1, column=0, padx=10, pady=10)
var_from_base = tk.StringVar(root)
var_from_base.set("Decimal (10)")
optionmenu_from_base = tk.OptionMenu(root, var_from_base, *BASE_MAP.keys(), command=on_convert)
optionmenu_from_base.grid(row=1, column=1, padx=10, pady=10)

label_binary_result = tk.Label(root, text="Binary (2):")
label_binary_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

label_octal_result = tk.Label(root, text="Octal (8):")
label_octal_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_decimal_result = tk.Label(root, text="Decimal (10):")
label_decimal_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

label_hexadecimal_result = tk.Label(root, text="Hexadecimal (16):")
label_hexadecimal_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

text_steps = tk.Text(root, height=15, width=50)
text_steps.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
text_steps.config(state=tk.DISABLED)

# Add bold tag for text widget
text_steps.tag_configure("bold", font=("Helvetica", 10, "bold"))

# Start the main event loop
root.mainloop()

