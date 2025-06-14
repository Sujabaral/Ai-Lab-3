from collections import Counter

data = [
    ([1, 2, 3], 'A'),
    ([2, 3, 4], 'A'),
    ([5, 5, 5], 'B'),
    ([6, 7, 8], 'B')
]

def distance(p1, p2):
    total = 0
    for i in range(len(p1)):
        total += (p1[i] - p2[i]) ** 2
    return total ** 0.5

def knn(test_point, data, k=3):
    distances = []
    for features, label in data:
        dist = distance(test_point, features)
        distances.append((dist, label))
    distances.sort(key=lambda x: x[0])
    neighbors = distances[:k]

    labels = [label for _, label in neighbors]
    most_common = Counter(labels).most_common(1)[0][0]
    return most_common

test = [3, 3, 3]
print("Classified as:", knn(test, data))
