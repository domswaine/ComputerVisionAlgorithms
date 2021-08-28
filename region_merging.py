import numpy as np
from distance_metrics import sum_of_absolute_differences
from offsets import horizontalVerticalAndDiagonal, neighbouring_positions


def region_merging(arr, metric, offsets):
    y_dim, x_dim, _ = arr.shape

    out = np.array([
        [3, 2, 6],
        [9, 7, 5],
        [1, 4, 8]
    ])

    region_index = 1
    while region_index <= (x_dim * y_dim):
        to_expand = []

        for x in range(x_dim):
            for y in range(y_dim):
                if out[y, x] == region_index:
                    to_expand.append((x, y))

        while len(to_expand) >= 1:
            pos = to_expand.pop()
            feature_vector = arr[pos[1], pos[0]]
            out[pos[1], pos[0]] = region_index
            for neighbour_pos in neighbouring_positions(pos, arr, offsets):
                if out[neighbour_pos[1], neighbour_pos[0]] > region_index:
                    neighbour_feature_vector = arr[neighbour_pos[1], neighbour_pos[0]]
                    if metric(feature_vector, neighbour_feature_vector):
                        to_expand.append(neighbour_pos)
        region_index += 1

    return out


if __name__ == "__main__":
    img = np.array([
        [[0.3, 0.9, 0.7], [0.2, 0.8, 0.5], [1.0, 0.8, 0.4]],
        [[0.7, 0.4, 0.3], [0.6, 0.7, 0.6], [1.0, 1.0, 0.0]],
        [[0.2, 0.1, 0.6], [0.6, 1.0, 1.0], [0.7, 0.1, 0.8]]
    ])
    hvdOffsets = horizontalVerticalAndDiagonal
    print(region_merging(img, lambda a, b: sum_of_absolute_differences(a, b) < 1, hvdOffsets))
