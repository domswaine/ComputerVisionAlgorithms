import numpy as np
from distance_metrics import sum_of_absolute_differences
from offsets import neighbouring_positions, eight_directions


def neighbour_similarities(arr, metric, offsets):
    for x in range(arr.shape[1]):
        for y in range(arr.shape[0]):
            pos = (x, y)
            feature_vector = arr[y, x]
            print(pos, feature_vector)
            for neighbour_pos in neighbouring_positions(pos, arr, offsets):
                neighbour_feature_vector = arr[neighbour_pos[1], neighbour_pos[0]]
                similarity = metric(feature_vector, neighbour_feature_vector)
                print(" > ", neighbour_pos, neighbour_feature_vector, similarity)
            print("")


if __name__ == "__main__":
    image = np.array([
        [[0.3,0.9,0.7], [0.2,0.8,0.5], [1.0,0.8,0.4]],
        [[0.7,0.4,0.3], [0.6,0.7,0.6], [1.0,1.0,0.0]],
        [[0.2,0.1,0.6], [0.6,1.0,1.0], [0.7,0.1,0.8]]
    ])
    neighbour_similarities(image, sum_of_absolute_differences, eight_directions)