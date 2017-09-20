# Author: Ian Burke
# Module: Emerging Technologies
# Date: September, 2017

#Problem Sheet: https://emerging-technologies.github.io/problems/digits.html

import gzip

with gzip.open('C:/Users/Iano/Desktop/t10k-images-idx3-ubyte.gz', 'rb') as f:
    f.read()
    #magic = f.read(4)

    print(f)