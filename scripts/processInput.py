import requests
import json
from getAirports import getAirports
from flightsQuery import getFlights
from datetime import datetime


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
    if (max_days > 2):
        day_list.append(num_days - 1)
        day_list.append(num_days - 2)
    elif (max_days == 2):
        day_list.append(num_days - 1)

    start_date = year + '-' + month + '-' + start_day

    hotels_list = []
    flights_list = []
    
    #This is the area where I call Jason's code. Method name will change, most likely
    for i in range(0, len(day_list)):
        flights_list[i], hotels_list[i] = getFlights(dep,all_destinations,(int)day_list[i],start_date,(int)user_price)
        
    
    master_list = {}
    for dest in all_destinations:
        done = False
        days_index = 0
        while not done:
            hotel = hotels_list[days_index][dest]
            current_price = (int)flights_list[days_index]['price'] + (int)hotel['price']
            if current_price <= (int)user_price:
                done = True                

                lat = hotel['lat']
                lng = hotel['lng']
                address = hotel['address']
                picture_url = hotel['url']
                state = hotel['state']
                city = hotel['city']
                country = "United States"
                start = flights_list[days_index]['depDate']
                end = flights_list[days_index]['retDate']
                airbnb_data = getAirbnbEntries(city, state, country, start, end)
                airbnb_cost = airbnb_data['airbnb_cost']
                airbnb_url = airbnb_data['url']
                master_list[dest] = {
                    'departure' : dep, 
                    'destination' : dest, 
                    'cost' = current_price, 
                    'lat' : lat,
                    'lng' : lng,
                    'picture' : url,
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
    destinations = locations.pop(locations.index(dep))

    if len(destinations) == len(locations):
        print("Error: departure location not in database.")
        exit(-1)
        
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
