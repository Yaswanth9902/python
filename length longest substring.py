s = input("Enter a string: ")

char_index = {}
max_length = 0
start = 0

for end, char in enumerate(s):
    if char in char_index and char_index[char] >= start:
        start = char_index[char] + 1

    char_index[char] = end
    max_length = max(max_length, end - start + 1)

print("Length of the longest substring without repeating characters:", max_length)
