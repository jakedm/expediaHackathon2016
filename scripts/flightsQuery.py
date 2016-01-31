import sys
import requests
import json
import hotels

'''
    This function will return the cheapest flight for a given location that leaves, returns on
    the given daterange.

    :param dep: String denoting departure airport
    :param all_destinations: List of all possible destinations (Strings)
    :param maxDays: integer value of desired travel duration 

    returns (in some data structure) the name of the flight to the destination, the name of the flight home, and the
      round trip price for the flights selected.
'''

flightOverViewUrl = 'http://terminal2.expedia.com:80/x/flights/overview/get'
def getFlights(depCode, all_destinations, maxDays):
    flightsDict = {}
    for des in all_destinations:
        flightsDict[des] = flightsQuery(depCode, des, maxDays)

    hotels_list = getHotels(allFlights, maxDays)

    return (allFlights,hotels_list)

def flightsQuery(depCode, des, maxDays):

    url = 'http://terminal2.expedia.com:80/x/flights/overview/get'
    data = {
    "MessageHeader" : {
    "ClientInfo" : {
    "DirectClientIP" : "1.0.0.0",
    "DirectClientHostname" : "TestDirectClientHostname",
    "DirectClientName" : "TestDirectClientName",
    "OriginalClientIP" : "10.0.0.5",
    "OriginalClientHostname" : "TestOriginalClientHostname",
    "OriginalClientName" : "TestOriginalClientName"
    },
    "MessageVersion" : "V1.1",
    "CreateDateTime" : 1439251723896,
    "MessageGUID" : "1234a34a-3567-89c4-19cd-12345678abcd",
    "TransactionGUID" : "airoverviewhappypath"
    },
    "tpid" : 1,
    "eapid" : 0,
    "PointOfSaleKey" : {
    "JurisdictionCountryCode" : "USA",
    "CompanyCode" : "10111",
    "ManagementUnitCode" : "1010"
    },
    "OriginAirportCodeList" : {
    "AirportCode" : [ depCode ]
    },
    "DestinationAirportCodeList" : {
    "AirportCode" : [ des ]
    },
    "FlightListings" : {
    "MaxCount" : 20
    },
    "FareCalendar": {
    "StartDate": "2016-02-05T19:33:39.363-08:00",
    "DayCount": str(maxDays)
    }
    }

    data_json = json.dumps(data)
    headers = {'accept': 'application/json', 'Authorization': 'expedia-apikey key=BQBh6sGziLeQsNQxVjHPlaO08ATfLKn7'}
    response = requests.post(url, data=data_json, headers=headers)

    jsonReturn = response.json()
    totalItems = len(jsonReturn["FareCalendar"]["AirOfferSummary"])
    allFlights = []
    allFlightsDepDates = []
    allFlightsRetDates = []
    for i in range(0,totalItems):
        allFlights.append(jsonReturn["FareCalendar"]["AirOfferSummary"][i]["FlightPriceSummary"]["TotalPrice"])
        allFlightsDepDates.append(jsonReturn["FareCalendar"]["AirOfferSummary"][i]["FlightItinerarySummary"]["OutboundDepartureTime"])
        allFlightsRetDates.append(jsonReturn["FareCalendar"]["AirOfferSummary"][i]["FlightItinerarySummary"]["InboundDepartureTime"])

    resultMin = min(allFlights)
    indexOfMin = allFlights.index(resultMin)

    flightsInfo = {}
    flightsInfo["depDate"] = allFlightsDepDates[indexOfMin]
    flightsInfo["retDate"] = allFlightsRetDates[indexOfMin]
    flightsInfo["price"] = allFlights[indexOfMin]

    return flightsInfo 
