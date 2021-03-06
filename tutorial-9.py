import numpy as np
from distance_metrics import cross_correlation
from distance_metrics import normalised_cross_correlation
from distance_metrics import cosine
from distance_metrics import correlation_coefficient
from distance_metrics import sum_of_absolute_differences


def question_1():
    template = np.array([
        [100, 150, 200],
        [150, 10, 200],
        [200, 200, 250]
    ])

    image = np.array([
        [60, 50, 40, 40],
        [150, 100, 100, 80],
        [50, 20, 200, 80],
        [200, 150, 150, 50]
    ])

    print(normalised_cross_correlation(image[:3, :3], template))
    print(sum_of_absolute_differences(image[:3, :3], template))


def question_2():
    template_1 = np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1]])
    template_2 = np.array([[1, 0, 0], [1, 0, 0], [1, 1, 1]])
    template_3 = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    image = np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1]])

    for i, template in enumerate([template_1, template_2, template_3], 1):
        print("Template %i" %i)
        print(" > Cross correlation:", cross_correlation(image, template))
        print(" > Normalised cross correlation:", normalised_cross_correlation(image, template))
        print(" > Correlation coefficient:", correlation_coefficient(image, template))
        print(" > Sum of absolute differences:", sum_of_absolute_differences(image, template))
        print("")


def question_7():
    object_a = np.array([[2, 0, 0, 5, 1, 0, 0, 0, 3, 1]])
    object_b = np.array([[0, 0, 1, 2, 0, 3, 1, 0, 1, 0]])
    object_c = np.array([[1, 1, 2, 0, 0, 1, 0, 3, 1, 1]])
    new = np.array([[2, 1, 1, 0, 1, 1, 0, 2, 0, 1]])

    print(cosine(object_a, new))
    print(cosine(object_b, new))
    print(cosine(object_c, new))


if __name__ == "__main__":
    question_1()
    question_2()
    question_7()

