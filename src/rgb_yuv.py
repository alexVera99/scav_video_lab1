"""Exercise 1."""


def rgb_to_yuv(rgb: list) -> list:
    """
    Convert from R G B values to Y U V values.

    :param rgb: list containing the rgb values
    :return: list of three numbers containing the Y U V values
    """
    # Decomposed the input vector

    r_ch = rgb[0]
    g_ch = rgb[1]
    b_ch = rgb[2]

    # Computing the yuv values
    y_ch = 0.299 * r_ch + 0.587 * g_ch + 0.114 * b_ch
    u_ch = 0.429 * (b_ch - y_ch)
    v_ch = 0.877 * (r_ch - y_ch)

    return [y_ch, u_ch, v_ch]


def yuv_to_rgb(yuv: list) -> list:
    """
    Convert from Y U V values in YUV color space to R G B in the RGB color\
    space.

    :param yuv: list containing the yuv values
    :return: list of three numbers containing the R G B values.
    """
    # Decomposed the input vector
    y_ch = yuv[0]
    u_ch = yuv[1]
    v_ch = yuv[2]

    # Computing the rgb values
    r_ch = y_ch + 1.140 * v_ch
    g_ch = y_ch - 0.395 * u_ch - 0.581 * v_ch
    b_ch = y_ch + 2.032 * u_ch

    return [r_ch, g_ch, b_ch]


def main():
    """
    Show an example of how to use the constructed functions.

    :return: no return
    """
    rgb = [90, 50, 12]

    yuv = rgb_to_yuv(rgb)

    rgb_converted = yuv_to_rgb(yuv)

    print(f"Converting {rgb} in RGB space to {yuv} in YUV space")
    print(f"Converting {yuv} in YUV space to {rgb_converted} in RGB space")


if __name__ == '__main__':
    main()
