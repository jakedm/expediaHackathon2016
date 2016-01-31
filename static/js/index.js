// SLIDE BAR
function showValue(val){
  document.getElementById("range").innerHTML=val;
}

$(document).ready(function(){
  // AIRPORT LIST
  var dropdown = "<select name='airports'><br>";
  for(airport in airports){
    dropdown += "<option value="+airports[airport].code+">"+airport+"</option><br>";
  }
  dropdown += "</select>";
  $('#dropdown').html(dropdown);
  
  $('#search').click(function(){
    console.log('hi');
    // GET request to API
    $.get('/search', function(res) {
      console.log(res);

      // MAP Specs
      var mapProp = {
        center:new google.maps.LatLng(47.609786,-122.1966154),
        zoom:8,
        mapTypeId:google.maps.MapTypeId.ROADMAP
      };

      // Instance of infowindow
      var infowindow = new google.maps.InfoWindow();
      var infowindow1 = new google.maps.InfoWindow();
      var marker, j;

      // Traversing through all locations that meet specifications by user (All Airports)
      for (var j =0; j < res.CarInfoList.CarInfo.length; j++) {
        console.log(res)

        // Creating Markers for each location (Airports)
        marker = new google.maps.Marker({
          position: new google.maps.LatLng(res.CarInfoList.CarInfo[j].DropOffInfo.Location.GeoLocation.Latitude, res.CarInfoList.CarInfo[j].DropOffInfo.Location.GeoLocation.Longitude),
          map: map
        });

        // Adding content to infowindows (Hotel+Airfare total)
        google.maps.event.addListener(marker, 'click', (function(marker, j) {
          return function() {
            infowindow.setContent("<i class='material-icons'>flight</i><p>$"+res.CarInfoList.CarInfo[j].Price.BaseRate.Value+"</p>");
            infowindow.open(map, marker);
          }
        })(marker, j));
        infowindow1.setContent("<p>$"+res.CarInfoList.CarInfo[j].Price.BaseRate.Value+"</p>");
        infowindow1.open(map, marker);
      }
    })
  })
})
