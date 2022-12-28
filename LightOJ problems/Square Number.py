import math

# T = int(input())

# for i in range(T):
#     N = int(input())
#     l = math.sqrt(N)
#     if l * l == N:
#         print('YES')
#     else:
#         print('NO')

T = int(input())

for i in range(T):
    N = int(input())
    root = math.sqrt(N)
    if int(root + 0.5) ** 2 == N:
        print('YES')
    else:
        print('NO')

