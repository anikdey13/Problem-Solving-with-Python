A,B,C,D = input().split(' ')
A = int(A)
B = int(B)
C = int(C)
D = int(D)
if B > C and D > A and C+D > A+B and C and D != float and A%2 == 0:
     print("Valores aceitos")
else:
     print("Valores nao aceitos")
    