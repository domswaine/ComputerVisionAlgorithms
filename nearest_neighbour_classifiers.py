import numpy as np
from distance_metrics import euclidean_distance


def mean(feature_vectors):
    size = len(feature_vectors)
    cumulative = np.zeros(feature_vectors[0].shape)
    for feature_vector in feature_vectors:
        cumulative += feature_vector
    return cumulative / size


def nearest_neighbours(dataset, point, metric):
    point = np.array(point)
    for feature_vector, label in dataset:
        similarity = metric(np.array(feature_vector), point)
        print(feature_vector, label, similarity)


def nearest_mean(dataset, point, metric):
    clusters = {}

    for feature_vector, label in dataset:
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(feature_vector)

    grouped_dataset = []
    for label, feature_vectors in clusters.items():
        grouped_dataset.append((mean(feature_vectors), label))

    return nearest_neighbours(grouped_dataset, point, metric)


def main():
    arr = [np.array([2, 3, 0]), np.array([0, 1, 3]), np.array([1, 2, 4]), np.array([3, 4, 1])]

    point = np.array([1, 4, 2])

    for a in arr:
        print(round(euclidean_distance(point, a), 4))


if __name__ == "__main__":
    main()
