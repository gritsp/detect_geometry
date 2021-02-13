import cv2
import numpy as np
from findGeometry import geometryColor

def on_trackbar(v):
    pass

def openVideoCapture(thresh):
    cap = cv2.VideoCapture(1)
    cap.set(3, 1280)
    cap.set(4, 720)
    if cap.isOpened() == False:
        print('can not open camera')

    while cap.isOpened:
        ret, frame = cap.read()
        frame = geometryColor(frame)
        mask = frame.mask(thresh)
        
        if ret == True:            
            cv2.imshow('shapes', frame.findGeometry(mask))
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        else:
            break

def threshRange():
    cv2.namedWindow('value', cv2.WINDOW_FREERATIO)
    cv2.createTrackbar('Threshold Value','value',0,255,on_trackbar)
    cap = cv2.VideoCapture(1)

    if cap.isOpened() == False:
        print('can not open camera')

    while cap.isOpened:
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        thresh = cv2.getTrackbarPos('Threshold Value','value')
        _,binary = cv2.threshold(frame,thresh,255,cv2.THRESH_BINARY)
        cv2.imshow('Threshold',binary)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        
        


def main():
    while True:
        print('1 : Choose threshold range\n2 : Open Camera\n3 : Exit')
        i = str(input('> '))
        while i!='1' and i!='2' and i!='3':
            print('1 : Choose threshold range\n2 : Open Camera\n3 : Exit')
            i = str(input('?> '))
            if i=='1' or i=='2' or i=='3':
                break
        if i=='1':
            threshRange()
            cv2.destroyAllWindows()
        elif i == '2':
            print('Input Threshold value')
            thresh = int(input('> '))
            # print(type(thresh))
            openVideoCapture(thresh)
            cv2.destroyAllWindows()
        else:
            break
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()