def binary_search(list,item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]

        if guess < item:
            low=mid + 1
        elif guess == item:
            return mid
        else:
            high = mid - 1
    return -1

my_list = [1, 2, 3, 5, 7, 9]

print(binary_search(my_list, 5))