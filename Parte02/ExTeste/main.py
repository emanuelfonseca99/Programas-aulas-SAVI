#!/usr/bin/env python3

import numpy as np  # shortcut or alias
import cv2


def main():


    print('Creating a new image')
    # image = np.ndarray((240,320,3), dtype=np.uint8)
    image = np.random.randint(0, high=255, size=(240,320), dtype=np.uint8)
    # when indexing matrices use a row,col (y,x) order

    # Set image to gray
    # image = image*0 + 128
    # image += 128 # is the same as "image = image + 128"

    cv2.imshow('window', image)
    pressed_key = cv2.waitKey(0)

    print('You pressed key = ' + str(chr(pressed_key)))


if __name__ == "__main__": # checks if code was called from terminal
    main() # call main function
