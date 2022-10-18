"""Solution for Exercise 5."""
import math
import numpy as np
from PIL import Image, ImageOps
from matplotlib import pyplot as plt


def dct_transform(image):
    """
    Compute the DCT transformation.\
    From \
    https://www.geeksforgeeks.org/discrete-cosine-transform-algorithm-program/.

    :param image:
    :return: dct transform matrix. Type: numpy.array
    """
    height, width = image.shape

    dct = []
    for _i in range(height):
        dct.append([None for _ in range(width)])

    for _i in range(height):
        for _j in range(width):

            # c_i and c_j depends on frequency as well as
            # number of row and columns of specified image
            if _i == 0:
                c_i = 1 / (height ** 0.5)
            else:
                c_i = (2 / height) ** 0.5
            if _j == 0:
                c_j = 1 / (width ** 0.5)
            else:
                c_j = (2 / width) ** 0.5

            # sum will temporarily store the sum of
            # cosine signals
            my_sum = 0
            for _k in range(height):
                for _l in range(width):
                    tmp_1 = math.cos((2 * _k + 1) * _i * np.pi / (2 * height))
                    tmp_2 = math.cos((2 * _l + 1) * _j * np.pi / (2 * width))

                    dct1 = image[_k][_l] * tmp_1 * tmp_2

                    my_sum = my_sum + dct1

            dct[_i][_j] = c_i * c_j * my_sum

    return np.asarray(dct)


def main():
    """
    Show an example of how to use the constructed functions.

    :return: no return
    """
    lenna = Image.open("../data/lenna.png")
    height, width = lenna.size
    resize_factor = 16
    lenna = lenna.resize([height // resize_factor, width // resize_factor])

    lenna_np = np.asarray(ImageOps.grayscale(lenna))

    dct = dct_transform(lenna_np)

    plt.imshow(dct / np.max(dct))
    plt.show()


if __name__ == "__main__":
    main()
