import tkinter as tk

# Function to convert temperature
def convert_temperature():
    try:
        temperature = float(temp_entry.get())
        scale = scale_var.get()

        if scale == "Celsius":
            fahrenheit = (temperature * 9 / 5) + 32
            kelvin = temperature + 273.15
            result = f"Fahrenheit: {fahrenheit:.2f}\nKelvin: {kelvin:.2f}"

        elif scale == "Fahrenheit":
            celsius = (temperature - 32) * 5 / 9
            kelvin = celsius + 273.15
            result = f"Celsius: {celsius:.2f}\nKelvin: {kelvin:.2f}"

        elif scale == "Kelvin":
            celsius = temperature - 273.15
            fahrenheit = (celsius * 9 / 5) + 32
            result = f"Celsius: {celsius:.2f}\nFahrenheit: {fahrenheit:.2f}"

        result_label.config(text=result)

    except ValueError:
        result_label.config(text="Please enter a valid number!")

# Create main window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("400x350")

# Heading
heading = tk.Label(
    window,
    text="Temperature Converter",
    font=("Arial", 16, "bold")
)
heading.pack(pady=15)

# Temperature Label
temp_label = tk.Label(window, text="Enter Temperature:")
temp_label.pack()

# Temperature Entry
temp_entry = tk.Entry(window, width=20)
temp_entry.pack(pady=5)

# Scale Label
scale_label = tk.Label(window, text="Select Scale:")
scale_label.pack()

# Dropdown Menu
scale_var = tk.StringVar()
scale_var.set("Celsius")

scale_menu = tk.OptionMenu(
    window,
    scale_var,
    "Celsius",
    "Fahrenheit",
    "Kelvin"
)
scale_menu.pack(pady=5)

# Convert Button
convert_button = tk.Button(
    window,
    text="Convert",
    command=convert_temperature
)
convert_button.pack(pady=10)

# Result Label
result_label = tk.Label(
    window,
    text="Result will appear here",
    font=("Arial", 11),
    justify="left"
)
result_label.pack(pady=15)

# Run the application
window.mainloop()