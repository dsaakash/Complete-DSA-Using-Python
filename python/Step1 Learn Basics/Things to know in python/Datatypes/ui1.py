# Problem statement
# Data type refers to the type of value a variable has and the way the computer interprets it.



# Each data type has a different size. You’ve studied 5 different data types and the sizes of the data types:


# Explain
# Integer: 4 bytes
# Long: 8 bytes
# Float: 4 bytes
# Double: 8 bytes
# Character: 1 byte


# You’re given a data type. Print its size in bytes.



# Example :

# Explain
# Input: Long

# Output: 8

# Explanation: The size of a Long variable is given as 8 bytes.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# Long


# Sample Output 1:
# 8


# Explanation of sample input 1 :
# The size of a Long variable is given as 8 bytes.


# Sample Input 2:
# Float


# Sample Output 2:
# 4


# Explanation of sample input 2 :
# The size of a Float variable is given as 4 bytes.


# Expected time complexity :
# The expected time complexity is O(1).


# Constraints :
# ‘type’ is one of the data types given above.

# Time limit: 1 second




# Data type sizes in bytes
data_type_sizes = {
    'Integer': 4,
    'Long': 8,
    'Float': 4,
    'Double': 8,
    'Character': 1
}

def get_data_type_size(data_type):
    # Get the size of the given data type
    size = data_type_sizes.get(data_type, None)
    
    if size is not None:
        return size
    else:
        return "Invalid data type"

# Get input from the user
user_input = input("Enter a data type: ")

# Convert the input to title case for case-insensitivity
user_input = user_input.title()

# Get and print the size of the given data type
result = get_data_type_size(user_input)
print(f"Size of {user_input} variable: {result}")
