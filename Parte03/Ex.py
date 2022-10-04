#!/usr/bin/env python3

import cv2
import numpy as np

def main():

    cap = cv2.VideoCapture("/home/rafael/Desktop/savi_22-23/Parte03/docs/traffic.mp4")
    if (cap.isOpened()== False):
        print("Error opening video stream or file")

    while(cap.isOpened()):
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if ret == True:
            cv2.imshow('Frame',frame)

    
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()