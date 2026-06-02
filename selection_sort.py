"""
Create a find smallest function, 
and use it in selection Sort function
"""

def findSmallest(arr):
    smallest_val= arr[0]       # stores the smallest **value**
    smallest_idx = 0        # store the smalles **index** for the value

    # use for loop to iterate through the list
    for i in range(1, len(arr)):
        # if value current < smallest now/previous, update the value as smallest
        if arr[i] < smallest_val:
            smallest_val = arr[i]
            smallest_idx = i

    return smallest_idx
    
def selectionSort(arr):
    # create empty list to sort the value of the target list
    newArr = []

    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))


my_arr = [1,4,2,3,6,5,8,7,10,19]
print(selectionSort(my_arr))