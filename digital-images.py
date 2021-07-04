import numpy as np
from math import pow


def to_greyscale(channels: list, weights: list = None):
    dimensions = np.array(channels[1]).shape
    greyscale = np.zeros(dimensions)
    if weights is None:
        weights = [1 / len(channels)] * len(channels)
    for channel, weight in zip(channels, weights):
        channel = np.array(channel)
        if channel.shape != dimensions:
            raise Exception('Channel dimensions must match')
        greyscale += weight * channel
    return greyscale


def quantize(image, desired: int, current: int = 255):
    factor = 1 / (current / pow(2, desired))
    return np.floor(factor * image)


def main():
    red_channel = np.array([
        [205, 195],
        [238, 203]
    ])

    green_channel = np.array([
        [143, 138],
        [166, 143]
    ])

    blue_channel = np.array([
        [154, 145],
        [174, 151]
    ])

    greyscale = np.around(to_greyscale([red_channel, green_channel, blue_channel]), 0)
    print(greyscale)
    print(quantize(greyscale, 2))


if __name__ == "__main__":
    main()
