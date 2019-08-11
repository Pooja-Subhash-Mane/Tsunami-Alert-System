import pyrebase

config = {
'apiKey' : "AIzaSyAi3gP2MNwvzdlcvcaMuewc8zoQMDQltow",
'authDomain': "test-3f09a.firebaseapp.com",
'databaseURL': "https://test-3f09a.firebaseio.com",
'projectId': "test-3f09a",
'storageBucket': "test-3f09a.appspot.com",
'messagingSenderId': "928354029774"
}

firebase = pyrebase.initialize_app(config)
firebase.database().child("RealTime Node").child("Mane").set("1");


