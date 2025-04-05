import os
import pathlib
from itertools import product

from PIL import Image

from stamen import __ROOT__


def tile(filepath: pathlib.Path, tile_size: int = 256):
    """Takes an image and then tiles up the pieces of the square
        into tile_size x tile_size pieces.

    NOTE: partial tiles are ignored.
    """
    dir_out = __ROOT__.joinpath('imgs/unseen')

    name = filepath.stem
    ext = filepath.suffix
    img = Image.open(filepath)
    w, h = img.size

    grid = product(range(0, h - h % tile_size, tile_size), range(0, w - w % tile_size, tile_size))
    for i, j in grid:
        box = (j, i , j + tile_size, i + tile_size)
        out = dir_out.joinpath(f'{name}_{i}_{j}{ext}')
        img.crop(box).save(out)

