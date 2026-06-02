# def countdown(i):
#     print(i)
#     if i <= 0:
#         return i
#     return countdown(i-1)

# eg 1:

def countdown(i):
    print(i)
    if i <= 0:
        return              # base case
    else:
        countdown(i-1)      # recursive base


countdown(5)



# eg 2:
def factorial(x):
    if x == 1:
        return 1                    # base case
    else:
        return x * factorial(x-1)   # recursive base

print(f"factorial of 3 is : {factorial(3)}")