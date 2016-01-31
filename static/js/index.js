// SLIDE BAR
function showValue(val){
  document.getElementById("range").innerHTML=val;
}

$(document).ready(function(){


// window.onload = initMap();
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
      // var mapProp = {
      //   center:new google.maps.LatLng(47.609786,-122.1966154),
      //   zoom:8,
      //   mapTypeId:google.maps.MapTypeId.ROADMAP
      // };

      // Instance of infowindow
      var infowindow = new google.maps.InfoWindow();

      var marker, j;

      var count = 0;
           for (airport in airports){
             if(count < 25){
               var marker = new google.maps.Marker({
                 position: new google.maps.LatLng(airports[airport].lat, airports[airport].lon),
                 map: map
               })
               var infowindow = new google.maps.InfoWindow();
               infowindow.setContent("$200");
               infowindow.open(map, marker);
             }
             else{
               break;
             }
             count++
           }

      // Traversing through all locations that meet specifications by user (All Airports)
      for (var j =0; j < 1; j++) {
        console.log(res.CarInfoList.CarInfo[j].DropOffInfo.Location.GeoLocation.Latitude, res.CarInfoList.CarInfo[j].DropOffInfo.Location.GeoLocation.Longitude)

        // Creating Markers for each location (Airports)
        marker = new google.maps.Marker({
          // position: new google.maps.LatLng(res.CarInfoList.CarInfo[j].DropOffInfo.Location.GeoLocation.Latitude, res.CarInfoList.CarInfo[j].DropOffInfo.Location.GeoLocation.Longitude),
          position: new google.maps.LatLng(38.50, -102.35),
          map: map
        });

        // Adding content to infowindows (Hotel+Airfare total)
        google.maps.event.addListener(marker, 'click', (function(marker, j) {
          return function() {
            // infowindow.setContent("<i class='material-icons'>flight</i><span>SEA --> SLC $300</span><hr><img src="+res.CarInfoList.CarInfo[j].ThumbnailUrl+" alt='hotel' height='100' width='100'><hr><i class='material-icons'>home</i><span> 3 days x $66 -> $198</span><br><span>Total = $498</span><br><button>Book</button><p>$"+res.CarInfoList.CarInfo[j].Price.BaseRate.Value+"</p>");
            infowindow.setContent('<div class="panel panel-warning detail-box" style="position: relative; z-index: 400;"><div class="panel-heading"><h3 class="panel-title"><span><i class="fa fa-map-marker"></i></span> <span id="city">Salt Lake City, Utah</span></h3></div><div class="panel-body"><img src="../static/images/hotel.jpg" class="img-responsive" alt="Hotel Image"><div class="panel-heading"><h3 class="panel-title"><span><i class="fa fa-plane"></i></span><span id="origin">SEA</span><span><i class="fa fa-long-arrow-right"></i></span><span id="destination">SLC</span><span class="pull-right"><span><i class="fa fa-usd"></i> </span><span id="fare">327</span></span></h3></div><hr style="margin-top: 2px; margin-bottom: 2px;"><div class="panel-heading"><h3 class="panel-title"><span><i class="fa fa-bed"></i></span><span><i class="fa fa-times"></i></span><span id="duration">3</span><span class="pull-right"><span><i class="fa fa-usd"></i> </span><span id="rent">198</span></span></h3></div><a id="purchase" href="https://www.airbnb.com/" target="_blank" type="button" class="btn btn-warning btn-block">Purchase &raquo;</a></div></div>');
            infowindow.open(map, marker);
          }
        })(marker, j));
        var infowindow1 = new google.maps.InfoWindow();
        infowindow1.setContent("<p>$ " + 525 + "</p>");
        // infowindow1.setContent("<p>$"+res.CarInfoList.CarInfo[j].Price.BaseRate.Value+"</p>");
        infowindow1.open(map, marker);
      }
    })
  })
})
