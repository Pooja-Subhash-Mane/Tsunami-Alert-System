
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

if(newPost=='true')
	$("#predictIt").append("Predicted The Tsunami..Voila");
else
document.body.style.backgroundColor="red";


});