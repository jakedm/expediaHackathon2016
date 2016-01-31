import requests
import json
from getAirports import getAirports
from datetime import datetime

def getNumDays(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return int(abs((d2 - d1).days))

"""
DEPRECATED
JASON PUTTING THIS LOGIC IN SEPERATE FILE

def getHotels(dep, all_destinations, daterange):
    '''
    This function will return the cheapest flight for a given location that leaves, returns on
    the given daterange.
    
    '''
    result = Requests.get("http://terminal2.expedia.com:80/x/mflights/search", params=payload)

"""
def getFlights(dep, all_destinations, daterange;):
    '''
    This function will return the cheapest flight for a given location that leaves, returns on
    the given daterange.

    :param dep: String denoting departure airport
    :param all_destinations: List of all possible destinations (Strings)
    :param daterange: List of date range (two strings)

    returns (in some data structure) the name of the flight to the destination, the name of the flight home, and the
      round trip price for the flights selected.
    '''

    


def parseFlights(all_destinations, flight_dict):
    '''
    This function will parse the json response, and get the desired fields from the json text.
    '''
    



def parseHotels(json_response):
    '''
    This function will parse the json response, and get the desired fields from the json text.

    This will return a dictionary of the data for the selected hotel, of form:
      display_info = {
        'name' : hotel_name (string)
        'address' : hotel_address (string)
        'lat' : latitude (string)
        'lng' : longitude (string)
        'cost' : total cost (float)
      }

    '''
    response = json.loads(str(json_response))
    
    
    hotel = response['HotelInfoList'][0]
    name = hotel['Name']
    address = hotel['Location']['StreetAddress'] + ", " hotel['Location']['City'] + ", " + hotel['Location']['Province'] + " " + hotel['Location']['Country']
    lat_lng = [hotel['Location']['GeoLocation']['Latitude'], hotel['Location']['GeoLocation']['Longitude']]
    price_per_night = (double)hotel['Promotion']['Amount']['Value']
    days = (int)hotel['LengthOfStay']
    
    total_cost = price_per_night * days

    display_info = {'name' : name, 'address' : address, 'lat' : lat_lng[0], 'lng' : lat_lng[1], 'cost' : total_cost}

    return display_info

def findVacations(dep, all_destinations, daterange, user_price):
    '''
    Returns all vacations possible (hotel + round trip flight) under a given input price, for a given departure location.
    
    '''
    #Final dictionary(?) of possible vacations; will contain one entry for every given location.
    acceptable_vacations = {}

    #Length of stay variable needs to be set to number of days between the start/end 
    length_of_stay = getNumDays(daterange[1], daterange[0])


#def getFlightOverview(dep, all_destinations, daterange, user_price):
    


def findAllDest(dep, daterange, user_price):
    '''
    This function will get all available destinations from a given departure location.

    OPTION 1: Assume all locations are reachable from all other locations, use the getFlights()
      function (which depends on the Flight Search API) to repeatedly query the website; getFlights() will then make len(locations) - 1
      different queries, and select the cheapest flight from that.

    OPTION 2: Use the Flights Overview API to do 1 query, return all destinations from a given departure location on a given date, possibly
      get return flight information from same query.
        -- FLIGHTS OVERVIEW API IS BROKEN AS OF 10:39 AM

    '''
    locations = getAirports()
    destinations = locations.pop(locations.index(dep))

    if len(destinations) == len(locations):
        print("Error: departure location not in database.")
        exit(-1)
        
    return destinations

#def computeCosts(user_price):


def processInput(daterange, price, dep):
    '''
    This is the function that the first page will send user input to.

    This function will query the websites for data, and will call the helper functions to make the requests.
    
    Once the helper functions are done, then this function will call the function which will compute the average.

    :param daterange: list of form (startdate, enddate); both elements are strings, in some form.
    :param price: String representing max price.
    :param dep: 3 letter airport code, recieved from dropdown list.
    '''
    
    
    # findAllDest() will return all destination options available for the given input date
    possible_dest = findAllDest(dep, daterange, price)

    # findVacations will return a dictionary(?) of structure:
    #   vacations['destination airport'] = {'price of cheapest destination flight' : 'price', 'flight name' : 'name', 'price of cheapest return flight' : 'price', 'flight name' : 'name', 'price of cheapest hotel for entirety of stay' : 'price', 'name of hotel' : 'name']
    #   
    #   In other words, the dictionary will contain:
    #   Price of cheapest flight to destination, name of flight, price of cheapest flight home, name of flight,
    vacations = findVacations()
