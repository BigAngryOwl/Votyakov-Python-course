# Task 2
print('Task 2')
print(input() == input())

# Task 3
print('Task 3')
nums = []

for i in range(4):
    nums.append(int(input()))

print(min(nums))

# Task 4
print('Task 4')
nums = []

for i in range(4):
    nums.append(int(input()))

print(max(nums))

# Task 5
print('Task 5')
sides = []

for i in range(3):
    sides.append(int(input()))

sides.sort()

if sides[0] + sides[1] > sides[2]:
    print(True) 
else:
    print(False)

# Task 6
print('Task 6')
sides = []

for i in range(3):
    sides.append(int(input()))

sides.sort()

if sides[0] + sides[1] >= sides[2]:
    if sides[0] + sides[1] == sides[2]:
        print('Вырожденный')
    elif sides[0] == sides[1] and sides[0] == sides[2]:
        print('Равносторонний')
    else:
        print('Разносторонний')
else:
    print('Не треугольник')

# Task 7
print('Task 7')
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b < c or d < a: # [a b] [c d] or [c d] [a b]
    print(0)
elif a <= c and d <= b: # [a {c d} b]
    print(d - c + 1)
elif c <= a and b <= d: # [c {a b} d]
    print(b - a + 1)
elif c <= a and d <= b: # {c [a d} b]
    print(d - a + 1)
elif a <= c and b <= d: # {a [c b} d]
    print(b - c + 1)