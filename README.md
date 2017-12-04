# Problem Sheet 2: Read the MNIST data files
---
#### *Emerging Technologies - Lecturer: [Dr Ian McLoughlin](ianmcloughlin.github.io) - 4th Year (Hons) Software Development*
This repository contains solutions to [problem sheet 2](https://emerging-technologies.github.io/problems/mnist.html) for [Emerging Technologies](https://emerging-technologies.github.io/) 4th year module. These problems relate to the famous MNIST data set.

#### **_Solution can be found above in [mnist.py](https://github.com/ianburkeixiv/mnist-reader/blob/master/mnist.py)_**

## How to run
1. Click [here](https://github.com/ianburkeixiv/mnist-reader/archive/master.zip) to download zip of the repository
2. Unzip the repository in a directory e.g. Desktop
3. Open up a command terminal 
4. Enter the following to run each python script:
```bash
 python mnist.py
```

## How to clone this repository
1. Go to clone or download (should be on right side of the repository in green)
2. Copy the URL.
3. Open up git bash and change into a directory where you want to save the git repository.
4. Enter git clone followed by the link: 
```bash
git clone https://github.com/ianburkeixiv/mnist-reader.git
```
---
## mnist-reader
[MNIST]( http://yann.lecun.com/exdb/mnist/) is a famous dataset that consists of handwritten digits commonly used for training various image processing systems and also used in machine learning. The dataset contains 60,000 training images and 10,000 testing images. Each image is a 28x28 pixel square (784 pixels in total).
It is a popular database for people who want to try learning techniques and pattern recognition methods on real-world data while spending minimal efforts on preprocessing and formatting. 

![](https://www.tensorflow.org/images/mnist_digits.png)

## Python
The programming language used for this problem is sheet is [Python](https://www.python.org/)

---
## Objectives
---
### 1. Read the data files
Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.
### 2. Output an image to the console
Output the third image in the training set to the console. Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.
### 3. Output the image files as PNGs
Use Python to output the image files as PNGs, saving them in a subfolder in your repository. Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number (where it occurs in the data file) and Y is its label. For instance, the five-thousandth training image is labelled 2, so its file name should be train-04999-2.png. Note the images are indexed from 0, so the five-thousandth image is indexed as 4999. 

