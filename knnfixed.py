from collections import Counter
import math

# Example dataset: Each item is ([feature1, feature2], label)
data = [
    ([1, 2], 'Class A'),
    ([2, 3], 'Class A'),
    ([3, 3], 'Class B'),
    ([6, 5], 'Class B')
]

# Function to calculate Euclidean distance between two points with 2 features
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# KNN function
def knn(test_point, data, k=3):
    distances = []
    for features, label in data:
        dist = euclidean_distance(test_point, features)
        distances.append((dist, label))
    distances.sort(key=lambda x: x[0])  # Sort by distance

    # Get labels of k closest points
    k_labels = [label for _, label in distances[:k]]

    # Return the most common label among neighbors
    most_common = Counter(k_labels).most_common(1)[0][0]
    return most_common

# Test example
test_point = [3, 2]
predicted_class = knn(test_point, data, k=3)
print(f"The test point {test_point} is classified as: {predicted_class}")
