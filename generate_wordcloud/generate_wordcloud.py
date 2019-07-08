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


mask = np.array(Image.open("circle.png"))
image_colors = ImageColorGenerator(mask)

wc = WordCloud(background_color="white", max_words=1000,
               mask=mask)


wc.generate_from_frequencies(freqDict)
# print(len(freqDict))
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()


image_colors = ImageColorGenerator(mask)
# plt.figure(figsize=[7, 7])
