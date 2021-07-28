import numpy as np
from math import pi, exp
from scipy.signal import convolve2d, correlate2d


def t3_q1():
    H = np.array([[1, 0], [1, 1]])
    I1 = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    I2 = np.array([[0, 0, 0], [1, 1, 0], [0, 1, 0]])
    print(convolve2d(I1, H, 'valid'))
    print(convolve2d(I2, H, 'valid'))


def t3_q2():
    I = np.array([[0.25, 1, 0.8], [0.75, 1, 1], [0, 1, 0.4]])
    H = np.array([[0, 0, 0], [0, 0, 1], [0, 0, 0]])
    print(convolve2d(I, H, 'same'))


def t3_q3():
    h = np.array([[1, 0.5, 0.1]])
    print(convolve2d(h, h.transpose()))
    print(correlate2d(h, h.transpose()))
    I = np.ones((3, 3))
    print(convolve2d(convolve2d(I, h, 'same'), h.transpose(), 'same'))


firstDerivative = np.array([[-1, 1]])
secondDerivative = np.array([[-1, 2, -1]])

laplacian = np.array([
    [-1, -1, -1],
    [-1, +8, -1],
    [-1, -1, -1]
])


def t3_q5():
    print(firstDerivative)
    print(firstDerivative.transpose())
    print(secondDerivative)
    print(secondDerivative.transpose())
    print(laplacian)


def t3_q6():
    mask = np.array([[-1, 1]])
    print(convolve2d(mask, mask))


def sqr(n):
    return n * n


def gaussian_mask(x, y, std):
    return (1 / (2 * pi * sqr(std))) \
           * exp(-1 * ((sqr(x) + sqr(y))/(2 * sqr(std))))


def t3_q7():
    for x in range(-1, 2):
        for y in range(-1, 2):
            print("(%i, %i)" % (x, y), gaussian_mask(x, y, 0.46))


def main():
    t3_q1()
    t3_q2()
    t3_q3()
    t3_q5()
    t3_q6()
    t3_q7()


if __name__ == "__main__":
    main()
