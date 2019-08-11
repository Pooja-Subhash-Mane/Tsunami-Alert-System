
var rootref = firebase.database().ref().child("RealTime Node");
rootref.on("child_changed",function(snapshot){


var newPost = snapshot.val();           
var asa = snapshot.child("as");
$("#ak").append("Tsunami Alert at: " + newPost);


var imgRef=firebase.database().ref().child("Images").child(newPost);
imgRef.on('value', function(snapshot) {    
    var data = snapshot.val();
    document.getElementById("imgLoad").src=data;
    console.log(data);
});

$("#imgt").append("So it is:");

// const accountSid = 'AC4106d85131931e833b4ae54621c0375b';
// const authToken = '89ac03a76fe7e425b2444c3c47333e15';
// const client = require('twilio')(accountSid, authToken);

// client.messages
// .create({
// 	body: 'Tsunami Alert!!!!!!!',
// 	from: '+13216168741',
// 	to: '+919637336606'
// }).then(message => console.log(message.sid));


});