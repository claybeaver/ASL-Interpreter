###################################
### Web Camera Hand Recognition ###
###################################

###################################
### ********* NOTES *********** ###
### Spacebar = Save Screenshot ####
### Escape = Cancel Application ###
### *************************** ###
###################################


import cv2

def show_webcam(mirror=False):

    cam = cv2.VideoCapture(0)
    img_counter = 1

    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)
        cv2.line
        
        xmin = 384
        xmax = 584
        ymin = 100
        ymax = 300

        square = cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), (0,0, 225), 3)
        
        if not ret:
            print("~~~~~~~  Try Again  ~~~~~~~")
            break
        cv2.imshow("Hand Capture", frame)
        
        k = cv2.waitKey(1)
        if k%256 == 27:  #--------------------> ESC pressed 
            print("~~~~~~~  Closing Program  ~~~~~~~")
            break
        elif k%256 == 32:  #------------------> SPACE pressed
            img_name = "hand_capture_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame[ymin:ymax, xmin:xmax]) #------> Crop to image to ROI
            print("~~~~~~~  {} has been saved  ~~~~~~~".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()

def main():
     show_webcam(mirror=True)

if __name__ == '__main__':
    main()