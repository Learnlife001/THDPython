mylist1 = []
mylist1.append([])

def myfactorial_recursive(n):
    if n == 0:
        return 1
    return n * myfactorial_recursive (n-1)

def myfactorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result =result * i
    return result


print(myfactorial_recursive(5))
#print(myfactorial_iterative(5))

