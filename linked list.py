num1 = input("Enter the first number (digits separated by spaces): ")
num1 = [int(x) for x in num1.split()]

num2 = input("Enter the second number (digits separated by spaces): ")
num2 = [int(x) for x in num2.split()]

num1.reverse()
num2.reverse()

result = []
carry = 0

for i in range(max(len(num1), len(num2))):
    digit_sum = carry
    
    if i < len(num1):
        digit_sum += num1[i]
    if i < len(num2):
        digit_sum += num2[i]
    
    result.append(digit_sum % 10)
    
    carry = digit_sum // 10

if carry:
    result.append(carry)

result.reverse()

print("The sum of the two numbers is:", ''.join(map(str, result)))
