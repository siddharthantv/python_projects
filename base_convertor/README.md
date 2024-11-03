
# Number Base Converter Application (Tkinter)

This code creates a GUI application using Python's `tkinter` library to convert a given number from one base to others. The program supports conversions between Binary (base 2), Octal (base 8), Decimal (base 10), and Hexadecimal (base 16), providing detailed steps for each conversion.

## Main Features and How It Works

### 1. Base Conversion Logic
- The `convert_base` function converts a number from one base to another.
- It first converts the input number to Decimal (base 10), then converts it from Decimal to the desired base.
- Steps of the conversion process are stored in a list called `steps`, which records each calculation, division, and remainder for traceability.
- The function returns both the converted result and the detailed steps as a formatted string.

### 2. Updating the UI
- The `on_convert` function is triggered whenever the user inputs a new number or changes the "From Base" option.
- It uses the `convert_base` function to calculate conversions to all supported bases (Binary, Octal, Decimal, and Hexadecimal).
- The conversion results are displayed as text in the UI, and the steps for each base conversion are shown in a scrollable text box.

### 3. User Interface Components
- **Entry Widget**: Allows the user to input a number.
- **Option Menu**: Lets the user select the base of the input number (from Binary, Octal, Decimal, or Hexadecimal).
- **Labels**: Display conversion results for each base.
- **Text Box**: Shows detailed steps of the conversions, formatted with bold headers for each base type. The text is initially disabled to prevent editing, but it’s re-enabled for updating the content.

### 4. Automatic Updates
- Whenever the user enters a number or changes the input base, the `on_convert` function automatically updates all conversion results and steps.

### 5. Styling
- The text box uses a bold style for headers (e.g., "Binary (2) Steps:") to make it easy to distinguish different sections of the steps.

## Purpose of the Code
The code provides an interactive way for users to convert numbers between common bases while understanding each step of the conversion process. This can be especially useful for learning and verifying base conversions.
