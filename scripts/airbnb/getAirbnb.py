import requests
from bs4 import BeautifulSoup
import json
from scraper import IterateMainPage, DetailResults


#link = "https://www.airbnb.com/s/Portland--OR--United-States?checkin=02%2F09%2F2016&checkout=02%2F13%2F2016&zoom=10&search_by_map=true&sw_lat=45.28478648192639&sw_lng=-123.00186467695312&ne_lat=45.78498760084404&ne_lng=-122.30697942304687&ss_id=ooxd6oxn

#alt_link = 'https://www.airbnb.com/s/New-York--NY?checkin=02%2F18%2F2016&checkout=02%2F27%2F2016&guests=&source=bb&ss_id=ss_id%3Dooxd6oxn'
'''
def search(city, state, country, start, end):

    country = country.split()
    
    country_in = ''
    if len(country) > 1:
        country_in = country[0] + '-' + country[1]

    start_list = start.split('-')
    end_list = end.split('-')

    start_in = start_list[1] + "%2F" + start_list[0] + "%2F" + start_list[2]
    end_in = end_list[1] + "%2F" + end_list[0] + "%2F" + end_list[2]

    link = 'https://www.airbnb.com/s/%s--%s--%s?checkin=%s&checkout=%s&zoom=10&search_by_map=false&ss_id=ooxd6oxn' %(city, state, country_in,start_in,end_in)

    r = requests.get(link)
    print(r)
    return r.text

def parseHtml(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    results = soup.find_all('div',class_="listings-container")
    print(results)
    

def getAirbnbEntries(city, state, country, startdate, enddate):
    
    response_text = search(city, state, country, startdate, enddate)
    
    data = parseHtml(response_text)
'''

def getData(state, city):
    
    location_string = 
    results = IterateResults
