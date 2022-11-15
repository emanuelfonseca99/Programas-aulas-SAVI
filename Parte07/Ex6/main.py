#!/usr/bin/env python3

import pickle

import matplotlib.pyplot as plt
from models import Polynomial
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
    model = Polynomial(pts) 

    # ------------------------------------------
    # Execution
    # ------------------------------------------
    # Set new values
    model.randomizeParams()

    x0 = [model.a, model.b, model.c, model.d, model.e, model.f, model.g, model.h]
    result = least_squares(model.objectiveFunction, x0, verbose=2)
        
    model.draw()
    plt.show()
    
    # ------------------------------------------
    # Termination
    # ------------------------------------------


if __name__ == "__main__":
    main()
