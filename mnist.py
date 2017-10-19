# Author: Ian Burke
# Module: Emerging Technologies
# Date: September, 2017

#Problem Sheet: https://emerging-technologies.github.io/problems/digits.html
#import the following python libraries:
import gzip
# In shell, run pip install image..
from PIL import Image #image library
import numpy as np 

#function to read label files
def read_labels_from_file(filename):
    with gzip.open(filename,'rb') as f: #use gzip to open the file in read binary mode
        magic = f.read(4) # magic number is the first 4 bytes
        magic = int.from_bytes(magic,'big') # Convert bytes to integers.
        print("Magic is:", magic) # print to console

        # the same as above but with labels
        nolab = f.read(4)
        nolab = int.from_bytes(nolab,'big')
        print("Num of labels is:", nolab)
        # for looping through labels
        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label, 'big') for label in labels]
    return labels
print()
train_labels = read_labels_from_file("C:/Users/Iano/Downloads/train-labels-idx1-ubyte.gz")
test_labels = read_labels_from_file("C:/Users/Iano/Downloads/t10k-labels-idx1-ubyte.gz")

def read_images_from_file(filename):
    with gzip.open(filename,'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic,'big')
        print("Magic is:", magic)

        # Number of images in next 4 bytes
        noimg = f.read(4)
        noimg = int.from_bytes(noimg,'big')
        print("Number of images is:", noimg)

        # Number of rows in next 4 bytes
        norow = f.read(4)
        norow = int.from_bytes(norow,'big')
        print("Number of rows is:", norow)
        
        # Number of columns in next 4 bytes
        nocol = f.read(4)
        nocol = int.from_bytes(nocol,'big')
        print("Number of cols is:", nocol)

        images = [] # create array
        #for loop
        for i in range(noimg):
            rows = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1), 'big')) # append the current byte for every column
                rows.append(cols) # append columns array for every row
            images.append(rows) # append rows for every image
    return images
print() #line break

train_images = read_images_from_file("C:/Users/Iano/Downloads/train-images-idx3-ubyte.gz")
test_images = read_images_from_file("C:/Users/Iano/Downloads/t10k-images-idx3-ubyte.gz")

# print out image of 2
for row in train_images[4999]:
    for col in row: 
        print('.' if col <= 127 else '#', end='')
    print()

img = Image.fromarray(np.array(train_images[5]).astype('uint8'))
img = img.convert('RGB') # convert into rgb format
img.show() # display image in window
img.save(str(5) + '.png') # save the image file as png
