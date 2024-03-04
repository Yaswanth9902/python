
nums = list(map(int, input("Enter the list of numbers separated by space: ").split()))
val = int(input("Enter the value to remove: "))


left = 0
right = len(nums) 

while left <= right:
    if nums[left] == val:
        nums[left], nums[right] = nums[right], nums[left]
        right -= 1
    else:
        left += 1
k = left
print("Number of elements not equal to {} after removing {}: {}".format(val, val, k))
print("Modified nums:", nums[:k])
