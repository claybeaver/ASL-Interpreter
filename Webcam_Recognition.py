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

    cam = cv2.VideoCapture(0)                       #-------------> Set to 0 (if using built in webcam) or 1 (for using camera)
    # img_counter = 1                               #-------------> Used for saving images to local computer

    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)                  #-------------> To activate mirror imaging
        
        (xmin, xmax, ymin, ymax) = (384, 584, 100, 300)
        
        (xmin2, xmax2, ymin2, ymax2) = (56, 256, 100, 300)

        cv2.rectangle(frame, (xmin-2,ymin-2), (xmax+2,ymax+2), (0,0, 225), 2)
        
        if not ret:
            print("~~~~~~~~~~~~           Try Again            ~~~~~~~~~~~~")
            break
        cv2.imshow("Hand Capture", frame)
        
        k = cv2.waitKey(1)
        if k%256 == 27:                            #--------------------> ESC pressed 
            print("~~~~~~~~~~~~       Terminating Program      ~~~~~~~~~~~~")
            break
        elif k%256 == 32:                          #------------------> SPACE pressed
            retval, image = cam.read()
            cropped = image[ymin2:ymax2, xmin2:xmax2]
            cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
            retval, buffer = cv2.imencode('.jpg', cropped)
            jpg_as_text = base64.b64encode(buffer)
            print("~~~~~~~~~~~~ Image Encoded to Base64 Format ~~~~~~~~~~~~")
            print(jpg_as_text)                     #-----------------> Test print for base64 string 
            print("~~~~~~~~~~~~ Image Encoded to Base64 Format ~~~~~~~~~~~~")  
            # img_name = "hand_capture_{}.jpg".format(img_counter)                # \
            # cv2.imwrite(img_name, frame[ymin:ymax, xmin:xmax])                  #  }----> Code to save image on local computer
            # print("~~~~~~~  {} has been saved  ~~~~~~~".format(img_name))       # /
            # img_counter += 1                                                    #/

    cam.release()

    cv2.destroyAllWindows()

def main():
     show_webcam(mirror=True)

if __name__ == '__main__':
    main()