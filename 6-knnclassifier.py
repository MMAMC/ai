#Implement a simple k-NN classifier to classify points on a plane into two categories.

import math 

  

class Point: 

    def __init__(self, x, y, label): 

        self.x = x 

        self.y = y 

        self.label = label  # Category label (e.g., "red" or "blue") 

  

    def distance(self, other): 

        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2) 

  

def knn_classify(data, test_point, k): 

    # Calculate distances from test point to all points in data 

    distances = [(point.distance(test_point), point) for point in data] 

    # Sort distances in ascending order (nearest neighbors first) 

    distances.sort() 

  

    # Get k nearest neighbors 

    k_nearest_neighbors = distances[:k] 

  

    # Count occurrences of each label in k nearest neighbors 

    label_counts = {} 

    for distance, neighbor in k_nearest_neighbors: 

        label = neighbor.label 

        label_counts[label] = label_counts.get(label, 0) + 1 

  

    # Predict the label with the most occurrences 

    most_frequent_label = max(label_counts, key=label_counts.get) 

    return most_frequent_label 

  

# Example data (replace with your actual data) 

data = [ 

    Point(1, 2, "red"), 

    Point(3, 4, "red"), 

    Point(5, 1, "blue"), 

    Point(7, 3, "blue"), 

] 

  

# Example test point 

test_point = Point(4, 2, None) 

  

# Classify the test point with k=3 neighbors 

predicted_label = knn_classify(data, test_point, k=3) 

print(f"Predicted label for test point ({test_point.x}, {test_point.y}): {predicted_label}") 


""" Predicted label for test point (4, 2): red


** Process exited - Return Code: 0 **
Press Enter to exit terminal  """
