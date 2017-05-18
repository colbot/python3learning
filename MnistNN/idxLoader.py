import os
import gzip
import struct
import numpy as np


def get_images(path):
    if not path:
        print("Please specify a file ")
        return
    if not os.path.exists(path):
        print("File '%s' not found ".format(path))
        return
    if path.endswith('.gz'):
        f = gzip.open(path, 'rb')
    else:
        f = open(path, 'rb')
    fbin = f.read()
    pos = 0
    fmt_header = '>iiii'
    magic, num_img, num_row, num_col = struct.unpack_from(fmt_header, fbin, pos)
    img_size = num_row * num_col
    pos += struct.calcsize(fmt_header)

    fmt_img = '>'+str(img_size)+'B'
    ofs_img = struct.calcsize(fmt_img)
    images = np.empty([num_img, img_size])
    for i in range(num_img):
        images[i] = np.array(struct.unpack_from(fmt_img, fbin, pos))
        pos += ofs_img

    return images


def get_labels(path):
    if not path:
        print("Please specify a file ")
        return
    if not os.path.exists(path):
        print("File '%s' not found ".format(path))
        return
    if path.endswith('.gz'):
        f = gzip.open(path, 'rb')
    else:
        f = open(path, 'rb')
    fbin = f.read()
    pos = 0
    fmt_header = '>ii'
    magic, num_lab = struct.unpack_from(fmt_header, fbin, pos)
    pos += struct.calcsize(fmt_header)

    fmt_lab = '>B'
    ofs_lab = struct.calcsize(fmt_lab)
    labels = np.empty(num_lab, dtype=int)
    for i in range(num_lab):
        labels[i] = np.array(struct.unpack_from(fmt_lab, fbin, pos))[0]
        pos += ofs_lab

    return labels


def load(path):
    if not os.path.exists(path) or not os.path.isdir(path):
        print("Please specify a path for data !")
        return
    train_images = get_images(path+os.sep+"train-images-idx3-ubyte.gz")
    train_labels = get_labels(path+os.sep+"train-labels-idx1-ubyte.gz")
    train_data = []
    for img, label in zip(train_images, train_labels):
        tmp = np.zeros(10)
        tmp[label] = 1
        train_data.append((img, tmp))

    test_images = get_images(path + os.sep + "t10k-images-idx3-ubyte.gz")
    test_labels = get_labels(path + os.sep + "t10k-labels-idx1-ubyte.gz")
    test_data = []
    for img, label in zip(test_images, test_labels):
        tmp = np.zeros(10)
        tmp[label] = 1
        test_data.append((img, tmp))
    return (train_data, test_data)