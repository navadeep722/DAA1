N = 8
a = [5, 7, 3, 4, 9, 12, 6, 2]
min_value = a[0]
max_value = a[0]
for i in range(1, N):
    if a[i] < min_value:
        min_value = a[i]
    if a[i] > max_value:
        max_value = a[i]
print("Min =", min_value)
print("Max =", max_value)
