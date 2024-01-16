def check_character_type(char):
    if char.isalpha():
        return 1 if char.isupper() else 0
    else:
        return -1

# Get input from the user
user_input = input("Enter a character: ")

# Check the type of the entered character
result = check_character_type(user_input)

# Print the result
print(f"Result for character '{user_input}': {result}")
