some_list_1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

def binary_search(some_list: list, num: int) -> int | None:
    low = 0
    high = len(some_list) -1
    while low <= high:
        mid = (low + high) // 2
        guess = some_list[mid]
        if guess == num:
            return mid
        elif guess <= num:
            low = mid - 1
        else:
            high = mid + 1
    return None

print(binary_search(some_list_1, 10))