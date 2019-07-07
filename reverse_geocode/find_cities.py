import reverse_geocode
import json

multiple = 10**7
cityDict = {}
with open('../data/clean_history.json') as json_file:  
    data = json.load(json_file)
    for p in data:
        for j in data[p]:
            fixedLat = j['latitudeE7']/(multiple)
            fixedLong = j['longitudeE7']/(multiple)
            coordinate = [(fixedLat, fixedLong)]
            reverseInfo = reverse_geocode.search(coordinate)[0]
            reverseCity = reverseInfo['city']
            reverseCountry = reverseInfo['country']
            if reverseCity in cityDict:
                cityDict[reverseCity] += 1
            else: 
                cityDict[reverseCity] = 1
print (cityDict)


# print(reverse_geocode.search(coordinates))
