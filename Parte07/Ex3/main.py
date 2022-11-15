#!/usr/bin/env python3

import pickle

import matplotlib.pyplot as plt
from models import Sinusoid
from colorama import Fore, Style


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
    best_model = Sinusoid(pts) 
    best_error = 1E6 # a very large number to start

    # ------------------------------------------
    # Execution
    # ------------------------------------------
    while True: # iterate setting new values for the params and recomputing the error

        # Set new values
        model.randomizeParams()

        # Compute error
        error = model.objectiveFunction()
        print(error)

        if error < best_error: # we found a better model!!!
            best_model.a = model.a # copy the best found line params
            best_model.b = model.b
            best_model.h = model.h
            best_model.k = model.k
            best_error = error # update best error
            print(Fore.RED + 'We found a better model!!!' + Style.RESET_ALL)

        # Draw current model
        model.draw()
        best_model.draw('r-')


        plt.waitforbuttonpress(0.01)
        if not plt.fignum_exists(1): # a way to do a clean termination
            print('Terminating')
            break



    # ------------------------------------------
    # Termination
    # ------------------------------------------


if __name__ == "__main__":
    main()
