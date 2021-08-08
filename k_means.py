import numpy as np
from distance_metrics import sum_of_absolute_differences


def k_means(feature_vectors, cluster_centroids, metric):
    number_of_clusters = len(cluster_centroids)
    allotted_clusters = [0] * len(feature_vectors)
    cluster_indexes = list(range(number_of_clusters))

    has_changed = True
    while has_changed:
        has_changed = False

        for i, feature_vector in enumerate(feature_vectors):
            centroid_index = min(cluster_indexes, key=lambda a: metric(cluster_centroids[a], feature_vector))
            if centroid_index != allotted_clusters[i]:
                has_changed = True
            allotted_clusters[i] = centroid_index

        buckets = [[] for _ in range(number_of_clusters)]
        for feature_vector, cluster_index in zip(feature_vectors, allotted_clusters):
            buckets[cluster_index].append(feature_vector)
        for i in range(number_of_clusters):
            cluster_centroids[i] = np.mean(buckets[i], axis=0)

    print(allotted_clusters)
    print(np.around(cluster_centroids, 3))


if __name__ == "__main__":
    fvs = [
        np.array([5, 10, 15]), np.array([10, 15, 30]), np.array([10, 10, 25]),
        np.array([10, 10, 15]), np.array([5, 20, 15]), np.array([10, 5, 30]),
        np.array([5, 5, 15]), np.array([30, 10, 5]), np.array([30, 10, 10])
    ]
    centroids = [np.array([5, 10, 15]), np.array([10, 10, 25])]
    k_means(fvs, centroids, sum_of_absolute_differences)
