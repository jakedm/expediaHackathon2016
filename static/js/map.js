var map
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    // center: {lat: 39.50, lng: -98.35},
    center: {lat:47.45, lng: -122.29},
    zoom: 10,

  });
}
window.onload = initMap();