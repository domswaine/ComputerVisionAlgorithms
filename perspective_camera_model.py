import numpy as np


def main():
    # Intrinsic parameters
    alpha = 925  # Magnification factor in x' direction
    beta = 740  # Magnification factor in y' direction
    offset_x = 244  # Offset from the top-left corner to the principal point, along the x-axis, in pixels
    offset_y = 180  # Offset from the top-left corner to the principal point, along the y-axis, in pixels

    projection_operator = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ])

    intrinsic_camera_parameters = np.array([
        [alpha, 0, offset_x],
        [0, beta, offset_y],
        [0, 0, 1]
    ])

    X, Y, Z = 10, 10, 500

    coords = (1/Z) * np.matmul(
        intrinsic_camera_parameters,
        np.matmul(projection_operator, np.array([[X], [Y], [Z], [1]]))
    )
    print(coords)


if __name__ == "__main__":
    main()
