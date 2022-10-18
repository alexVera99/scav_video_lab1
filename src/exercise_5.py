import math
import numpy as np


def dct_transform(matrix, m, n):
    """
    Compute the DCT transformation
    From https://www.geeksforgeeks.org/discrete-cosine-transform-algorithm-program/

    :param matrix:
    :param m:
    :param n:
    :return:
    """
    dct = []
    for i in range(m):
        dct.append([None for _ in range(n)])

    for i in range(m):
        for j in range(n):

            # ci and cj depends on frequency as well as
            # number of row and columns of specified matrix
            if i == 0:
                ci = 1 / (m ** 0.5)
            else:
                ci = (2 / m) ** 0.5
            if j == 0:
                cj = 1 / (n ** 0.5)
            else:
                cj = (2 / n) ** 0.5

            # sum will temporarily store the sum of
            # cosine signals
            my_sum = 0
            for k in range(m):
                for l in range(n):
                    dct1 = matrix[k][l] * math.cos((2 * k + 1) * i * np.pi / (
                            2 * m)) * math.cos((2 * l + 1) * j * np.pi / (2 * n))
                    my_sum = my_sum + dct1

            dct[i][j] = ci * cj * my_sum

    for i in range(m):
        for j in range(n):
            print(dct[i][j], end="\t")
        print()


def main():
    """
    Show an example of how to use the constructed functions.

    :return: no return
    """
    # Driver code
    matrix = [[255, 255, 255, 255, 255, 255, 255, 255],
              [255, 255, 255, 255, 255, 255, 255, 255],
              [255, 255, 255, 255, 255, 255, 255, 255],
              [255, 255, 255, 255, 255, 255, 255, 255],
              [255, 255, 255, 255, 255, 255, 255, 255],
              [255, 255, 255, 255, 255, 255, 255, 255],
              [255, 255, 255, 255, 255, 255, 255, 255],
              [255, 255, 255, 255, 255, 255, 255, 255]]

    dct_transform(matrix, 8, 8)


if __name__ == "__main__":
    main()
