import cv2
import numpy as np 

class Colors:
    def __init__(self,frame):
        self.frame = frame
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        # self.blackMinRange = (0,0,0)
        # self.blackMaxRange = (180,255,80)
        # self.whiteMinRange = (0,0,180)
        # self.whiteMaxRange = (180,70,255)
        # self.grayMinRange = (80,20,80)
        # self.grayMaxRange = (120,110,170)
        # self.brownMinRange = (5,20,20)
        # self.brownMaxRange = (20,250,190)
        # self.redMinRange = (160,97,100)
        # self.redMaxRange = (180,255,255)
        # self.orangeMinRange = (0,30,130)
        # self.orangeMaxRange = (25,110,200)
        # self.yellowMinRange = (30,20,130)
        # self.yellowMaxRange = (70,160,185)
        # self.greenMinRange = (80,130,120)
        # self.greenMaxRange = (100,180,160)
        # self.blueMinRange = (100,120,130)
        # self.blueMaxRange = (120,190,170)
        # self.purpleMinRange = (110,60,100)
        # self.purpleMaxRange = (160,100,130)
        # self.pinkMinRange = (100,50,160)
        # self.pinkMaxRange = (165,90,200)

        self.blackMinRange = (0,0,0)
        self.blackMaxRange = (180,255,25)
        self.whiteMinRange = (0,0,180)
        self.whiteMaxRange = (180,50,255)
        self.grayMinRange = (0,0,50)
        self.grayMaxRange = (180,50,180)

        self.brownMinRange = (5,25,25)
        self.brownMaxRange = (25,255,255)

        self.redMinRange = (0,25,25)
        self.redMaxRange = (10,255,255)

        self.red2min = (170,25,25)
        self.red2max = (180,255,255)

        self.orangeMinRange = (11,25,25)
        self.orangeMaxRange = (27,255,255)
        self.yellowMinRange = (28,25,25)
        self.yellowMaxRange = (35,255,255)
        self.greenMinRange = (36,25,25)
        self.greenMaxRange = (70,255,255)
        self.blueMinRange = (100,25,25)
        self.blueMaxRange = (130,255,255)
        self.purpleMinRange = (131,25,25)
        self.purpleMaxRange = (145,255,255)
        self.pinkMinRange = (146,25,25)
        self.pinkMaxRange = (169,255,255)
    
    def mask(self):
        blackRange = cv2.inRange(self.hsv, self.blackMinRange, self.blackMaxRange)
        whiteRange = cv2.inRange(self.hsv, self.whiteMinRange, self.whiteMaxRange)
        grayRange = cv2.inRange(self.hsv, self.grayMinRange, self.grayMaxRange)
        brownRange = cv2.inRange(self.hsv, self.brownMinRange, self.brownMaxRange)
        redRange = cv2.inRange(self.hsv, self.redMinRange, self.redMaxRange)
        orangeRange = cv2.inRange(self.hsv, self.orangeMinRange, self.orangeMaxRange)
        yellowRange = cv2.inRange(self.hsv, self.yellowMinRange, self.yellowMaxRange)
        greenRange = cv2.inRange(self.hsv, self.greenMinRange, self.greenMaxRange)
        blueRange = cv2.inRange(self.hsv, self.blueMinRange, self.blueMaxRange)
        purpleRange = cv2.inRange(self.hsv, self.purpleMinRange, self.purpleMaxRange)
        pinkRange = cv2.inRange(self.hsv, self.pinkMinRange, self.pinkMaxRange)
        
        bw = cv2.bitwise_or(blackRange,whiteRange)
        gb = cv2.bitwise_or(grayRange,brownRange)
        ro = cv2.bitwise_or(redRange,orangeRange)
        yg = cv2.bitwise_or(yellowRange,greenRange)
        bp = cv2.bitwise_or(blueRange,purpleRange)
        bwp = cv2.bitwise_or(bw,pinkRange)

        gbro = cv2.bitwise_or(gb,ro)
        ygbp = cv2.bitwise_or(yg,bp)
        gbro_ygbp = cv2.bitwise_or(gbro,ygbp)

        allRange = cv2.bitwise_or(bwp,gbro_ygbp)
        # cv2.imshow('mask',allRange)
        kernal = np.ones((5,5), np.uint8)
        kernal2 = np.ones((9,9), np.uint8)            
        erosion = cv2.erode(allRange,kernal)
        cv2.imshow('erosion',erosion)
        # dilation = cv2.dilate(allRange,kernal)
        # cv2.imshow('dilation',dilation)
        # closing = cv2.dilate(erosion,kernal2)
        # cv2.imshow('closing',closing)

        return erosion

    def isColor(self,pixel):
        if (pixel[0] in range(self.blackMinRange[0], self.blackMaxRange[0])) and (pixel[1] in range(self.blackMinRange[1], self.blackMaxRange[1])) and\
            (pixel[2] in range(self.blackMinRange[2], self.blackMaxRange[2])):
            return 'Black'
        elif (pixel[0] in range(self.whiteMinRange[0], self.whiteMaxRange[0])) and (pixel[1] in range(self.whiteMinRange[1], self.whiteMaxRange[1])) and\
            (pixel[2] in range(self.whiteMinRange[2], self.whiteMaxRange[2])):
            return 'white'
        elif (pixel[0] in range(self.grayMinRange[0], self.grayMaxRange[0])) and (pixel[1] in range(self.grayMinRange[1], self.grayMaxRange[1])) and\
            (pixel[2] in range(self.grayMinRange[2], self.grayMaxRange[2])):
            return 'gray'
        elif (pixel[0] in range(self.redMinRange[0], self.redMaxRange[0])) and (pixel[1] in range(self.redMinRange[1], self.redMaxRange[1])) and\
            (pixel[2] in range(self.redMinRange[2], self.redMaxRange[2])):
            return 'red'
        elif (pixel[0] in range(self.orangeMinRange[0], self.orangeMaxRange[0])) and (pixel[1] in range(self.orangeMinRange[1], self.orangeMaxRange[1])) and\
            (pixel[2] in range(self.orangeMinRange[2], self.orangeMaxRange[2])):
            return 'orange'
        elif (pixel[0] in range(self.brownMinRange[0], self.brownMaxRange[0])) and (pixel[1] in range(self.brownMinRange[1], self.brownMaxRange[1])) and\
            (pixel[2] in range(self.brownMinRange[2], self.brownMaxRange[2])):
            return 'brown'
        elif (pixel[0] in range(self.yellowMinRange[0], self.yellowMaxRange[0])) and (pixel[1] in range(self.yellowMinRange[1], self.yellowMaxRange[1])) and\
            (pixel[2] in range(self.yellowMinRange[2], self.yellowMaxRange[2])):
            return 'yellow'
        elif (pixel[0] in range(self.greenMinRange[0], self.greenMaxRange[0])) and (pixel[1] in range(self.greenMinRange[1], self.greenMaxRange[1])) and\
            (pixel[2] in range(self.greenMinRange[2], self.greenMaxRange[2])):
            return 'green'
        elif (pixel[0] in range(self.blueMinRange[0], self.blueMaxRange[0])) and (pixel[1] in range(self.blueMinRange[1], self.blueMaxRange[1])) and\
            (pixel[2] in range(self.blueMinRange[2], self.blueMaxRange[2])):
            return 'blue'
        elif (pixel[0] in range(self.purpleMinRange[0], self.purpleMaxRange[0])) and (pixel[1] in range(self.purpleMinRange[1], self.purpleMaxRange[1])) and\
            (pixel[2] in range(self.purpleMinRange[2], self.purpleMaxRange[2])):
            return 'purple'
        elif (pixel[0] in range(self.pinkMinRange[0], self.pinkMaxRange[0])) and (pixel[1] in range(self.pinkMinRange[1], self.pinkMaxRange[1])) and\
            (pixel[2] in range(self.pinkMinRange[2], self.pinkMaxRange[2])):
            return 'pink'
        else:
            return 'Unknow'
    
    def findGeometry(self):
        
        contours , hierarchy = cv2.findContours(self.mask(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1] - 5
            M = cv2.moments(contour)
            cX = int(M["m10"] / (M["m00"]+1))
            cY = int(M["m01"] / (M["m00"]+1))
            color = self.isColor(self.hsv[cY,cX])
            if color != 'Unknow':
                cv2.drawContours(self.frame, [approx], 0, (0, 0, 0), 2)          
            
                if len(approx) == 3:
                    cv2.putText(self.frame, "Triangle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0) )
                elif len(approx) == 4 :
                    cv2.putText(self.frame, "rectangle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
                elif len(approx) == 5 :
                    cv2.putText(self.frame, "pentagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
                elif len(approx) == 10 :
                    cv2.putText(self.frame, "star, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
                elif len(approx) == 6 :
                    cv2.putText(self.frame, "Hexagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
                elif len(approx) == 8 :
                    cv2.putText(self.frame, "Octagon, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
                else:
                    cv2.putText(self.frame, "circle, "+color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
        
        return self.frame