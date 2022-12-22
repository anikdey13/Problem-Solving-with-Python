T = int(input())

for i in range(T):
    N = input().split(' ')
    while("" in N):
        N.remove("")
    c = len(N)
    print(c)
