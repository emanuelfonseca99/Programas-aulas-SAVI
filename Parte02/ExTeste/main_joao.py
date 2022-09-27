#!/usr/bin/env python3

import numpy as np  # shortcut or alias
import cv2


def main():

    print('Creating a new image')
    image_in_main = createImage()

    print('Darkening image')
    image_in_main_darkened = darkenImage(image_in_main)

    cv2.imshow('window', image_in_main_darkened)
    pressed_key = cv2.waitKey(0)
    print('You pressed key = ' + str(chr(pressed_key)))


def createImage():
    image_in_create_image = np.random.randint(0, high=255, size=(240,320), dtype=np.uint8)
    # when indexing matrices use a row,col (y,x) order
    return image_in_create_image

def darkenImage(image_to_darken):
    print(image_to_darken.dtype)
    image_darkened = (image_to_darken * 0.5).astype(np.uint8)
    print(image_darkened.dtype)
    return image_darkened



if __name__ == "__main__": # checks if code was called from terminal
    main() # call main function
