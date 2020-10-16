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
import base64

def show_webcam(mirror=False):

    cam = cv2.VideoCapture(1)
    img_counter = 1

    while True:
        ret, frame = cam.read()
        # frame = cv2.flip(frame, 1)  #-------------> To activate mirror imaging
        
        xmin = 50
        xmax = 250
        ymin = 100
        ymax = 300

        cv2.rectangle(frame, (xmin-2,ymin-2), (xmax+2,ymax+2), (0,0, 225), 2)
        
        if not ret:
            print("~~~~~~~  Try Again  ~~~~~~~")
            break
        cv2.imshow("Hand Capture", frame)
        
        k = cv2.waitKey(1)
        if k%256 == 27:  #--------------------> ESC pressed 
            print("~~~~~~~~~~~~  Terminating Program  ~~~~~~~~~~~~")
            break
        elif k%256 == 32:  #------------------> SPACE pressed
            retval, image = cam.read()
            cropped = image[ymin:ymax, xmin:xmax]
            retval, buffer = cv2.imencode('.jpg', cropped)
            jpg_as_text = base64.b64encode(buffer)
            # img_name = "hand_capture_{}.jpg".format(img_counter)
            # cv2.imwrite(img_name, frame[ymin:ymax, xmin:xmax]) #------> Crop to image to ROI
            # print("~~~~~~~  {} has been saved  ~~~~~~~".format(img_name))
            # img_counter += 1

    cam.release()

    cv2.destroyAllWindows()

def main():
     show_webcam(mirror=True)

if __name__ == '__main__':
    main()