from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import sys
import json
import numpy as np
from argparse import ArgumentParser, ArgumentTypeError
from datetime import datetime
import reverse_geocode


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


def createfreqDict():

    with open('clean_history.json') as json_file:
        data = json.load(json_file)
        for p in data:
            for j in data[p]:
                coordinate = [(j['latitude'], j['longitude'])]
                reverseInfo = reverse_geocode.search(coordinate)[0]
                if args.countries:
                    reverseItem = reverseInfo['country']
                else:
                    reverseItem = reverseInfo['city']
                # Adjust to change weight range
                if reverseItem in freqDict:
                    freqDict[reverseItem] += 100/(freqDict[reverseItem]**2)
                else:
                    freqDict[reverseItem] = 10

    with open('freq_dict.json', 'w') as fp:
        json.dump(freqDict, fp)


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


def generateWordcloud():
    with open('freq_dict.json') as json_file:
        freqDict = json.load(json_file)
    if args.mask:
        try:
            mask = np.array(Image.open(args.mask))
            image_colors = ImageColorGenerator(mask)
            wc = WordCloud(background_color=args.bgcolor, max_words=1000,
                           mask=mask)
            isMask = True
        except:
            print('invalid image, using default')
            wc = WordCloud(background_color=args.bgcolor,
                           max_words=1000, height=2000, width=4000)
            isMask = False

    else:
        print('no stencil provided, using default')
        wc = WordCloud(background_color=args.bgcolor,
                       max_words=1000, height=2000, width=4000)
        isMask = False
    wc.generate_from_frequencies(freqDict)

    if isMask:
        wc.recolor(color_func=image_colors)

    wc.to_file('wor(l)d map.png')


freqDict = {}
e7 = 10**7
arg_parser = ArgumentParser()
arg_parser.add_argument(
    '-s', "--startdate", help="The Start Date - format YYYY-MM-DD (0h00)", type=valid_date)
arg_parser.add_argument(
    '-e', "--enddate", help="The End Date - format YYYY-MM-DD (0h00)", type=valid_date)
arg_parser.add_argument(
    '-co', "--countries", help="Use countries instead of cities", action='store_true')
arg_parser.add_argument(
    '-m', "--mask", help="Image file to use as stencil for wordcloud")
arg_parser.add_argument(
    '-b', "--bgcolor", help="Wordcloud background color, defaults to white")
args = arg_parser.parse_args()

if not args.bgcolor:
    args.bgcolor = 'white'


def main():
    print('cleaning raw location file...')
    cleanRawHistory()
    print('converting to city or country names...')
    createfreqDict()
    print('generating image...')
    generateWordcloud()
    print('done :-)')


if __name__ == "__main__":
    sys.exit(main())
