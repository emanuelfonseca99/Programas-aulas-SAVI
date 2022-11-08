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
    # Two images, query (q) and target (t)
    q_path = '../images/castle/1.png'
    q_image = cv2.imread(q_path)
    q_gui = deepcopy(q_image)
    q_gray = cv2.cvtColor(q_image,cv2.COLOR_BGR2GRAY)
    q_win_name = 'Query Image'

    t_path = '../images/castle/2.png'
    t_image = cv2.imread(t_path)
    t_gui = deepcopy(t_image)
    t_gray = cv2.cvtColor(t_image,cv2.COLOR_BGR2GRAY)
    t_win_name = 'Target Image'

    # ------------------------------------------
    # Execution
    # ------------------------------------------
    # Create sift detection object
    sift = cv2.SIFT_create(nfeatures=200)

    # Detect keypoints in both images
    q_key_points, q_des = sift.detectAndCompute(q_gray,None) # SIFT features
    t_key_points, t_des = sift.detectAndCompute(t_gray,None) # SIFT features

    # Match features (FLANN based matching)
    index_params = dict(algorithm = 1, trees = 15)
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    best_two_matches = flann.knnMatch(q_des, t_des,k=2)

    # Create a list containing only the best matches, and use David Lowe's ratio test to compute the uniqueness of a match
    matches = []
    for best_two_match in best_two_matches:
        best_match = best_two_match[0]
        second_best_match = best_two_match[1]

        # David Lowe's test
        if  best_match.distance < 0.3 * second_best_match.distance:
            matches.append(best_match)

    # print(matches)

    # Visualize ----------------------

    # Draw keypoints 
    for idx, key_point in enumerate(q_key_points):
        x = int((key_point.pt[0]))
        y = int((key_point.pt[1]))
        color = (randint(0,255), randint(0,255), randint(0,255))
        cv2.circle(q_gui, (x,y), 30, color, 3)

    for idx, key_point in enumerate(t_key_points):
        x = int((key_point.pt[0]))
        y = int((key_point.pt[1]))
        color = (randint(0,255), randint(0,255), randint(0,255))
        cv2.circle(t_gui, (x,y), 30, color, 3)

    # Show the matches image
    matches_image = cv2.drawMatches(q_image, q_key_points,
                                    t_image, t_key_points, matches,None)

    cv2.namedWindow(q_win_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(q_win_name, 600, 400)
    cv2.imshow(q_win_name, q_gui)

    cv2.namedWindow(t_win_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(t_win_name, 600, 400)
    cv2.imshow(t_win_name, t_gui)

    cv2.namedWindow('Matches', cv2.WINDOW_NORMAL)
    cv2.imshow('Matches', matches_image)

    cv2.waitKey(0)



    # ------------------------------------------
    # Termination
    # ------------------------------------------

if __name__ == "__main__":
    main()
