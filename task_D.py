# DA-108 : Python Programming - Task D
# Write a python script which takes input as number and outputs the number of bytes the number will require for its binary representation.

import shutil

terminal_width = shutil.get_terminal_size().columns #linebreak based on terminal width
linebreak = ("━" * terminal_width) # Special Character (Box Drawings Heavy Horizontal - Unicode code point - U+2501)

title = "Task_D - Byte Counter"
padding = (terminal_width - len(title)) // 2 # Calculate padding for centering
centered_title = " " * max(0, padding) + title
print(linebreak)
print(centered_title)
print(linebreak)

while True:
    user_input = input("Enter a number ('q' to quit): ")

    if user_input.lower() == 'q': # if user input either q or Q the program will quit
        print(linebreak)
        print("Goodbye! Hope to see you again soon!")
        print(linebreak)
        break

    try:
        number = int(user_input)
        
        binary_representation = bin(number)[2:] # Convert the number to binary and remove the '0b' prefix

        bits = len(binary_representation) # Calculate the number of bytes needed
        bytes_needed = (bits + 7) // 8  # Divide by 8 and round up

        print(linebreak)
        print("> The binary representation of the number is : " , binary_representation)
        print("> It requires ", bytes_needed," byte(s) for its binary representation.")
        print(linebreak)

    except ValueError:
        print(linebreak)
        print("Invalid input. Please enter a valid integer!")
        print(linebreak)