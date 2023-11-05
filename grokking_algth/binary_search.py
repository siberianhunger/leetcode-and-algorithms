"""
There is an ordered list of unique numbers. We need to find an index of a given number.
"""
nums_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

n_2 = [-1,0,3,5,9,12]

def binary_search(nums: list, target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = (low + high) // 2
        guess = nums[middle]
        if guess == target:
            return middle
        elif guess > target:
            high = middle - 1
        else:
            low = middle + 1
    return -1


def binary_search_2(nums: list, target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = (low + high)//2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            high -= 1
        else:
            low += 1
    return -1

def binary_search_3(nums: list, target: int) -> int:
    lowest = 0
    highest = len(nums) - 1
    while lowest <= highest:
        middle = lowest + ((highest - lowest) // 2)
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            highest -= 1
        elif nums[middle] < target:
            lowest += 1
    return -1



# print(binary_search(nums_1, 10))

print(binary_search_3(nums_1, 21))