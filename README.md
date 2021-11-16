# SCAV-P1
Public repo to deliver Practice 1 from Audio and Video Codification Systems

## Explanation

Each .py file has a main inside so it can be run using the following command:
```
python3 name_of_file.py
```

- 1. To test the rgb to yuv converter use the main.py
- 2. See the command_script.sh file and the 320_240_lena.jpeg
- 3. See the command_script.sh file and the bw_lena.jpeg. Using the qscale:v 31, we obtain the highest compression, According to ffmpeg documentation https://trac.ffmpeg.org/wiki/Encode/MPEG-4 . We can see that we have a size of 8,8kB instead of 474 kB. The image has clear "squares" from the compression
- 4. Run the run_len.py
- 5. Run the dct_enc_dec.py
 
 ## Dependencies

You will need to have the following packages installed:
- pdb
- numpy
- matplotlib
- scipy
