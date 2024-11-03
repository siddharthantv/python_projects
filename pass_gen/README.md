# Password Generator Program Explanation

This program is a customizable password generator designed to help users create strong, secure passwords based on their preferences. It allows for adjustments to the password’s length, difficulty level, and the types of characters included (such as uppercase letters, digits, and symbols).

## How the Program Works

### 1. Setting Parameters by Difficulty
The difficulty level—`easy`, `medium`, `hard`, or `expert`—determines the minimum length of the password and sometimes limits which types of characters can be included:
- **Easy**: Uses only lowercase letters and sets a minimum length of 8 characters.
- **Medium**: Allows the inclusion of uppercase letters, digits, and symbols (if specified), with a minimum length of 12 characters.
- **Hard**: Increases the minimum length to 16 characters and keeps all types of characters available.
- **Expert**: Sets a minimum length of 20 characters and automatically includes symbols, along with uppercase letters and digits if selected.

### 2. Character Selection
The program builds a pool of characters based on user choices. This pool may include:
- Lowercase letters
- Uppercase letters (if chosen)
- Digits (if chosen)
- Symbols (if chosen)

The program raises an error if no character types are selected, ensuring that a valid character set is always available for password generation.

### 3. Password Generation with Loading Bar
As the password is being generated, the program simulates a loading process. A rectangular progress bar visually fills up with each character added to the password, showing the progress as a percentage. This real-time update provides user feedback on the password generation process.

### 4. Displaying and Returning the Password
After the password has been generated, it is displayed to the user.

### 5. User Interaction
The program prompts the user for input to set:
- **Length** of the password
- **Difficulty** level (easy, medium, hard, or expert)
- **Character types** (whether to include uppercase letters, digits, and symbols)

If any input is invalid, such as a non-numeric input for length, an error message is displayed to guide the user.

## Summary
This program balances security and usability by providing options for complexity and showing a progress bar during generation. It’s a flexible tool for creating strong passwords tailored to individual needs.
