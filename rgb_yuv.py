#
from typing import Union, Any
import pdb


def rgb2yuv(r, g, b):

    #pdb.set_trace()
    y = 0.257 * r + 0.504 * g + 0.098 * b + 16
    u = -0.148 * r - 0.291 * g + 0.439 * b + 128
    v = 0.439 * r - 0.368 * g - 0.071 * b + 128

    return [y, u, v]


def yuv2rgb(y, u, v):

    b = 1.64 * (y-16) + 2.018 * (u - 128)
    g = 1.64 * (y-16) - 0.813 * (v - 128) - 0.391 * (u - 128)
    r = 1.64 * (y-16) + 1.596 * (v - 128)

    return [r, g, b]
