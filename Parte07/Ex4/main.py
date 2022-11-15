#!/usr/bin/env python3

import csv
import pickle
from copy import deepcopy
from random import randint, uniform
from turtle import color

import cv2
import numpy as np
import matplotlib.pyplot as plt
from models import Line
from colorama import Fore, Style
from scipy.optimize import least_squares


def main():

    # ------------------------------------------
    # Initialization
    # ------------------------------------------

    # Load file with points
    file = open('pts.pkl', 'rb')
    pts = pickle.load(file)
    file.close()
    print('pts = ' + str(pts))

    # Create figure
    plt.figure()
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    print('Created a figure.')

    # Draw ground truth pts
    plt.plot(pts['xs'], pts['ys'], 'sk', linewidth=2, markersize=6)


    # Define the model
    line = Line(pts) 
    best_line = Line(pts) 
    best_error = 1E6 # a very large number to start

    # ------------------------------------------
    # Execution
    # ------------------------------------------
    # Set new values
    line.randomizeParams()

    result = least_squares(line.objectiveFunction, [line.m, line.b], verbose=2)
        
    
    # ------------------------------------------
    # Termination
    # ------------------------------------------


if __name__ == "__main__":
    main()
