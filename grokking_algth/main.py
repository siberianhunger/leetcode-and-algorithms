list_to_sort = [1, 3, 5, 7, 9]
l_2 = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

def binary_search(unsorted_list: list[int], number_to_find: int) -> int | None:
    """
    :param number_to_find:
    :param unsorted_list: ordered list of integers
    :return: index of a given number in the list or None if it doesn't appear in the list
    """
    low = 0
    high = len(unsorted_list) - 1
    while low <= high:
        guess = low + (high-low) // 2
        if unsorted_list[guess] == number_to_find:
            return guess
        elif unsorted_list[guess] > number_to_find:
            high = guess - 1
        else:
            low = guess + 1

    return


assert binary_search(list_to_sort, 3) == 1
assert binary_search(l_2, 23) == 5

