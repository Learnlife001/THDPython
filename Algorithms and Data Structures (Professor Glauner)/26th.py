def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False

print(is_multiple(10, 5))  # True
print(is_multiple(10, 3))  # False