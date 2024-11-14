A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
sum_ab = {}
for i in range(len(A)):
    for j in range(len(B)):
        sum_ab[A[i] + B[j]] = sum_ab.get(A[i] + B[j], 0) + 1
count = 0
for k in range(len(C)):
    for l in range(len(D)):
        target = -(C[k] + D[l])
        if target in sum_ab:
            count += sum_ab[target]
print(count)
