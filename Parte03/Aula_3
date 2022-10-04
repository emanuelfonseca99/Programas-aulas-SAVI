import cv2
from cv2 import rectangle
import numpy

def main():
    img = cv2.imread('/home/bachsoto/Desktop/SAVI/savi_22-23/Parte03/docs/highway.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
    cv2.rectangle(img, (150,500),(350,700), (0,255,0),2)
    cv2.rectangle(img, (400,500),(600,700), (0,255,0),2)
    cv2.rectangle(img, (700,500),(900,700), (0,255,0),2)
    cv2.rectangle(img, (1000,500),(1200,700), (0,255,0),2)


    cv2.imshow('Ẃindow', img)
    
    cv2.waitKey(0)

if __name__ == '__main__':
    main()