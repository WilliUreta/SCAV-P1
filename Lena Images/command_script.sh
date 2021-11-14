#!/bin/bash

#Resize image to lower quality
ffmpeg -i Lenna_\(test_image\).jpeg -vf scale=320:240,setsar=1:1 320_240_lena.jpeg

#Transform image to b/w with hardest compression
ffmpeg -i Lenna_\(test_image\).jpeg -vf format=gray -qscale:v 31 bw_lena.jpeg
