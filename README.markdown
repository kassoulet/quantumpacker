
quantumpacker - Quantum Quantization Compressor
===============================================

Based on a complex algorithm which has root in quantum mechanics,
using quantum chaos applied to topological quantum numbers.

quantumpacker can compress huge files to only a series of topological quantum numbers,
resulting in a file 50x smaller. (more precisely 51.113x)

The method is complex, but the compression is reasonably fast, and decompression
is even faster.

This version is still very experimental, DO NOT use it in production, DO NOT use it
to archive anything important.

"screenshot"
------------
    # compress a big avi file
    gautier@quad-damage:~$ ./qp.py big_buck_bunny_720p_surround.avi
    big_buck_bunny_720p_surround.avi ok

    # tada! 50x smaller!!
    gautier@quad-damage:~$ ll -h big_buck_bunny_720p_surround.avi*
    -rw-r--r-- 1 gautier gautier 317M 2010-01-26 20:26 big_buck_bunny_720p_surround.avi
    -rw-r--r-- 1 gautier gautier 6.2M 2010-05-02 22:44 big_buck_bunny_720p_surround.avi.quant

    # decompress it,
    gautier@quad-damage:~$ ./qp.py big_buck_bunny_720p_surround.avi.quant
    big_buck_bunny_720p_surround.avi.quant ok

    # back to original form!
    gautier@quad-damage:~$ ll -h big_buck_bunny_720p_surround.avi*
    -rw-r--r-- 1 gautier gautier 317M 2010-01-26 20:26 big_buck_bunny_720p_surround.avi
    -rw-r--r-- 1 gautier gautier 6.2M 2010-05-02 22:44 big_buck_bunny_720p_surround.avi.quant
    -rw-r--r-- 1 gautier gautier 317M 2010-05-02 22:44 big_buck_bunny_720p_surround.avi.quant.orig

    # and they really are the same.
    gautier@quad-damage:~$ md5sum big*
    0da8fe124595f5b206d64cb1400bbefc  big_buck_bunny_720p_surround.avi
    0da8fe124595f5b206d64cb1400bbefc  big_buck_bunny_720p_surround.avi.quant.orig

