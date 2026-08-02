# divide and conquer technique, to solve problem
# includes the recursion algo

def quicksort(array):
    if len(array) < 2:
        return array        # base case: array with 0 or 1 element are already sorted
    else:
        pivot = array[0]
        less = [i for i in array[1:] 
                if i < pivot]     #Sub-array of all element < than pivot
        greater = [i for i in array[1:] 
                   if i >= pivot]  #Sub-array of all element > than pivot

        
        less_sorted = quicksort(less)
        greater_sorted = quicksort(greater)

        print(f"\nCurrent array:{array}")
        print(f"Current pivot point:{pivot}")
        print("less_sorted:", less_sorted)
        print("greater_sorted:", greater_sorted)
        print(f"Current progress: {less_sorted}{pivot}{greater_sorted}")

        return less_sorted + [pivot] + greater_sorted
        #return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,2,3]))

# pivot : 10 => less than 10 is : 5,2,3
# pivot : 5 => less than 5 is : 2,3
# current : [ [2,3], [5,10]]
# pivot : 2 => less than 2 is [] ; [ [3]+[pivot]+[5,10]]
# pivot : 3 => less than 3 is [2] ; [2] + [3] + [5,10]

""" Visualizing the recursion tree
quicksort([10,5,2,3])
pivot = 10

        [10,5,2,3]
          /     \
   [5,2,3]      []

pivot = 5

       [5,2,3]
        /    \
    [2,3]    []

pivot = 2

      [2,3]
      /   \
    []    [3]
"""