input()
A = [int(i) for i in input().split()]
D = [0 for _ in A]
prev = [-1 for _ in A]
max_len = 1
index = 0
for i in range(len(A)):
    D[i] = 1
    for j in range(i):
        if A[i] <= A[j] and D[j] + 1 > D[i]:
            D[i] = D[j] + 1
            if D[i] >= max_len:
                max_len = D[i]
                index = i
            prev[i] = j
print(max_len)
res_list = [-1 for _ in range(max_len)]
for x in range(len(D) - 1, -1, -1):
    if D[x] != max_len:
        continue
    res_list[max_len - 1] = x + 1
    max_len -= 1
    if max_len == 0:
        break
print(*res_list)
