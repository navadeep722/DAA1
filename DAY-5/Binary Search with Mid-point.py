a = [3, 9, 14, 19, 25, 31, 42, 47, 53]
key = 31
N = len(a)
low = 0
high = N - 1
comparisons = 0
while low <= high:
    mid = (low + high) // 2
    comparisons += 1  
    
    print(f"Low: {low}, High: {high}, Mid: {mid}, Mid Value: {a[mid]}")
    
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
