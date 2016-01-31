import json
import requests

depCode = "SEA"
maxDays = 10
all_destinations = ["SFO", "LAX", "JFK"]


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
"dayCount": str(maxDays)
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
indexOfMin = allFlights.index(price)

flightsInfo = {}
flightsInfo["depDate"] = allFlightsDepDates[index]
flightsInfo["retDate"] = allFlightsRetDates[index]
flightsInfo["price"] = allFlights[index]

flightsDict = {}
for des in all_destinations:
    flightsDict[des] = flightsQuery(depCode, des, maxDays)

