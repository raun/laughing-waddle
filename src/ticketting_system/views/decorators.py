
import requests
from random import randint
import random
import string

useragents = [ "IE8.0", "Safari", "Chrome", "NULL"]
ips = ["192.1.164.1", "192.1.164.2", "192.1.164.3", "192.1.164.4", "192.1.164.5", "192.1.162.5", "192.1.162.100", "192.1.162.205"]
sessionIds = ["ACQPH776666", "ACQPH775555", "ACQPH774444", "ACQPH773333", "681967"]
browserIds = ["1234", "5678", "9012", "3456", "7826", "52637", "231876", "6218"]
site_urls = ["http://furlenco.com/categories", "http://furlenco.com/products","http://furlenco.com/packages", "http://furlenco.com/build"]
locations = ["{\"coordinates\":{\"lat\":36.518375,\"lon\":-86.05828083}}", "{\"coordinates\":{\"lat\":12.9833,\"lon\":77.5833}}", "{\"coordinates\":{\"lat\":28.6139,\"lon\":77.2090}}", "{\"coordinates\":{\"lat\":51.5072,\"lon\":-0.1275}}", "{\"coordinates\":{\"lat\":-33.8650,\"lon\":151.2094}}", "{\"coordinates\":{\"lat\":35.6833,\"lon\":139.6833}}"]

def getRandom(lst):
	return useragents[randint(0, len(lst)-1)]

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def write_to_elastic_search():
	base_url = "http://127.0.0.1:9200/furlenco_v5/"
	useragent = "Mozilla/5.0 (X11; Linux x86_64; rv:6.0a1) Gecko/20110421 Firefox/6.0a1"
	ip = "192.1.164.2"
	sessionId = "ACQPH776666"
	site_url = getRandom(site_urls)
	browserId = "231876"
	location = "{\"coordinates\":{\"lat\":36.518375,\"lon\":-86.05828083}}"
	payload = "{\"useragent\":\"" + useragent + "\",\"IP\":\""+ ip +"\",\"sessionId\":\"" + sessionId +"\",\"URL\":\"" + site_url + "\",\"browserId\":\""+ browserId +"\",\"geo\":"+ location +"}"
	headers = {
	    'content-type': "application/json",
	    'cache-control': "no-cache",
	    'postman-token': "ad403018-69fa-f2a7-0ae9-a8e0d34073f5"
	    }
	url = base_url + id_generator()
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)	

def pushlish_to_clickstream(func):
	def func_wrapper(*args, **kwargs):
		write_to_elastic_search()
		return func(*args, **kwargs)
	return func_wrapper


