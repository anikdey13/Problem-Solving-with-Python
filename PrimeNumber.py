
#Prime Number

N = int(input())

if N > 1:
    for i in range(2, N):
        if N % i == 0:
            print(N, 'is not a prime number')
            break
    else:
        print(N, 'is a prime number')
else:
    print(N, 'is a prime number')


#1 to 100 prime number

for i in range(2, 101):
    for k in range(2, i):
        if i % k == 0:
            break
    else:
        print(i, end=' ')
