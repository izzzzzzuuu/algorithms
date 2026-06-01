# create stopwatch to measure big O / performance
import time


def single_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
        else:
            i = i+1
    return -1

def binary_search(list,target):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2
        guess_target =  list[mid]

        if guess_target < target:
            low = mid + 1
        elif guess_target == target:
            return mid
        else:
            high = mid - 1
    return -1

my_list=[1,2,3,4,6,7,8,9,10]

# stopwatch for single search
start = time.perf_counter()
print(f"single search : {single_search(my_list,8)}")
end = time.perf_counter()
print(f"finished in {end - start:.6f} sec")

start = time.perf_counter()
print(f"binary search : {binary_search(my_list,8)}")
end = time.perf_counter()
print(f"finished in {end - start:.6f} sec")

# ===============================================
"""
for above output, single search seems faster than binary which contradicts with the theory.
However, for small list, the overhead of runtime need to be accounted for, because actual runtime also includes:

-function call overhead
-variable assignments
-computing mid
-loop setup
-Python interpreter overhead
-timing measurement noise

For such tiny workloads, those overheads are larger than the search itself.

Hence, the output is given.
"""

# ===============================================

big_list = list(range(1, 1_000_001))
big_target = 1_000_000

start = time.perf_counter()
single_search(big_list, big_target)
end = time.perf_counter()

print(f"Single search {end - start:.6f} sec")

start = time.perf_counter()
binary_search(big_list, big_target)
end = time.perf_counter()

print(f"Binary search {end - start:.6f} sec")