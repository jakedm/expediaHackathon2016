from getAirports import getAirports
import json
import requests

URL = "http://terminal2.expedia.com/x/hotels"


def getLatLng():
    airports = getAirports()
    d = []
    loc = {}
    with open('airportTolatlng.json') as f:    
        file = json.load(f)
        d = file["data"]
        
    
    
    for l in d:
        if str(l[8]) in airports:
            index = airports.index(str(l[8]))
            lat = str(l[9])
            lng = str(l[10])
            loc[airports[index]] = (lat, lng)
        

    return loc


def hotelsQuery(dest, start, end, num_days, dest_loc):

    search = URL + "?" + "maxhotels=1&location=" + dest_loc[0] + "%2C" + dest_loc[1] + "&radius=10km&sort=price&order=desc"
    
    r = requests.get(search)
    hotel = json.loads(str(r.text))
    hotel = response['HotelInfoList'][0]
    name = str(hotel['Name'])
    address = str(hotel['Location']['StreetAddress']) + ", " + str(hotel['Location']['City']) + ", " + str(hotel['Location']['Province']) + " " + str(hotel['Location']['Country'])
    city = str(hotel['Location']['City'])
    state = str(hotel['Location']['Province'])
    lat_lng = [str(hotel['Location']['GeoLocation']['Latitude']), str(hotel['Location']['GeoLocation']['Longitude'])]
    price_per_night = float(hotel['Promotion']['Amount']['Value'])
    days = int(hotel['LengthOfStay'])
    pic = str(hotel['detailsUrl'])

    display_info = {'name' : name, 'address' : address, 'lat' : lat_lng[0], 'lng' : lat_lng[1], 'cost' : total_cost, 'picture_url' : pic, 'city' : city, 'state' : state}

    

    return display_info

def getHotels(flight_dict, num_days):
    
    lat_long = getLatLng()
    hotels_list = {}

    for dest in flight_dict.keys():
        start = flight_dict[dest]['depDate']
        end = flight_dict[dest]['retDate']
        hotel_data = hotelsQuery(dest, start, end, num_days, lat_lng[dest])
        hotels_list[dest] = hotel_data
        
    print(hotels_list['SEA'].values())

    return hotels_list
