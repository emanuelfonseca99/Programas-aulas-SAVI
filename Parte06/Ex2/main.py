#!/usr/bin/env python3

import csv
from copy import deepcopy
from random import randint
from turtle import color

import cv2
import numpy as np


def main():

    # ------------------------------------------
    # Initialization
    # ------------------------------------------
    image1_path = '../images/santorini/1.png'
    image1 = cv2.imread(image1_path)

    # ------------------------------------------
    # Execution
    # ------------------------------------------

    gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)

    # Create sift detection object
    sift = cv2.SIFT_create(nfeatures=500)

    # Create key_points
    key_points, des = sift.detectAndCompute(gray1,None) # SIFT features

    # Draw keypoints using opencv's function
    # image1 = cv2.drawKeypoints(image1,key_points,image1)

    # Draw keypoints 
    print(key_points)
    for idx, key_point in enumerate(key_points):
        # print('key_point ' + str(idx) + ': ' + str(key_point))
        # print('x=' + str(key_point.pt[0]))
        # print('y=' + str(key_point.pt[1]))
        x = int((key_point.pt[0]))
        y = int((key_point.pt[1]))
        color = (randint(0,255), randint(0,255), randint(0,255))
        cv2.circle(image1, (x,y), 80, color, 3)

    # Visualize
    cv2.namedWindow('Image1', cv2.WINDOW_NORMAL)
    cv2.imshow('Image1', image1)
    cv2.waitKey(0)



    # ------------------------------------------
    # Termination
    # ------------------------------------------

if __name__ == "__main__":
    main()
