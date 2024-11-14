a = [5, 10, 15, 20, 25, 30, 35, 40, 45]
key = 20
N = len(a)
low = 0
high = N - 1
comparisons = 0
while low <= high:
    mid = (low + high) // 2
    comparisons += 1  
    if a[mid] == key:
        print(f"Element {key} found at index {mid}")
        print(f"Number of comparisons: {comparisons}")
        break
    elif a[mid] > key:
        high = mid - 1
    else:
        low = mid + 1
else:
    print(f"Element {key} not found")
    print(f"Number of comparisons: {comparisons}")
