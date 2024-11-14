points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
distances = []
for point in points:
    distance = point[0] ** 2 + point[1] ** 2 
    distances.append((distance, point))
distances.sort() 
closest_points = [point for _, point in distances[:k]] 

print(closest_points)
