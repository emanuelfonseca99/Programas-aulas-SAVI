#!/usr/bin/env python3

import pickle

import matplotlib.pyplot as plt
from models import Sinusoid
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
    model = Sinusoid(pts) 
    best_line = Sinusoid(pts) 

    # ------------------------------------------
    # Execution
    # ------------------------------------------
    # Set new values
    model.randomizeParams()

    result = least_squares(model.objectiveFunction, [model.a, model.b, model.h, model.k], verbose=2)
        
    
    # ------------------------------------------
    # Termination
    # ------------------------------------------


if __name__ == "__main__":
    main()
