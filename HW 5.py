a = int(input())
b = int(input())
n = int(input())

ans = 0

for i in range(n):
    c = int(input())
    if (a**2 + b**2 == c**2) and (c > 10) and (c %3 == 0 or c % 4 == 0):
        ans += 1

print(ans)