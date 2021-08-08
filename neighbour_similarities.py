import numpy as np
from distance_metrics import sum_of_absolute_differences
from offsets import neighbouring_positions, eight_directions


def neighbour_similarities(arr, metric, offsets):
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            pos = (x, y)
            feature_vector = arr[x, y]
            print(pos, feature_vector)
            for neighbour_pos in neighbouring_positions(pos, arr, offsets):
                neighbour_feature_vector = arr[neighbour_pos[0], neighbour_pos[1]]
                similarity = metric(feature_vector, neighbour_feature_vector)
                print(" > ", neighbour_pos, neighbour_feature_vector, similarity)
            print("")


if __name__ == "__main__":
    image = np.array([
        [[5, 10, 15], [10, 15, 30], [10, 10, 25]],
        [[10, 10, 15], [5, 20, 15], [10, 5, 30]],
        [[5, 5, 15], [30, 10, 5], [30, 10, 10]]
    ])
    neighbour_similarities(image, sum_of_absolute_differences, eight_directions)