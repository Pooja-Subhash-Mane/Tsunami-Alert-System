import smtplib
import extcolors as ji
import cv2
import time
from twilio.rest import Client
import extcolors as ji
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
                nvar="1"
                firebase.database().child("RealTime Node").child("Mane").set(nvar)#Updating the Database

                dlink=firebase.database().child("Images").child(nvar).get().val()
                #dlink="https://firebasestorage.googleapis.com/v0/b/test-3f09a.appspot.com/o/1.jpg?alt=media&token=9cf380b8-755a-4723-8d41-4cd98c5e8f58"

                content = 'TSUNAMI ALERT!!!!'+'\nThe Safe zones are as follows: '+dlink;
                mail=smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                recipients = ['siddhantsukhatankar@gmail.com', 'atharvakango1@gmail.com', 'nikitaaware1998@gmail.com', 'poojamane0101@gmail.com']
                mail.login('swatikasar17@gmail.com','sk27$9806')
                mail.sendmail('swatikasar17@gmail.com',recipients,content)
                mail.close()

                
                #sending text messages


                account_sid = 'ACbb713e5387b4d4d93ecd8c7b80cf6cfb'
                auth_token = '72a40562f8b77477f06c52a1f5e19855'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                                     body="Tsunami Alert!!"+'\nFollowing are the safe zones you should head  to :'+dlink,
                                     from_='+19497634689',
                                     to='+919881862818'
                                 )

                print(message.sid)

                # Your Account Sid and Auth Token from twilio.com/console
                account_sid = 'AC42f06897050e484f5624419e1701f0db'
                auth_token = '4e52319b8760b0a2743ecbbfbefccab0'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                                     body="Tsunami Alert!!"+'\nFollowing are the safe zones you should head  to :'+dlink,
                                     from_='+16106869128',
                                     to='+919421986210'
                                 )

                print(message.sid)

                account_sid ='AC0fe52979971e508c946069aaf822499e'
                auth_token = '1a5f643116b1d884ab5e0d8fadd80f9b'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                                     body="Tsunami Alert!!"+'\nFollowing are the safe zones you should head  to :'+dlink,
                                     from_='+19284517433',
                                     to='+918007817047'
                                 )

                print(message.sid)


                account_sid ='AC4106d85131931e833b4ae54621c0375b'
                auth_token = '89ac03a76fe7e425b2444c3c47333e15'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                                     body="Tsunami Alert!!"+'\nFollowing are the safe zones you should head  to :'+dlink,
                                     from_='+13216168741',
                                     to='+919637336606'
                                 )

                print(message.sid)                

                account_sid = 'ACbb713e5387b4d4d93ecd8c7b80cf6cfb'
                auth_token = '72a40562f8b77477f06c52a1f5e19855'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                                     body="Tsunami Alert!!"+'\nFollowing are the safe zones you should head  to :'+dlink,
                                     from_='+19497634689',
                                     to='+919881862818'
                                 )

                print(message.sid)

                # Your Account Sid and Auth Token from twilio.com/console
                account_sid = 'AC42f06897050e484f5624419e1701f0db'
                auth_token = '4e52319b8760b0a2743ecbbfbefccab0'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                                     body="Tsunami Alert!!"+'\nFollowing are the safe zones you should head  to :'+dlink,
                                     from_='+16106869128',
                                     to='+919421986210'
                                 )

                print(message.sid)

                account_sid ='AC0fe52979971e508c946069aaf822499e'
                auth_token = '1a5f643116b1d884ab5e0d8fadd80f9b'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                                     body="Tsunami Alert!!"+'\nFollowing are the safe zones you should head  to :'+dlink,
                                     from_='+19284517433',
                                     to='+918007817047'
                                 )

                print(message.sid)


                account_sid ='AC537a49d120b9fa65e37ccc04b9b37b10'
                auth_token = '1706d481924a04924a35eb0b76afb3f8'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                                     body="Tsunami Alert!!"+'\nFollowing are the safe zones you should head  to :'+dlink,
                                     from_='+12015281649',
                                     to='+919518371149'
                                 )

                print(message.sid)




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
