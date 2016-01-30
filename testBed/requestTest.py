import requests

r = requests.get("http://terminal2.expedia.com/x/mflights/search?departureAirport=LAX&arrivalAirport=ORD&departureDate=2016-02-22&childTravelerAge=2&apikey=BQBh6sGziLeQsNQxVjHPlaO08ATfLKn7")

print(r.url)
print(r.text)
