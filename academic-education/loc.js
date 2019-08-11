if( navigator.geolocation )
	{
		var optn = {
enableHighAccuracy: true,
			timeout: Infinity,
			maximumAge: 0	
		};
		 var watchID = navigator.geolocation.watchPosition(success, fail, optn);	
	}
 
	else
	 $("p").html("HTML5 Not Supported");
 
$("button").click(function(){
 
	if(watchID)
	 navigator.geolocation.clearWatch(watchID);
 
	watchID = null;
	return false;
});