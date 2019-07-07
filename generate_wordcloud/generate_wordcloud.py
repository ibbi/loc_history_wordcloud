import numpy as np

import os
import re
import json
from PIL import Image
from os import path
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open('../data/freq_dict.json') as json_file:
    freqDict = json.load(json_file)


mask = np.array(Image.open("circle.png"))

wc = WordCloud(background_color="white", max_words=1000,
               mask=mask, contour_width=3, contour_color='steelblue')


wc.generate_from_frequencies(freqDict)
# print(len(freqDict))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
