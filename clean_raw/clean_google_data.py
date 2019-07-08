import sys
import json
from argparse import ArgumentParser, ArgumentTypeError
from datetime import datetime
import reverse_geocode
import json


def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise ArgumentTypeError(msg)


def dateCheck(timestampms, startdate, enddate):
    dt = datetime.utcfromtimestamp(int(timestampms) / 1000)
    if startdate and startdate > dt:
        return False
    if enddate and enddate < dt:
        return False
    return True


def createCityDict():

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

    with open('freq_dict.json', 'w') as fp:
        json.dump(cityDict, fp)


def cleanRawHistory():
    output = 'clean_history.json'
    try:
        json_data = open('Location History.json').read()
    except:
        print("Error opening input file")
        return

    try:
        data = json.loads(json_data)
    except:
        print("Error decoding json")
        return

    if "locations" in data and len(data["locations"]) > 0:
        try:
            f_out = open(output, "w")
        except:
            print("Error creating output file for writing")
            return

        items = data["locations"]

        if args.startdate or args.enddate:
            items = [item for item in items if dateCheck(
                item["timestampMs"], args.startdate, args.enddate)]

        f_out.write("{\"locations\":[")
        first = True

        for item in items:
            if first:
                first = False
            else:
                f_out.write(",")
            if item["latitudeE7"] > 1800000000:
                item["latitudeE7"] = item["latitudeE7"] - 4294967296
            if item["longitudeE7"] > 1800000000:
                item["longitudeE7"] = item["longitudeE7"] - 4294967296
            f_out.write("{")
            f_out.write("\"latitude\":%s," % (item["latitudeE7"]/e7))
            f_out.write("\"longitude\":%s" % (item["longitudeE7"]/e7))
            f_out.write("}")
        f_out.write("]}")

        f_out.close()

    else:
        print("No data found in json")
        return


cityDict = {}
e7 = 10**7
arg_parser = ArgumentParser()
arg_parser.add_argument(
    '-s', "--startdate", help="The Start Date - format YYYY-MM-DD (0h00)", type=valid_date)
arg_parser.add_argument(
    '-e', "--enddate", help="The End Date - format YYYY-MM-DD (0h00)", type=valid_date)
args = arg_parser.parse_args()


def main():
    cleanRawHistory()
    createCityDict()


if __name__ == "__main__":
    sys.exit(main())
