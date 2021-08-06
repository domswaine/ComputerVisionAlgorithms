import numpy as np
from distance_metrics import sum_of_absolute_differences

horizontalAndVertical = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def neighbouring_positions(pos, arr, offsets):
    x_dim, y_dim, _ = arr.shape
    positions = [(pos[0] + x_offset, pos[1] + y_offset) for x_offset, y_offset in offsets]
    return [(x, y) for x, y in positions if 0 <= x < x_dim and 0 <= y < y_dim]


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


def region_merging(arr, metric, offsets):
    out = np.zeros((arr.shape[0], arr.shape[1]))
    region_indices = set()

    region_index = 1
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            out[x, y] = region_index
            region_indices.add(region_index)
            region_index += 1
    del region_index

    region_index = min(region_indices)


    return out


if __name__ == "__main__":
    a = np.array([
        [[5, 10, 15], [10, 15, 30], [10, 10, 25]],
        [[10, 10, 15], [5, 20, 15], [10, 5, 30]],
        [[10, 10, 15], [30, 10, 5], [10, 5, 30]]
    ])
    metric = lambda a, b: sum_of_absolute_differences(a, b) < 12
    # print(region_growing(a, metric, horizontalAndVertical))
    print(region_merging(a, metric, horizontalAndVertical))
