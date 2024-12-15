import os
#Addressing slow startup issue with logicool web camera
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
import sys
import subfunc

args = sys.argv

#----------------------------------------
#variable
#----------------------------------------
devno = 0       #0,1,... Depends on device connection order and USB port
isFullScreen = False        #fullscreen toggle
isFlipLR = False            #flip (mirror mode) toggle
modeRotate = 0              #rotate 0:0 degrees,1:90 degrees, 2:180 degrees, 3:270 degrees

#----------------------------------------
#init
#----------------------------------------
#Addressing slow startup issue with logicool web camera
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

# Set as device number if argument
if len(args) > 1:
    argnum = int(args[1])
    if argnum > 0 and argnum < 3:
        devno = argnum

subfunc.dbgprint("cv video init.")
cap = cv2.VideoCapture(devno)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)   #FullHD 1920x1080
cap.set(cv2.CAP_PROP_FPS, 30)             #30fps

#----------------------------------------
#function
#----------------------------------------
def cv2_imgshow(winname, img, bfscr):
    #ToDo:FullScreen mode
    """
    if isFullScreen:
        cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(winname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    """
    cv2.imshow(winname, img)

subfunc.dbgprint("LOOP start.")
#----------------------------------------
#LOOP
#----------------------------------------
while True:
    _, img = cap.read()
    tick = cv2.getTickCount()

    if isFlipLR:
        img = cv2.flip(img, 1)
    if modeRotate == 1:
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)          #90 degrees
    elif modeRotate == 2:
        img = cv2.rotate(img, cv2.ROTATE_180)                   #180 degrees
    elif modeRotate == 3:
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)   #270 degrees

    #draw webcam image
    cv2_imgshow("Image", img, isFullScreen)

    #key check
    key = cv2.waitKey(1)
    prop_val = cv2.getWindowProperty('Image', cv2.WND_PROP_ASPECT_RATIO)
    if key != -1:
        print(key)
    if key == 27: break     #esc  exit
    if key == 113: break    #q    exit
    if prop_val < 0: break  #exit from close button
    if key == 114:          #r    Flip
      isFlipLR = not isFlipLR
    if key == 116:          #t    Rotate
        modeRotate += 1
        if modeRotate > 3: modeRotate = 0
    if key == 102:          #f    FullScreen
        isFullScreen = not isFullScreen

cap.release()
subfunc.dbgprint("LOOP end.")
