"""Solution for Exercise 2."""


import logging
import pathlib
import subprocess


def exec_in_shell_wrapper(cmd: list):
    """
    Execute command in Linux shell.

    :param cmd: command to execute. Type: list
    :return: string with the stderr
    """
    with subprocess.Popen(cmd,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE) as run_cmd:

        _, stderr = run_cmd.communicate()

    return stderr


def rename_from_path(filename_path: pathlib.Path,
                     new_filename: str,
                     new_extension: str = None) -> pathlib.Path:
    """
    Rename file name.

    :param filename_path: file name with its path
    :param new_filename: new file name use to change the previous one
    :param new_extension: new file name extension to change the previous one
    :return: new filename with the correct extension and path
    """
    parent_path = filename_path.parent.resolve()

    if new_extension is None:
        new_extension = filename_path.name.split(".")[1]

    return parent_path / f"{new_filename}.{new_extension}"


def resize_using_ffmpeg(img_path: pathlib.Path,
                        width: int, height: int, out_filename: str = ""):
    """
    Resize an image with based on the given width and height.

    :param img_path: image filename path
    :param width: target width
    :param height: target height
    :param out_filename: output image filename
    :return: no return
    """
    if out_filename == "":
        img_name = img_path.name.split(".")[0]
        out_filename = f"{img_name}_resize_{width}x{height}"

    new_filename = rename_from_path(img_path, out_filename)

    cmd = ["ffmpeg", "-y", "-i", img_path, "-vf",
           f"scale={width}:{height}", new_filename]

    stderr = exec_in_shell_wrapper(cmd)

    # Convert to str
    stderr = stderr.decode('ascii')

    if stderr.lower().__contains__("error"):
        logging.exception("Could not resize the image %s", img_path.name)
        logging.error(stderr)


def main():
    """
    Show an example of how to use the constructed functions.

    :return: no return
    """
    img_path = pathlib.Path("../data/lenna.png")

    resize_using_ffmpeg(img_path, 10, 10)


if __name__ == "__main__":
    main()
