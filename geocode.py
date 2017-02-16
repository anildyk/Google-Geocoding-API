import urllib, json
#Google Geocoding API url.
api_url = "https://maps.googleapis.com/maps/api/geocode/json?"
while True:
	address = raw_input('Enter Location: ')
	if len(address) < 1: break
	url = api_url + urllib.urlencode({'address':address, 'key': 'YOUR_API_KEY'}) #URL of JSON file 
  
	data = urllib.urlopen(url).read()

	try: js = json.loads(data)  #js is JSON object that is like a dictionary of lists and dictionaries. 
	except: js = None

	if 'status' not in js or js['status'] != 'OK':
		print 'Failed. Can\'t locate this location'
		print data
		continue

	lat = js["results"][0]["geometry"]["location"]["lat"] #Get Latitude from JSON Object.
	lng = js["results"][0]["geometry"]["location"]["lng"] #Get Longitude fron JSON Object.
	print "Latitude:",lat
	print "Longitude:",lng
	location = js["results"][0]["formatted_address"] #Get formatted location or location according to Google Map
	print "Formatted Address:",location
