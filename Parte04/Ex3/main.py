#!/usr/bin/env python3

import csv
from copy import deepcopy
from turtle import color

import cv2
import numpy as np
from functions import Detection, Tracker


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

    person_detector = cv2.CascadeClassifier('haarcascade_fullbody.xml')

    detection_counter = 0
    tracker_counter = 0
    trackers = []
    iou_threshold = 0.8

    # ------------------------------------------
    # Execution
    # ------------------------------------------
    frame_counter = 0
    while(cap.isOpened()): # this is an infinite loop

        # Step 1: get frame
        ret, image_rgb = cap.read() # get a frame, ret will be true or false if getting succeeds
        image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
        image_gui = deepcopy(image_rgb)
        if ret == False:
            break
        stamp = float(cap.get(cv2.CAP_PROP_POS_MSEC))/1000


        # ------------------------------------------
        # Detection of persons 
        # ------------------------------------------
        bboxes = person_detector.detectMultiScale(image_gray, scaleFactor=1.2, minNeighbors=4, minSize=(20,40))

        # ------------------------------------------
        # Create Detections per haar cascade bbox
        # ------------------------------------------
        detections = []
        for bbox in bboxes: 
            x1, y1, w, h = bbox
            detection = Detection(x1, y1, w, h, image_gray, id=detection_counter, stamp=stamp)
            detection_counter += 1
            detection.draw(image_gui)
            detections.append(detection)
            # cv2.imshow('detection ' + str(detection.id), detection.image  )

        # ------------------------------------------
        # For each detection, see if there is a tracker to which it should be associated
        # ------------------------------------------
        for detection in detections: # cycle all detections
            for tracker in trackers: # cycle all trackers
                tracker_bbox = tracker.detections[-1]
                iou = detection.computeIOU(tracker_bbox)
                # print('IOU( T' + str(tracker.id) + ' D' + str(detection.id) + ' ) = ' + str(iou))
                if iou > iou_threshold: # associate detection with tracker 
                    tracker.addDetection(detection, image_gray)

        # ------------------------------------------
        # Track using template matching
        # ------------------------------------------
        for tracker in trackers: # cycle all trackers
            last_detection_id = tracker.detections[-1].id
            print(last_detection_id)
            detection_ids = [d.id for d in detections]
            if not last_detection_id in detection_ids:
                print('Tracker ' + str(tracker.id) + ' Doing some tracking')
                tracker.track(image_gray)

        # ------------------------------------------
        # Deactivate Tracker if no detection for more than T
        # ------------------------------------------
        for tracker in trackers: # cycle all trackers
            tracker.updateTime(stamp)

        # ------------------------------------------
        # Create Tracker for each detection
        # ------------------------------------------
        for detection in detections:
            if not detection.assigned_to_tracker:
                tracker = Tracker(detection, id=tracker_counter, image=image_gray)
                tracker_counter += 1
                trackers.append(tracker)
    
        # ------------------------------------------
        # Draw stuff
        # ------------------------------------------

        # Draw trackers
        for tracker in trackers:
            tracker.draw(image_gui)

            # win_name= 'T' + str(tracker.id) + ' template'
            # cv2.imshow(win_name, tracker.template)

        # for tracker in trackers:
            # print(tracker)

        cv2.imshow(window_name,image_gui) # show the image

        if cv2.waitKey(50) == ord('q'):
            break

        frame_counter += 1


    # ------------------------------------------
    # Termination
    # ------------------------------------------
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
