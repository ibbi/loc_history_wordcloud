# What

Generates a word cloud of the cities or countries you've visited ranked by frequency.

# How

- Download your google location history [here](https://takeout.google.com/). Make sure only Location History is selected, and set to JSON.
- Run the script in the same folder as Location History.json (python locCloud.py)
- Very nice

# Extra (otherwise it'll probably be ugly)

- The script has a few extra (optional) parameters:
  - -h to bring up all these options
  - -s to specify a start date, and ignore older locations
  - -e to specify an end date, and ignore newer locations
  - -b to specify a background color for the image
  - -m to specify a stencil image to shape the cloud (like mask.png)
  - -co to switch to countries instead of cities


     python locCloud.py -s 2018-02-03 -e 2019-01-01 -b yellow -m mask.png -co

will generate a cloud using dates between 02/03/2018 and 01/01/2019, with a yellow background, using mask.png as a stencil and only using countries visited.
