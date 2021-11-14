# -*- coding: utf-8 -*-
# This is a sample Python script.
# !/usr/bin/python
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from rgb_yuv import rgb2yuv, yuv2rgb
from run_len import encoded_message, decoded_message
from dct_enc_dec import dct_encoding, dct_decoding
import pdb;

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def validate_number(number):
    if (number > 255):
        return 255
    elif (number < 0):
        return 0
    else:
        return number

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Input values from [0-255]")

    r = validate_number(float(input("Value for R: ")))
    g = validate_number(float(input("Value for G: ")))
    b = validate_number(float(input("Value for B: ")))
    #pdb.set_trace()
    test = rgb2yuv(r, g, b)

    print(test)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
