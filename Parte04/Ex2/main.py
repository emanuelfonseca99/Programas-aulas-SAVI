#!/usr/bin/env python3

import csv
from copy import deepcopy
from turtle import color

import cv2
import numpy as np


def main():

    # ------------------------------------------
    # Initialization
    # ------------------------------------------
    cap = cv2.VideoCapture("../docs/OxfordTownCentre/TownCentreXVID.mp4")
    if (cap.isOpened()== False):
        print("Error opening video stream or file")

    window_name = 'image_rgb'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 800, 500)


    # Count number of persons in the dataset
    number_or_persons = 0
    csv_reader = csv.reader(open('../docs/OxfordTownCentre/TownCentre-groundtruth.top'))
    for row in csv_reader:
        if len(row) != 12: # skip badly formatted rows
            continue

        person_number, frame_number, _, _, _, _, _, _, body_left, body_top, body_right, body_bottom = row
        person_number = int(person_number) # convert to number format (integer)
        if person_number >= number_or_persons:
            number_or_persons = person_number + 1

    # Create the colors for each person
    colors = np.random.randint(0, high=255, size=(number_or_persons, 3), dtype=int)

    # ------------------------------------------
    # Execution
    # ------------------------------------------
    frame_counter = 0
    while(cap.isOpened()): # this is an infinite loop

        # Step 1: get frame
        ret, image_rgb = cap.read() # get a frame, ret will be true or false if getting succeeds
        image_gui = deepcopy(image_rgb)
        if ret == False:
            break
        stamp = float(cap.get(cv2.CAP_PROP_POS_MSEC))/1000


        # Draw ground truth bboxes
        csv_reader = csv.reader(open('../docs/OxfordTownCentre/TownCentre-groundtruth.top'))
        for row in csv_reader:

            if len(row) != 12: # skip badly formatted rows
                continue

            person_number, frame_number, _, _, _, _, _, _, body_left, body_top, body_right, body_bottom = row
            person_number = int(person_number) # convert to number format (integer)
            frame_number = int(frame_number)
            body_left = int(float(body_left))
            body_right = int(float(body_right))
            body_top = int(float(body_top))
            body_bottom = int(float(body_bottom))

            if frame_counter != frame_number: # do not draw bbox of other frames
                continue

            x1 = body_left
            y1 = body_top
            x2 = body_right
            y2 = body_bottom
            color = colors[person_number,:]

            cv2.rectangle(image_gui,(x1,y1),(x2,y2),(int(color[0]),int(color[1]),int(color[2])),3)

            print('person ' + str(person_number) + ' frame ' + str(frame_number))


        
        cv2.imshow(window_name,image_gui) # show the image

        if cv2.waitKey(25) == ord('q'):
            break

        frame_counter += 1


    # ------------------------------------------
    # Termination
    # ------------------------------------------
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
