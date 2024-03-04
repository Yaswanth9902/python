# Take user input for the sorted array
nums = [int(x) for x in input("Enter the sorted array of distinct integers: ").split()]

# Take user input for the target value
target = int(input("Enter the target value: "))

left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        print("Output:", mid)
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Output:", left)