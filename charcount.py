# Input string
input_string = "Hello, World!"
# Initialize an empty dictionary to store character counts
char_count = {}
# Iterate through each character in the string
for char in input_string:
    # Update the character count in the dictionary
    char_count[char] = char_count.get(char, 0) + 1
# Print the character counts
for char, count in char_count.items():
    print(f"'{char}': {count}")
