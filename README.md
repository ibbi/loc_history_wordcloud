# What

Generates a word cloud of the cities or countries you've visited ranked by frequency.

# How

- Download your google location history [here](https://takeout.google.com/). Make sure only Location History is selected, and set to JSON.
- Run the script in the same folder as Location History.json (python locCloud.py)
- Very nice

# Extra (otherwise it'll probably be ugly)

- The script has a few extra (optional) parameters:
  - -h to bring up all these options ```python locCloud.py -h```
  - -s to specify a start date, and ignore older locations ```python locCloud.py -s 2018-02-03```
  - -e to specify an end date, and ignore newer locations ```python locCloud.py -e 2019-01-01```
  - -b to specify a background color for the image ```python locCloud.py -b black```
  - -m to specify a stencil image for cloud palette and shape ```python locCloud.py -m mask.png```
  - -co to switch to countries instead of cities ```python locCloud.py -co```



So, to generate a cloud of countries using locations visited between 02/03/2018 and 01/01/2019, with a yellow background, using mask.png as a stencil/palette.
```
python locCloud.py -s 2018-02-03 -e 2019-01-01 -b yellow -m mask.png -co
```
