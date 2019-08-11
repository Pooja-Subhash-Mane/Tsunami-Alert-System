import smtplib
import extcolors as ji
import cv2
import time
import extcolors as ji
from twilio.rest import Client
import numpy as np
import pyrebase
from PIL import Image


config = {
'apiKey' : "AIzaSyAi3gP2MNwvzdlcvcaMuewc8zoQMDQltow",
'authDomain': "test-3f09a.firebaseapp.com",
'databaseURL': "https://test-3f09a.firebaseio.com",
'projectId': "test-3f09a",
'storageBucket': "test-3f09a.appspot.com",
'messagingSenderId': "928354029774"
}
firebase = pyrebase.initialize_app(config)

def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
   # cropped_image.show()

# Function to extract frames

def FrameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    time.sleep(5)
    count = 0

    # checks whether frames were extracted
    success = 1
    flg = 0
    while success:
        # vidObj object calls read
        # function extract frames
        image: object
        success, image = vidObj.read()

        # Saves the frames with frame-count
        frameoriginal="originalframe%d.jpg" % count
        cv2.imwrite(frameoriginal, image)


       # im_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_LINEAR)
        #cv2.imshow('dst_rt', image)
        #image = Image.open("frame%d.jpg" % count, image)
        #image.show()

        #img = np.zeros((46341, 46341))
        #image = cv2.resize(image, (0, 0), fx=1, fy=61, interpolation=cv2.INTER_CUBIC)

        """image_obj = Image.open("image")
        cropped_image = image_obj.crop(coords)
        cv2.imwrite("frame%d.jpg" % count, image)"""
        crop(frameoriginal, (206, 4, 890, 1079), "frameASHWAMEDHA%d.jpg" % count)
       # cropped_image.save(saved_location)
        #cropped_image.show()

        """colors, pixel_count = ji.extract("frameASHWAMEDHA%d.jpg" % count)
        print(colors)"""
        frameoriginalextract = "frameASHWAMEDHA%d.jpg" % count
        colors, pixel_count = ji.extract(frameoriginalextract)
       # print(colors)
        for x in colors:
            """print(x[0][0])
            print(x[0][1])
            print(x[0][2])"""
            if ((x[0][0] == 246 and x[0][1] == 157 and x[0][2] == 73) or (
                    x[0][0] == 213 and x[0][1] == 254 and x[0][2] == 160) or (
                    x[0][0] == 249 and x[0][1] == 219 and x[0][2] == 105) or (
                    x[0][0] == 247 and x[0][1] == 220 and x[0][2] == 105)):
                print('alert there')
                #sending Email alerts to everyone

                content = 'TSUNAMI ALERT!!!!'
                mail=smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                recipients = ['siddhantsukhatankar@gmail.com', 'atharvakango1@gmail.com', 'nikitaaware1998@gmail.com', 'poojamane0101@gmail.com']
                mail.login('swatikasar17@gmail.com','sk27$9806')
                mail.sendmail('swatikasar17@gmail.com',recipients,content)
                mail.close()

                firebase.database().child("RealTime Node").child("Mane").set("5");#Updating the Database
                #sending text messages

                frameoriginalextract.show()
                flg=1
                break
        count += 1
        if flg==1:
            break



# Driver Code
if __name__ == '__main__':
    # Calling the function
    FrameCapture("tsunamiwave.mp4")
