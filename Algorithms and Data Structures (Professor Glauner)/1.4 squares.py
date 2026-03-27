def sum_squares(n):
    sum = 0
    for i in range(1,n):
        sum += i**2
    return sum
print(sum_squares(3))