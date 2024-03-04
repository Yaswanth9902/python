strs = []
n = int(input("Enter the number of strings: "))
for i in range(n):
    string = input("Enter string {}: ".format(i+1))
    strs.append(string)
min_str = min(strs, key=len)
for i, char in enumerate(min_str):
    for string in strs:
        if string[i] != char:
            print("Longest common prefix:", min_str[:i])
            exit()
print("Longest common prefix:", min_str)
