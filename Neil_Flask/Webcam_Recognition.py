import cv2
import base64

class VideoCamera(object):
        def __init__(self):
            self.video = cv2.VideoCapture(1)
        
        def __del__(self):
            self.video.release()
        
        def get_frame(self):
            xmin = 384
            xmax = 584
            ymin = 100
            ymax = 300

            xmin2 = 56
            xmax2 = 256
            ymin2 = 100
            ymax2 = 300
        
            retval, image = self.video.read()
            image = cv2.flip(image, 1) 
            cv2.rectangle(image, (xmin-2,ymin-2), (xmax+2,ymax+2), (0,0, 225), 2)
            retval, jpeg = cv2.imencode('.jpg', image)
            # k = cv2.waitKey(1)
            # if k%256 == 27:  #--------------------> ESC pressed 
            #     self.video.release()
            #     print("~~~~~~~~~~~~  Terminating Program  ~~~~~~~~~~~~")
            # elif k%256 == 32:
            #     cropped = image[ymin2:ymax2, xmin2:xmax2]
            #     cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
            #     retval, buffer = cv2.imencode('.jpg', cropped)
            #     jpg_as_text = base64.b64encode(buffer)
            #     print(jpg_as_text)
            return jpeg.tobytes()
        
        
