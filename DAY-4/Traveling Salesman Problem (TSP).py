import itertools
import math
cities = [(1, 2), (4, 5), (7, 1), (3, 6)]
distance = lambda city1, city2: math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
min_distance = float("inf")
shortest_path = []
for perm in itertools.permutations(cities[1:]):
    route = [cities[0]] + list(perm) + [cities[0]] 
    route_distance = 0
    for i in range(len(route) - 1):
        route_distance += distance(route[i], route[i + 1])
    if route_distance < min_distance:
        min_distance = route_distance
        shortest_path = route
print("Shortest distance:", min_distance)
print("Shortest path:", shortest_path)
