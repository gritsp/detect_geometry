import cv2
import numpy as np

def isColor(color):
    # color[0] = color[0]*2
    if 0<=color[0]<=180 and 0<=color[1]<255 and color[2]<25:
        return 'Black'
    elif 0<=color[0]<=180 and color[1]<50 and 180<=color[2]:
        return 'White'
    elif 0<=color[0]<=180 and color[1]<50 and 50<=color[2]<=180:
        return 'Gray'
    elif 5<=color[0]<25 and 25<=color[1] and 25<=color[2]:
        return 'Brown'

    elif (color[0]<10 or 175<=color[0]) and 25<=color[1] and 25<=color[2]:
        return 'Red'
    # elif (color[0]<15 or 345<=color[0]) and color[1]<179 and 25<=color[2]:
    #     return 'Pink'
    
    elif 10<=color[0]<25 and 25<=color[1] and 25<=color[2]:
        return 'Orange'
    
    elif 25<=color[0]<35 and 25<=color[1] and 25<=color[2]:
        return 'Yellow'
    elif 35<=color[0]<90 and 25<=color[1] and 25<=color[2]:
        # print(color)
        return 'Green'
    # elif 106<=color[0]<127 and 38<=color[1] and 25<=color[2]:
    #     return 'Blue-Green'
    elif 110<=color[0]<130 and 25<=color[1] and 25<=color[2]:
        return 'Blue'
    elif 130<=color[0]<160 and 25<=color[1] and 25<=color[2]:
        return 'Purple'
    # elif 220<=color[0]<255 and 38<=color[1]<127 and 25<=color[2]:
    #     return 'Light-Purple'
    elif 160<=color[0]<175 and 25<=color[1] and 25<=color[2]:
        return 'Pink'

def img():
    img = './test1.jpg'
    img = cv2.imread(img)
    # img = cv2.imread(i)
    h,w,c = img.shape
    newWidth = 800
    newHight = newWidth*h//w
    img = cv2.resize(img,(newWidth,newHight),interpolation = cv2.INTER_AREA)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,binary = cv2.threshold(img_gray,70,255,cv2.THRESH_BINARY)
    kernal = np.ones((5,5), np.uint8)
    # kernal2 = np.ones((9,9), np.uint8)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv',hsv)
    erosion = cv2.erode(binary,kernal)
    cv2.imshow('erosion',erosion)
    contours , hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, (255, 255, 255), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        M = cv2.moments(contour)
        cX = int(M["m10"] / (M["m00"]+1))
        cY = int(M["m01"] / (M["m00"]+1))
        
        color = str(isColor(hsv[cY,cX]))
        print(hsv[cY,cX])
        # color = 'Unknow'
        if len(approx) == 3:
            cv2.putText( img, "Triangle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1 )
        elif len(approx) == 4 :
            cv2.putText(img, "rectangle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)

        elif len(approx) == 5 :
            cv2.putText(img, "pentagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)
        elif len(approx) == 10 :
            cv2.putText(img, "star, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)
        elif len(approx) == 6 :
            cv2.putText(img, "Hexagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)
        elif len(approx) == 8 :
            cv2.putText(img, "Octagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)
        else:
            cv2.putText(img, "circle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)

    cv2.imshow('shapes', img)
    cv2.imshow('binary',binary)
    # cv2.imshow('img',img)
    cv2.waitKey(0)

def vdo():
    cap = cv2.VideoCapture(1)
    
    while True:
        _, img = cap.read()
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        _,binary = cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY)
        kernal = np.ones((5,5), np.uint8)
        # kernal2 = np.ones((9,9), np.uint8)
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        cv2.imshow('hsv',hsv)
        erosion = cv2.erode(binary,kernal)
        cv2.imshow('erosion',erosion)
        contours , hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
            cv2.drawContours(img, [approx], 0, (255, 255, 255), 5)
            x = approx.ravel()[0]
            y = approx.ravel()[1] - 5
            M = cv2.moments(contour)
            cX = int(M["m10"] / (M["m00"]+1))
            cY = int(M["m01"] / (M["m00"]+1))
            color = str(isColor(hsv[cY,cX]))
            # color = 'Unknow'
            if len(approx) == 3:
                cv2.putText( img, "Triangle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1 )
            elif len(approx) == 4 :
                cv2.putText(img, "rectangle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)

            elif len(approx) == 5 :
                cv2.putText(img, "pentagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)
            elif len(approx) == 10 :
                cv2.putText(img, "star, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)
            elif len(approx) == 6 :
                cv2.putText(img, "Hexagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)
            elif len(approx) == 8 :
                cv2.putText(img, "Octagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)
            else:
                cv2.putText(img, "circle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1)

        cv2.imshow('shapes', img)



        # cv2.imshow('binary',binary)
        # cv2.imshow('img',img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# vdo()
img()