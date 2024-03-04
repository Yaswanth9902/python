n = str(input("Enter the string: "))
n = n.lower()
if n == n[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")