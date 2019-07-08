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

wc = WordCloud(height=5000, width=10000, background_color="white", max_words=1000,
               mask=mask)


wc.generate_from_frequencies(freqDict)
plt.figure(figsize=(200, 100))

# print(len(freqDict))
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")

wc.to_file('thing.png')


plt.axis("off")
plt.figure()
