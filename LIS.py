input()
A = [int(i) for i in input().split()]
D = [0 for _ in A]
for i in range(len(A)):
    D[i] = 1
    for j in range(i):
        if A[i] % A[j] == 0 and D[j] + 1 > D[i]:
            D[i] = D[j] + 1
result = 0
for k in D:
    if k > result:
        result = k
print(result)
