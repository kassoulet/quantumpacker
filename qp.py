#!/usr/bin/python

"""
quantumpacker - Quantum Quantization Compressor
Based on a complex algorithm which has root in quantum mechanics,
using quantum chaos applied to topological quantum numbers.

quantumpacker can compress huge files to only a series of topological quantum numbers,
resulting in a file 50x smaller. (51.113x in fact)

The method is complex, but the compression is reasonably fast, and decompression is
even faster.
"""

print 'quantumpacker - Quantum Quantization Compressor - by Gautier Portet <kassoulet at gmail>'

import os
import sys
import time
from os.path import getsize

# compression buffer size
BLOCK_SIZE = 1024*1

def error(msg):
    """
    Print an error message and exit program.
    """
    print msg
    raise SystemExit


progress_next = 0
def progress(filename, progress):
    """
    Display current processed filename, and job progress (in percent).
    """
    global progress_next
    t = time.time()
    if t > progress_next:
        sys.stdout.write('%s %3d%%\r' % (filename, progress))
        sys.stdout.flush()
        progress_next = t + 0.1


def is_quantum_file(filename):
    """
    Return True if the given filename is a file compressed by quantumpacker.
    """
    marker = 'q1'
    b = open(filename).read(len(marker))
    return b == marker


def compress(filename):
    """
    Compress a file.
    Will create a file with '.quant' prefixed to the filename.
    """
    quantizer = QuantumQuantizer()

    f = open(filename, 'rb')
    size = getsize(filename)
    current = 0.0
    while True:
        b = f.read(BLOCK_SIZE)
        if not b:
            break
        quantizer.update(b)
        current += len(b)
        progress(filename, 100.0*current/size)

    f.close()

    quantum = open(filename+'.quant', 'wb')
    quantum.write('q1' + quantizer.quantum())
    quantum.close()

    print filename, 'ok  '


def decompress(filename):
    """
    Decompress a file.
    Will create a file with '.orig' prefixed to the filename.
    """
    expander = QuantumExpander(filename)

    f = open(filename+'.orig', 'wb')
    size = expander.size()
    current = 0.0
    while True:
        b = expander.read(BLOCK_SIZE)
        if not b:
            break
        f.write(b)
        current += len(b)
        progress(filename, 100.0*current/size)

    f.close()

    print filename, 'ok  '


def manage_file(filename):
    """
    If the given file is compressed by quantumpacker, decompress. Else compress.
    """
    if is_quantum_file(filename):
        decompress(filename)
    else:
        compress(filename)


from core import QuantumQuantizer, QuantumExpander

files = sys.argv[1:]
if not files:
    error('need files to compress or decompress...')

for f in files:
    manage_file(f)



