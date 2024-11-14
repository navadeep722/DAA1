import itertools
weights = [2, 3, 1]
values = [4, 5, 3]
capacity = 4
max_value = 0
best_selection = []
for r in range(len(weights) + 1):
    for selection in itertools.combinations(range(len(weights)), r):
        total_weight = sum(weights[i] for i in selection)
        if total_weight <= capacity:
            total_value = sum(values[i] for i in selection)
            
            
            if total_value > max_value:
                max_value = total_value
                best_selection = selection
print("Optimal Selection:", list(best_selection))
print("Total Value:", max_value)
