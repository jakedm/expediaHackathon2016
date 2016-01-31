import json
import requests

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
"AirportCode" : [ "SEA" ]
},
"DestinationAirportCodeList" : {
"AirportCode" : [ "SFO" ]
},
"FlightListings" : {
"MaxCount" : 20
},
"FareCalendar": {
"StartDate": "2016-02-05T19:33:39.363-08:00",
"dayCount": "10"
}
}

data_json = json.dumps(data)
headers = {'accept': 'application/json', 'Authorization': 'expedia-apikey key=BQBh6sGziLeQsNQxVjHPlaO08ATfLKn7'}
response = requests.post(url, data=data_json, headers=headers)

with open('results.txt','w',) as outfile:
    json.dump(response.json(),outfile)
