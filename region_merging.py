import numpy as np
from distance_metrics import sum_of_absolute_differences
from offsets import horizontalVerticalAndDiagonal, neighbouring_positions


def region_merging(arr, metric, offsets):
    x_dim, y_dim, _ = arr.shape
    out = np.zeros((x_dim, y_dim))

    region_index = 1
    for y in range(y_dim):
        for x in range(x_dim):
            out[y, x] = region_index
            region_index += 1

    region_index = 1
    while region_index < (x_dim * y_dim):
        to_expand = []

        for y in range(y_dim):
            for x in range(x_dim):
                if out[y, x] == region_index:
                    to_expand.append((x, y))

        while len(to_expand) >= 1:
            pos = to_expand.pop()
            feature_vector = arr[pos[1], pos[0], :]
            out[pos[1], pos[0]] = region_index
            for neighbour_pos in neighbouring_positions(pos, arr, offsets):
                if out[neighbour_pos[1], neighbour_pos[0]] > region_index:
                    neighbour_feature_vector = arr[neighbour_pos[1], neighbour_pos[0], :]
                    if metric(feature_vector, neighbour_feature_vector):
                        to_expand.append(neighbour_pos)
        region_index += 1

    return out


if __name__ == "__main__":
    img = np.array([
        [[5, 10, 15], [10, 15, 30], [10, 10, 25]],
        [[10, 10, 15], [5, 20, 15], [10, 5, 30]],
        [[10, 10, 15], [30, 10, 5], [30, 10, 10]]
    ])
    hvdOffsets = horizontalVerticalAndDiagonal
    print(region_merging(img, lambda a, b: sum_of_absolute_differences(a, b) < 12, hvdOffsets))
