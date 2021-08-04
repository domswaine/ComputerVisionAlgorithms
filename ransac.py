import numpy as np


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
    function = lambda a, b: np.linalg.norm(a - b, 2) < 3

    matches = [((16, 50), (10, 40)), ((25, 14), (20, 5))]
    ransac(matches, function)

    matches = [((30, 31), (30, 5)), ((40, 45), (20, 10))]
    ransac(matches, function)


if __name__ == "__main__":
    main()
