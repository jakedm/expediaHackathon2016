import requests
from bs4 import BeautifulSoup
import json
#from scraper import IterateMainPage


#link = "https://www.airbnb.com/s/Portland--OR--United-States?checkin=02%2F09%2F2016&checkout=02%2F13%2F2016&zoom=10&search_by_map=true&sw_lat=45.28478648192639&sw_lng=-123.00186467695312&ne_lat=45.78498760084404&ne_lng=-122.30697942304687&ss_id=ooxd6oxn

#alt_link = 'https://www.airbnb.com/s/New-York--NY?checkin=02%2F18%2F2016&checkout=02%2F27%2F2016&guests=&source=bb&ss_id=ss_id%3Dooxd6oxn'

def search(city, state, country, start, end):

    country = country.split()
    
    country_in = ''
    if len(country) > 1:
        country_in = country[0] + '-' + country[1]

    start_list = start.split('-')
    end_list = end.split('-')

    start_in = start_list[1] + "%2F" + start_list[0] + "%2F" + start_list[2]
    end_in = end_list[1] + "%2F" + end_list[0] + "%2F" + end_list[2]

    link = 'https://www.airbnb.com/s/%s--%s--%s?checkin=%s&checkout=%s&zoom=10&search_by_map=false' %(city, state, country_in,start_in,end_in)

    r = requests.get(link)
    print(r)
    return r.text

def parseHtml(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    #results = soup.find_all('div',class_="row")
    results = soup.find_all('div',class_="col-sm-12 row-space-2 col-md-6")
    results_str = str(results)
    results_str.replace("&lt", "")
    results_str.replace("<sup>", "")
    results_str.replace("</sup>", "")
    results_arr = results_str.split(" ")
    
    dirty_prices = [r for r in results_arr if "data-price" in r]
    dirty_urls = [u for u in results_arr if "data-url" in u]
    prices = []
    urls = []
    for i in range(1,len(dirty_prices), 2):
        prices.append(dirty_prices[i])

    for i in range(0, len(dirty_urls), 2):
        urls.append(dirty_urls[i])
    print(prices)
    print(urls)
    print(len(prices))
    print(len(dirty_urls))
    #prices = soup.find_all('div')
    #urls = soup.find_all('div', id='data-url')

    
#getAirbnbEntries("Seattle", "WA", "United States", "2016-02-11", "2016-02-20")
def getAirbnbEntries(city, state, country, startdate, enddate):
    
    response_text = search(city, state, country, startdate, enddate)
    
    data = parseHtml(response_text)

