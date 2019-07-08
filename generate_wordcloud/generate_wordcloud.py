import numpy as np

import os
import re
import json
from PIL import Image
from os import path
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

with open('../data/freq_dict.json') as json_file:
    freqDict = json.load(json_file)


mask = np.array(Image.open("mask.png"))
image_colors = ImageColorGenerator(mask)

wc = WordCloud(background_color="white", max_words=1000,
               mask=mask)

wc.generate_from_frequencies(freqDict)
wc.recolor(color_func=image_colors)
wc.to_file('thing.png')
