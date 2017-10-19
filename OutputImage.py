# Author: Ian Burke
# Module: Emerging Technologies
#Problem Sheet: https://emerging-technologies.github.io/problems/digits.html

#import the following python libraries:
import gzip
import numpy as np 
#Function to read images from file
def read_images_from_file(filename):
    train_images = read_images_from_file('C:/Users/Iano/Downloads/train-images-idx3-ubyte.gz')

for img in train_images:
    for row in img:
        for col in row:
            try:
                print('.' if col <= 127 else '#', end = '.')
            except TypeError as err:
                print('.', end = '.')

        print()

import PIL.Image as pil # importing image library
img = pil.fromarray(np.array(train_images[5]).astype('uint8'))
img = img.convert('RGB')
img.show()
img.save(str(5) + '.png')
