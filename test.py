import math

T = int(input())


for i in range(T):
    N = int(input())
    l = math.sqrt(N)
    if l * l == N:
        print('YES')
    else:
        print('NO')

