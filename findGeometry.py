import cv2
import numpy as np

class geometryColor:
    def __init__(self,frame):
        self.frame = frame
        self.hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    def isColor(self,pixel):
        if 0<=pixel[0]<=180 and 0<=pixel[1]<255 and pixel[2]<30:
            return 'Black'
        elif 0<=pixel[0]<=180 and pixel[1]<50 and 180<=pixel[2]:
            return 'White'
        elif 0<=pixel[0]<=180 and pixel[1]<50 and 50<=pixel[2]<=180:
            return 'Gray'
        elif 5<=pixel[0]<25 and 25<=pixel[1] and 25<=pixel[2]<180:
            return 'Brown'

        elif (pixel[0]<10 or 175<=pixel[0]) and 25<=pixel[1] and 25<=pixel[2]:
            return 'Red'            
        elif 10<=pixel[0]<25 and 25<=pixel[1] and 180<=pixel[2]:
            return 'Orange'        
        elif 25<=pixel[0]<35 and 25<=pixel[1] and 25<=pixel[2]:
            return 'Yellow'
        elif 35<=pixel[0]<90 and 25<=pixel[1] and 25<=pixel[2]:
            return 'Green'
        elif 90<=pixel[0]<130 and 25<=pixel[1] and 25<=pixel[2]:
            return 'Blue'
        elif 130<=pixel[0]<160 and 25<=pixel[1] and 25<=pixel[2]:
            return 'Purple'
        elif 160<=pixel[0]<175 and 25<=pixel[1] and 25<=pixel[2]:
            return 'Pink'
        else:
            print(pixel)
            return 'Unknow'

    def mask(self,th):
        img_gray = cv2.cvtColor(self.frame,cv2.COLOR_BGR2GRAY)
        _,binary = cv2.threshold(img_gray,th,255,cv2.THRESH_BINARY)
        kernal = np.ones((5,5), np.uint8)
        erosion = cv2.erode(binary,kernal)
        return erosion

    def findGeometry(self,thres):
        contours , hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1] - 5
            M = cv2.moments(contour)
            cX = int(M["m10"] / (M["m00"]+1))
            cY = int(M["m01"] / (M["m00"]+1))
            color = self.isColor(self.hsv[cY,cX])
            cv2.drawContours(self.frame, [approx], 0, (255,255,255), 2)         
        
            if len(approx) == 3:
                cv2.putText(self.frame, "Triangle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            elif len(approx) == 4 :
                cv2.putText(self.frame, "rectangle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            elif len(approx) == 5 :
                cv2.putText(self.frame, "pentagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            elif len(approx) == 10 :
                cv2.putText(self.frame, "star, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            elif len(approx) == 6 :
                cv2.putText(self.frame, "Hexagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            elif len(approx) == 8 :
                cv2.putText(self.frame, "Octagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            else:
                cv2.putText(self.frame, "circle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        return self.frame