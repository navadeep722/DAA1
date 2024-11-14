import itertools
cost_matrix = [
    [3, 10, 7],
    [8, 5, 12],
    [4, 6, 9]
]
min_cost = float("inf")
best_assignment = []
for assignment in itertools.permutations(range(len(cost_matrix))):
    total_cost = sum(cost_matrix[worker][task] for worker, task in enumerate(assignment))
    if total_cost < min_cost:
     min_cost = total_cost
     best_assignment = assignment
print("Minimum cost:", min_cost)
print("Best assignment:", best_assignment)
