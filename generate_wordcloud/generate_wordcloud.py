import numpy as np

import os
import re
import json
from PIL import Image
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open('../data/freq_dict.json') as json_file:
    freqDict = json.load(json_file)

world_mask = np.array(Image.open("mask.png"))
wc = WordCloud(background_color="white", max_words=1000, mask=world_mask)


wc.generate_from_frequencies(freqDict)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
