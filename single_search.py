def single_search(list,target):
    for i in range (len(list)):
        if i == target:
            return i
        i += 1
    return -1

my_list = [1,2,3,4,5,6,7,8,9,10]
print(single_search(my_list,8))