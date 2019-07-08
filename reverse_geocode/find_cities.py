import reverse_geocode
import json

cityDict = {}
with open('clean_history.json') as json_file:
    data = json.load(json_file)
    for p in data:
        for j in data[p]:
            coordinate = [(j['latitude'], j['longitude'])]
            reverseInfo = reverse_geocode.search(coordinate)[0]
            reverseCity = reverseInfo['city']
            # reverseCountry = reverseInfo['country']
            # Adjust to change weight range
            if reverseCity in cityDict:
                cityDict[reverseCity] += 100/(cityDict[reverseCity]**2)
            else:
                cityDict[reverseCity] = 10

with open('../data/freq_dict.json', 'w') as fp:
    json.dump(cityDict, fp)
