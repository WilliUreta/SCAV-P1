# based on https://inst.eecs.berkeley.edu/~ee123/sp16/Sections/JPEG_DCT_Demo.html

# Import functions and libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy

from numpy import pi
from numpy import sin
from numpy import zeros
from numpy import r_
from scipy import signal
from scipy import fftpack  # pip install Pillow
#import matplotlib.pylab as pylab
from matplotlib.pyplot import imread


def dct2(a):
    return scipy.fftpack.dct( scipy.fftpack.dct( a, axis=0, norm='ortho' ), axis=1, norm='ortho' )


def idct2(a):
    return scipy.fftpack.idct( scipy.fftpack.idct( a, axis=0 , norm='ortho'), axis=1 , norm='ortho')


def dct_encoding(path, N):
    im = imread(path).astype(float)
    imsize = im.shape
    dct = np.zeros(imsize)

    # Do NxN DCT on image (in-place)
    for i in r_[:imsize[0]:N]:
        for j in r_[:imsize[1]:N]:
            dct[i:(i + N), j:(j + N)] = dct2(im[i:(i + N), j:(j + N)])

    thresh = 0.012
    plt.figure()
    plt.imshow(dct, cmap='gray', vmax=np.max(dct) * 0.01, vmin=0)
    plt.title(str(N) + "*" + str(N) + " DCT's of the image")
    plt.show(block=True)

    # we want to take the high freq information, gives + info.
    dct_thresh = dct * (abs(dct) > (thresh*np.max(dct)))      # take the "80%" of higher values

    plt.figure()
    plt.imshow(dct_thresh, cmap='gray', vmax=np.max(dct) * 0.01, vmin=0)
    plt.title("Thresholded 8x8 DCTs of the image")
    plt.show(block=True)

    percent_nonzeros = np.sum(dct_thresh != 0.0) / (
                imsize[0] * imsize[1] * 1.0)

    print("Keeping only %f%% of the DCT coefficients" % (percent_nonzeros * 100.0))
    return dct  # return the dct values

def dct_decoding(path, dct, N):

    im = imread(path).astype(float)

    imsize = dct.shape
    im_idct = np.zeros(imsize)

    # Do NxN DCT on image (in-place)
    for i in r_[:imsize[0]:N]:
        for j in r_[:imsize[1]:N]:
            im_idct[i:(i + N), j:(j + N)] = idct2(dct[i:(i + N), j:(j + N)])

    plt.figure()
    plt.imshow(np.hstack((im, im_idct)), cmap='gray')
    plt.title("Comparison between original and DCT compressed images")
    plt.show(block=True)


if __name__ == '__main__':

    #display()
    path = input("Enter the path to the image:")
    N = int(input("Enter the block size (has to be an integer):"))

    dct = dct_encoding(path, N)
    dct_decoding(path, dct, N)