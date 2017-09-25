# Author: Ian Burke
# Module: Emerging Technologies
# Date: September, 2017

#Problem Sheet: https://emerging-technologies.github.io/problems/digits.html

import gzip

#with gzip.open('C:/Users/Iano/Downloads/t10k-images-idx3-ubyte.gz', 'rb') as f:
f = gzip.open('C:/Users/Iano/Downloads/t10k-labels-idx1-ubyte.gz', 'rb')
    #f.read()
magic = f.read(4)
magic = int.from_bytes(magic, 'big')

print("Magic is: ", magic)

noimg = f.read(4) #read how many labels in a file
noimg = int.from_bytes(noimg, 'big')
print("images are : ",noimg)

norow = f.read(4) #read how many rows in a file
norow = int.from_bytes(norow, 'big')
print("rows are : ",norow)

nocol = f.read(4) #read how many coloumns in a file
nocol = int.from_bytes(nocol, 'big')
print("cols are : ",nocol)