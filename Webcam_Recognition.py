###################################
##### Web Camera Interaction ######
###################################


### ********* NOTES *********** ###
### Spacebar = Save Screenshot ####
### Escape = Cancel Application ###
### *************************** ###

### In Progress: working on building a segmented to screenshot for the hand ###

import cv2

def show_webcam(mirror=False):

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_counter = 0

    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            print("~~~~~~~ Try Again ~~~~~~~")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:  #--------------------> ESC pressed 
            print("~~~~~~~ Closing Program ~~~~~~~")
            break
        elif k%256 == 32:  #------------------> SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("~~~~~~~ {} has been saved ~~~~~~~".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()

def main():
     show_webcam(mirror=True)

if __name__ == '__main__':
    main()