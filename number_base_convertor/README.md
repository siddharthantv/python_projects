# Base Converter Program Explanation

This Python program is a command-line tool for converting numbers between different bases. It supports four bases: binary, octal, decimal, and hexadecimal. The tool provides detailed steps to help understand the conversion process between the selected bases.

## Features
- **Base Support**: The program can convert between binary (base 2), octal (base 8), decimal (base 10), and hexadecimal (base 16).
- **Conversion Steps**: It not only outputs the result but also shows step-by-step conversion details, which can help with learning and understanding base conversion.
- **Error Handling**: If an invalid input is provided (e.g., a character that doesn’t exist in the given base), the program returns "Invalid input."

## Program Flow

### 1. Setting Up Arguments with argparse
The program uses `argparse` to parse command-line arguments, allowing the user to specify:
- The **number** they want to convert.
- The **from_base**, or the base in which the number is currently represented.
- The **to_base**, or the base to which the number should be converted.

Each base option is mapped to its numerical base (e.g., `"binary"` to `2`) using a dictionary (`BASE_MAP`). This setup lets the user easily select the base by name instead of by number.

### 2. Converting Between Bases
The main conversion function, `convert_base`, performs two key steps:
- **Convert to Base 10**: The program first converts the input number to a decimal (base 10) integer using `int(number, from_base)`.
- **Convert to Target Base**: Once in base 10, the program then converts it to the target base by repeatedly dividing by the target base and recording remainders, which represent the digits of the new base.

Each step is recorded in a list (`steps`) to track the intermediate values and explain the conversion.

### 3. Handling Edge Cases and Output
- **Zero Case**: If the input number is zero, it directly returns "0" as the result in any base.
- **Invalid Input**: If a character is provided that doesn’t exist in the specified base, the function returns an "Invalid input" message.

### 4. Running the Program
The program is executed through the command line with the following structure:
```bash
python script.py <number> <from_base> <to_base>
