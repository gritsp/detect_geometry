import cv2
import numpy as np

def on_trackbar(v):
    pass

cv2.namedWindow('value')
cv2.createTrackbar('h max','value',0,255,on_trackbar)
cv2.createTrackbar('h min','value',0,255,on_trackbar)
cv2.createTrackbar('s max','value',0,255,on_trackbar)
cv2.createTrackbar('s min','value',0,255,on_trackbar)
cv2.createTrackbar('v max','value',0,255,on_trackbar)
cv2.createTrackbar('v min','value',0,255,on_trackbar)

def isColor2(color):
    color[0] = color[0]*2
    if 0<=color[0]<360 and 0<=color[1]<255 and color[2]<25:
        return 'Black'
    elif 0<=color[0]<360 and color[1]<38 and 165<=color[2]:
        return 'White'
    elif 0<=color[0]<360 and color[1]<38 and 25<=color[2]<=165:
        return 'Gray'
    elif (color[0]<15 or 345<=color[0]) and 179<=color[1] and 25<=color[2]:
        return 'Red'
    elif (color[0]<15 or 345<=color[0]) and color[1]<179 and 25<=color[2]:
        return 'Pink'
    elif 285<=color[0]<345 and 38<=color[1] and 25<=color[2]:
        return 'Pink'
    elif 15<=color[0]<45 and 38<=color[1] and 191<=color[2]:
        return 'Orange'
    elif 8<=color[0]<32 and 38<=color[1] and 25<=color[2]<191:
        return 'Brown'
    elif 45<=color[0]<75 and 38<=color[1] and 25<=color[2]:
        return 'Yellow'
    elif 75<=color[0]<165 and 38<=color[1] and 25<=color[2]:
        return 'Green'
    # elif 106<=color[0]<127 and 38<=color[1] and 25<=color[2]:
    #     return 'Blue-Green'
    elif 165<=color[0]<255 and 38<=color[1] and 25<=color[2]:
        return 'Blue'
    elif 255<=color[0]<285 and 127<=color[1] and 25<=color[2]:
        return 'Purple'
    # elif 220<=color[0]<255 and 38<=color[1]<127 and 25<=color[2]:
    #     return 'Light-Purple'

def isColor(color):
    color[0] = color[0]*2*255/360
    if 0<=color[0]<255 and 0<=color[1]<255 and color[2]<25:
        return 'Black'
    elif 0<=color[0]<255 and color[1]<38 and 165<=color[2]:
        return 'White'
    elif 0<=color[0]<255 and color[1]<38 and 25<=color[2]<=165:
        return 'Gray'
    elif (color[0]<8 or 249<=color[0]) and 179<=color[1] and 25<=color[2]:
        return 'Red'
    elif (color[0]<8 or 249<=color[0]) and color[1]<179 and 25<=color[2]:
        return 'Pink'
    elif 220<=color[0]<249 and 38<=color[1] and 25<=color[2]:
        return 'Pink'
    elif 8<=color[0]<32 and 38<=color[1] and 191<=color[2]:
        return 'Orange'
    elif 8<=color[0]<32 and 38<=color[1] and 25<=color[2]<191:
        return 'Brown'
    elif 32<=color[0]<45 and 38<=color[1] and 25<=color[2]:
        return 'Yellow'
    elif 45<=color[0]<106 and 38<=color[1] and 25<=color[2]:
        return 'Green'
    elif 106<=color[0]<127 and 38<=color[1] and 25<=color[2]:
        return 'Blue-Green'
    elif 127<=color[0]<180 and 38<=color[1] and 25<=color[2]:
        return 'Blue'
    elif 180<=color[0]<220 and 127<=color[1] and 25<=color[2]:
        return 'Purple'
    elif 220<=color[0]<255 and 38<=color[1]<127 and 25<=color[2]:
        return 'Light-Purple'


def vedioCapture():
    # cv2.namedWindow('value')
    # cv2.createTrackbar('h max','value',0,255,on_trackbar)
    # cv2.createTrackbar('h min','value',0,255,on_trackbar)
    # cv2.createTrackbar('s max','value',0,255,on_trackbar)
    # cv2.createTrackbar('s min','value',0,255,on_trackbar)
    # cv2.createTrackbar('v max','value',0,255,on_trackbar)
    # cv2.createTrackbar('v min','value',0,255,on_trackbar)

    cap = cv2.VideoCapture(1)

    if cap.isOpened() == False:
        print('can not open camera')

    ret, frame = cap.read()
    img_draw = np.zeros(frame.shape)

    while cap.isOpened():
        ret, frame = cap.read()
        img = frame
        h_max = cv2.getTrackbarPos('h max','value')
        h_min = cv2.getTrackbarPos('h min','value')
        s_max = cv2.getTrackbarPos('s max','value')
        s_min = cv2.getTrackbarPos('s min','value')
        v_max = cv2.getTrackbarPos('v max','value')
        v_min = cv2.getTrackbarPos('v min','value')

        
        # img[y,x] = (255,22,0)
        if ret == True:
            cv2.imshow('Frame',img)
            imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            # cv2.imshow('hsv',hsv)
            ret , mask1 = cv2.threshold(imgGry, s_min , 255, cv2.CHAIN_APPROX_NONE)
            # mask1 = cv2.inRange(hsv,(h_min,s_min,v_min),(h_max,s_max,v_max))
            # min(0,0,135) max(255,38,255) เปิดไฟ
            # mask1 = cv2.inRange(hsv,(0,0,135),(255,38,255))
            cv2.imshow('mask1',mask1)

            kernal = np.ones((5,5), np.uint8)
            kernal2 = np.ones((9,9), np.uint8)
            
            erosion = cv2.erode(mask1,kernal)
            cv2.imshow('erosion',erosion)
            # dilation = cv2.dilate(mask1,kernal)
            # cv2.imshow('dilation',dilation)
            closing = cv2.dilate(erosion,kernal2)
            # cv2.imshow('closing',closing)

            contours , hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            for contour in contours:
                approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
                cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
                x = approx.ravel()[0]
                y = approx.ravel()[1] - 5
                M = cv2.moments(contour)
                cX = int(M["m10"] / (M["m00"]+1))
                cY = int(M["m01"] / (M["m00"]+1))
                color = str(isColor(hsv[cY,cX]))
                if len(approx) == 3:
                    cv2.putText( img, "Triangle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0) )
                elif len(approx) == 4 :
                    cv2.putText(img, "rectangle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))

                elif len(approx) == 5 :
                    cv2.putText(img, "pentagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
                elif len(approx) == 10 :
                    cv2.putText(img, "star, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
                elif len(approx) == 6 :
                    cv2.putText(img, "Hexagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
                elif len(approx) == 8 :
                    cv2.putText(img, "Octagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
                else:
                    cv2.putText(img, "circle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))

            cv2.imshow('shapes', img)

         

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

def image():
    img = cv2.imread('./test1.jpg')
    
    cv2.imshow('img',img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret , thrash = cv2.threshold(imgGry, 200 , 255, cv2.CHAIN_APPROX_NONE)
    
    cv2.imshow('thresh',thrash)

    # mask1 = cv2.inRange(hsv,(0,0,135),(255,38,255))

    kernal = np.ones((5,5), np.uint8)
    # kernal2 = np.ones((9,9), np.uint8)
    
    erosion = cv2.erode(thrash,kernal)
    cv2.imshow('erosion',erosion)
    # dilation = cv2.dilate(mask1,kernal)
    # cv2.imshow('dilation',dilation)
    # closing = cv2.dilate(erosion,kernal2)
    # cv2.imshow('closing',closing)

    contours , hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, (0, 0, 0), 3)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        color = str(isColor(hsv[cY,cX]))
        if len(approx) == 3:
            cv2.putText( img, "Triangle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0) )
        elif len(approx) == 4 :
            cv2.putText(img, "rectangle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))

        elif len(approx) == 5 :
            cv2.putText(img, "pentagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
        elif len(approx) == 10 :
            cv2.putText(img, "star, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
        elif len(approx) == 6 :
            cv2.putText(img, "Hexagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
        elif len(approx) == 8 :
            cv2.putText(img, "Octagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
        else:
            cv2.putText(img, "circle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))

    cv2.imshow('shapes', img)

    cv2.imshow('shapes', img)
    cv2.waitKey(0)        

def resize(newWidth,img):
    hight, width, chanel = img.shape
    newHight = newWidth*hight//width
    return cv2.resize(img,(newWidth, newHight), interpolation = cv2.INTER_AREA)

# imgPath = './test1.jpg'

# img = cv2.imread(imgPath)

# img = resize(800,img)
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# vedioCapture()
image()
# min(0,0,135) max(255,38,255)
cv2.destoryAllWindows()