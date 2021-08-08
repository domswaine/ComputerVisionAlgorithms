horizontalAndVertical = [(0, 1), (1, 0), (0, -1), (-1, 0)]
diagonal = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

horizontalVerticalAndDiagonal = horizontalAndVertical + diagonal
eight_directions = set(horizontalVerticalAndDiagonal)


def neighbouring_positions(pos, arr, offsets):
    x_dim, y_dim, _ = arr.shape
    positions = [(pos[0] + x_offset, pos[1] + y_offset) for x_offset, y_offset in offsets]
    return [(x, y) for x, y in positions if 0 <= x < x_dim and 0 <= y < y_dim]