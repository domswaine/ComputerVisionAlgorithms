import numpy as np
from distance_metrics import sum_of_absolute_differences
from offsets import horizontalVerticalAndDiagonal, neighbouring_positions


def region_growing(arr, metric, offsets):
    x_dim, y_dim, _ = arr.shape
    out = np.zeros((x_dim, y_dim))
    positions = [(x, y) for x in range(x_dim) for y in range(y_dim)]
    unassigned = set(positions)

    region_index = 1
    while len(unassigned) >= 1:
        seed = [p for p in positions if p in unassigned][0]
        region = [seed]

        for pos in region:
            if pos in unassigned:
                unassigned.remove(pos)
                feature_vector = arr[pos[0], pos[1], :]
                out[pos[0], pos[1]] = region_index
                for neighbour_pos in neighbouring_positions(pos, arr, offsets):
                    neighbour_feature_vector = arr[neighbour_pos[0], neighbour_pos[1], :]
                    if metric(feature_vector, neighbour_feature_vector) and neighbour_pos in unassigned:
                        region.append(neighbour_pos)

        region_index += 1
    return out


if __name__ == "__main__":
    image = np.array([
        [[5, 10, 15], [10, 15, 30], [10, 10, 25]],
        [[10, 10, 15], [5, 20, 15], [10, 5, 30]],
        [[5, 5, 15], [30, 10, 5], [30, 10, 10]]
    ])
    hvdOffsets = horizontalVerticalAndDiagonal
    print(region_growing(image, lambda a, b: sum_of_absolute_differences(a, b) < 12, hvdOffsets))
