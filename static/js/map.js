var map
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 39.50, lng: -98.35},
    zoom: 5,

    mapTypeControl: false
  });
}
window.onload = initMap();
