import sys
import requests
import json

flightOverViewUrl = 'http://terminal2.expedia.com:80/x/flights/overview/get'
'''
    This function will return the cheapest flight for a given location that leaves, returns on
    the given daterange.

    :param dep: String denoting departure airport
    :param all_destinations: List of all possible destinations (Strings)
    :param maxDays: integer value of desired travel duration 

    returns (in some data structure) the name of the flight to the destination, the name of the flight home, and the
      round trip price for the flights selected.
'''

def hello(v):
    print('hello ' +v)

def getFlights(depCode, all_destinations, maxDays):
    ''' 
    String depCode


    '''
    retDate = 2016-02-22
    origin = 

    queryString = "http://terminal2.expedia.com/x/mflights/search?departureDate=" + depDate + "&returnDate=" + retDate +"&departureAirport="+ origin +"&arrivalAirport="+ retAirport +"&apikey=BQBh6sGziLeQsNQxVjHPlaO08ATfLKn7"
    
def main(args):
    hello(args[1])

if __name__ == '__main__':
    main(sys.argv)
