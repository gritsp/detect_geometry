import cv2
import numpy as np
from color import Colors

def on_trackbar(v):
    pass


def openCamera():
    cap = cv2.VideoCapture(1)

    if cap.isOpened() == False:
        print('can not open camera')

    while cap.isOpened:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        col = Colors(frame)
        
        if ret == True:            
            cv2.imshow('shapes', col.findGeometry())
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        else:
            break
    
def getRangeColor():
    cv2.namedWindow('value', cv2.WINDOW_FREERATIO)
    cv2.createTrackbar('H min','value',0,180,on_trackbar)
    cv2.createTrackbar('H max','value',0,180,on_trackbar)
    cv2.createTrackbar('S min','value',0,255,on_trackbar)
    cv2.createTrackbar('S max','value',0,255,on_trackbar)
    cv2.createTrackbar('V min','value',0,255,on_trackbar)
    cv2.createTrackbar('V max','value',0,255,on_trackbar)
    

    cap = cv2.VideoCapture(1)

    if cap.isOpened() == False:
        print('can not open camera')

    while cap.isOpened:
        ret, frame = cap.read()
        h_min = cv2.getTrackbarPos('H min','value')
        h_max = cv2.getTrackbarPos('H max','value')
        s_min = cv2.getTrackbarPos('S min','value')
        s_max = cv2.getTrackbarPos('S max','value')
        v_min = cv2.getTrackbarPos('V min','value')
        v_max = cv2.getTrackbarPos('V max','value')
        if ret == True:
            cv2.imshow('Frame',frame)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            cv2.imshow('hsv',hsv)
            mask = cv2.inRange(hsv,(h_min,s_min,v_min),(h_max,s_max,v_max))
            cv2.imshow('mask',mask)
            kernal = np.ones((5,5), np.uint8)
            kernal2 = np.ones((9,9), np.uint8)            
            erosion = cv2.erode(mask,kernal)
            cv2.imshow('erosion',erosion)
            dilation = cv2.dilate(mask,kernal)
            cv2.imshow('dilation',dilation)
            closing = cv2.dilate(erosion,kernal2)
            cv2.imshow('closing',closing)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break


def main():
    print('1 : Choose range color\n2 : Open Camera')
    i = str(input('>'))
    while i!='1' and i!='2':
        print('1 : Choose range color\n2 : Open Camera')
        i = str(input('?>'))
        if i=='1' or i=='2':
            break
    if i=='1':
        getRangeColor()
    else:
        openCamera()
    cv2.destoryAllWindows()

if __name__ == '__main__':
    main()
