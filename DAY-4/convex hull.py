points = [(1, 1), (4, 6), (8, 1), (0, 0), (3, 3)]
hull = []

orientation = lambda p, q, r: (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        left_turn = False
        for k in range(len(points)):
            if k == i or k == j:
                continue
            if orientation(points[i], points[j], points[k]) < 0:
                left_turn = True
                break
        if not left_turn:
            if points[i] not in hull:
                hull.append(points[i])
            if points[j] not in hull:
                hull.append(points[j])

hull.sort(key=lambda x: (x[0], x[1]))
print("Convex Hull:", hull)
