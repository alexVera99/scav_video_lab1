"""Solution exercise 3"""


import logging
import pathlib
import subprocess
from exercise_2 import rename_from_path


def to_grayscale_and_compress_ffmpeg(img_path: pathlib.Path,
                                     compression_level: int = 6,
                                     out_filename: str = ""):
    """
    Convert image to grayscale and applies some compression based on \
    the compression_level.


    :param img_path: image filename path
    :param compression_level: number from 0 to 6 that sets the compression\
    efforts
    :param out_filename: output image filename
    :return: no return
    """
    if compression_level > 6 or compression_level < 0:
        raise Exception("Compression level should be between 0 and 100")

    if out_filename == "":
        img_name = img_path.name.split(".")[0]
        # Building the new name
        out_filename = f"{img_name}_gray_cl_{compression_level}"

    new_filename = rename_from_path(img_path, out_filename)

    cmd = ["ffmpeg", "-y", "-i", img_path, "-vf",
           "format=gray",
           "-compression_level", str(compression_level),
           new_filename]

    with subprocess.Popen(cmd,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE) as run_cmd:

        _, stderr = run_cmd.communicate()

    # Convert to str
    stderr = stderr.decode('ascii')
    print(stderr)

    if stderr.lower().__contains__("error"):
        logging.exception("Could not convert the image %s to grayscale.",
                          img_path.name)
        logging.error(stderr)


def main():
    """
    Use the to_grayscale_and_compress_ffmpeg function to test different \
    different compression levels.

    :return: no return
    """
    img_path = pathlib.Path("../data/lenna.png")

    compression_levels = [0, 1, 2, 3, 4, 5, 6]
    for _c_l in compression_levels:
        to_grayscale_and_compress_ffmpeg(img_path, compression_level=_c_l)


if __name__ == "__main__":
    main()
