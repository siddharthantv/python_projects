import random
import string
import sys
import time

def generate_password(length=12, difficulty='medium', use_uppercase=True, use_digits=True, use_symbols=True):
    # Define character sets based on difficulty
    if difficulty == 'easy':
        length = max(8, length)
        use_uppercase = False
        use_digits = False
        use_symbols = False
    elif difficulty == 'medium':
        length = max(12, length)
    elif difficulty == 'hard':
        length = max(16, length)
    elif difficulty == 'expert':
        length = max(20, length)
        use_symbols = True
    else:
        raise ValueError("Invalid difficulty level. Choose from 'easy', 'medium', 'hard', or 'expert'.")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''
    
    # Combine all chosen character sets
    all_characters = lowercase + uppercase + digits + symbols
    
    # Check if at least one type of character is selected
    if not all_characters:
        raise ValueError("At least one type of character must be selected.")
    
    # Generate password with a rectangular loading bar
    password = ''
    bar_width = 40  # Width of the rectangular bar
    for i in range(length):
        password += random.choice(all_characters)
        # Calculate the progress
        progress = int((i + 1) / length * bar_width)
        # Create the rectangular loading bar
        bar = '█' * progress + '░' * (bar_width - progress)
        # Display the loading bar
        sys.stdout.write(f"\r[{bar}] {int((i + 1) / length * 100)}%")
        sys.stdout.flush()
        time.sleep(0.05)  # Simulate some processing time
    
    # Clear the line after completion
    sys.stdout.write("\n")
    
    return password

# Example usage
if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        difficulty = input("Select difficulty (easy, medium, hard, expert): ").lower()
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        print("Generated Password:", generate_password(length, difficulty, use_uppercase, use_digits, use_symbols))
    except ValueError as e:
        print(e)
