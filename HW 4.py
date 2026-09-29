# Task 5
n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

summ = 0

for i in range(0, n, 2):
    summ += array[i]

print(summ)