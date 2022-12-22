T = int(input())

for i in range(1,T+1):
    N = input().split(' ')
    nl = [int(x) for x in N]
    nl.sort()
    print('Case %i: '%i,end='')
    for x in nl:
        print(x, end=' ')