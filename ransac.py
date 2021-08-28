import numpy as np
from distance_metrics import sum_of_absolute_differences


def ransac(matches, is_inlier):
    for i, (a, b) in enumerate(matches):
        model = np.array(a) - np.array(b)
        inliers = 0
        consensus_set = set()
        for other_a, other_b in matches[:i] + matches[i+1:]:
            other_model = np.array(other_a) - np.array(other_b)
            if is_inlier(model, other_model):
                inliers += 1
                consensus_set.add((a, b))

        print("Points:", (a, b))
        print("Model:", model)
        print("Number of inliers:", inliers)
        print("Consensus set:", consensus_set)
        print("")


def main():
    # lista = [np.array([0.7, 0.1, 0.8]), np.array([1.0, 0.7, 0.3]), np.array([0.0, 0.2, 0.4])]
    # listb = [np.array([0.5, 0.3, 0.7]), np.array([0.0, 0.0, 1.0]), np.array([0.7, 0.6, 0.7]), np.array([0.6, 0.5, 0.6]),
    #          np.array([1.0, 0.8, 0.6])]
    #
    # a = lista[2]
    # for b in listb:
    #     print(round(sum_of_absolute_differences(a, b), 4))

    function = lambda a, b: sum_of_absolute_differences(a, b) < 5.05
    matches = [((98, 37), (25, 98)), ((13, 72), (12, 74)), ((32, 80), (26, 82))]
    ransac(matches, function)


if __name__ == "__main__":
    main()
