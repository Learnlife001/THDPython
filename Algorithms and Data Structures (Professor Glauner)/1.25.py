def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))

def remove_punctuation(s):
    punctuation = ['.', ',', '!', '?', ';', ':']
    for punct in punctuation:
        s = s.replace(punct, '')
    return s
print(remove_punctuation("H!ey, ha?ve y.ou.."))



def sum_divided_by_2(n):
    sum =6
    for i in range(1, n):
        sum /= i
    return sum
print(sum_divided_by_2(6))