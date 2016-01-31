import requests
import json
from getAirports import getAirports
from flightsQuery import getFlights
from datetime import datetime
import random
#from getAirbnb import *

# Day to begin searching at
start_day = '15'
year = datetime.now().year

def startQuery(dep, all_destinations, num_days, month, user_price):
    '''
    This function gets all required arguments and sends the necessary data to the query scripts.
    
    ASSUMPTION 1: Month is already a numeric type.
    '''

    max_days = num_days
    day_list = []
    day_list.append(max_days)
    """
    if (max_days > 2):
        day_list.append(int(num_days) - 1)
        day_list.append(int(num_days) - 2)
    elif (max_days == 2):
        day_list.append(int(num_days) - 1)
    """
    start_date = str(year) + '-' + str(month) + '-' + str(start_day)

    hotels_list = []
    flights_list = []
    
    #This is the area where I call Jason's code. Method name will change, most likely
    for i in range(0, len(day_list)):
        temp1, temp2 = getFlights(dep, all_destinations, int(day_list[i]))
        flights_list.append(temp1)
        hotels_list.append(temp2)
        #flights_list[i], hotels_list[i] = getFlights(dep, all_destinations, int(day_list[i]))

    #flights_list[0], hotels_list[0] = 

    master_list = {}
    for dest in all_destinations:
        done = False
        days_index = 0
        while not done:
            #hotel = hotels_list[days_index][dest]
            #current_price = int(flights_list[days_index]['price']) + int(hotel['price'])
            current_price = random.randrange(150, 300)
            if current_price <= int(user_price):
                done = True                

                #lat = str(hotel['lat'])
                #lng = str(hotel['lng'])
                #address = str(hotel['address'])
                #picture_url = str(hotel['url'])
                #state = str(hotel['state'])
                #city = str(hotel['city'])
                lat = hotels_list[0]["lat"]
                lng = hotels_list[0]["lng"]
                address = hotels_list[0]["address"]
                picture_url= hotels_list[0]["url"]
                state= hotels_list[0]["state"]
                city = hotels_list[0]["city"]
                country = "United States"
                start = str(flights_list[days_index][dest]['depDate'])
                end = str(flights_list[days_index][dest]['retDate'])
                #airbnb_data = getAirbnbEntries(city, state, country, start, end)
                #airbnb_cost = str(airbnb_data['airbnb_cost'])
                airbnb_cost = random.randrange(50, 200)
                airbnb_url = "www.airbnb.com"
                #airbnb_url = str(airbnb_data['url'])
                master_list[dest] = {
                    'departure' : dep, 
                    'destination' : dest, 
                    'cost' : current_price, 
                    'lat' : lat,
                    'lng' : lng,
                    'picture' : picture_url,
                    'startDate' : start,
                    'endDate' : end,
                    'airbnb_cost' : airbnb_cost,
                    'airbnb_url' : airbnb_url}
            else:
                days_index += 1
            
    return master_list

def findAllDest(dep):
    '''
    This function will get all available destinations from a given departure location.

    '''
    locations = getAirports()
    orig = len(locations)
    print (len(locations))
    temp = locations.index(dep)
    del(locations[temp])
    #temp = locations.pop(locations.index(dep))
    #destinations = locations.pop(locations.index(dep))
    destinations = locations

    if len(destinations) == orig:
        print("Error: departure location not in database.")
        exit(-1)
        
    print(len(destinations))
        
    return destinations


def processInput(month, num_days, price, dep):
    '''
    This is the function that the first page will send user input to.

    This function will query the websites for data, and will call the helper functions to make the requests.
    
    Once the helper functions are done, then this function will call the function which will compute the average.

    :param num_days: Number of days to plan vacation for
    :param price: String representing max price.
    :param dep: 3 letter airport code, recieved from dropdown list.
    '''
    
    
    # findAllDest() will return all destination options available for the given input 
    destinations= findAllDest(dep)

    data = startQuery(dep, destinations, num_days, month, price)

    #processInput("02", "10", "800", "SEA")

    return data
