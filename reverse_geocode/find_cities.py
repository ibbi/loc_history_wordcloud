import reverse_geocode
import json

coordinates = []
multiple = 10**7
with open('../data/clean_history.json') as json_file:  
    data = json.load(json_file)
    for p in data:
        for j in data[p]:
            fixedLat = j['latitudeE7']/(multiple)
            fixedLong = j['longitudeE7']/(multiple)
            coordinate = (fixedLat, fixedLong)
            print(coordinate)

# print(reverse_geocode.search(coordinates))
