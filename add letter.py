s = input("Enter string s: ")
t = input("Enter string t: ")
for char in t:
    if char not in s:
        a = char
print("Added letter:", a)