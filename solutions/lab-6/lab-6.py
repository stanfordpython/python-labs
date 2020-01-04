
##################################
# CONVERTING IMAGES TO ASCII ART
##################################

import pandas as pd
import numpy as np
from PIL import Image
import requests

# Load the CSV into a pandas DataFrame
# either download 'secret.csv' and run:
d = pd.read_csv('secret.csv')
# or:
d = pd.read_csv(BytesIO(requests.get('https://raw.githubusercontent.com/stanfordpython/python-labs/master/notebooks/lab-6/secret.csv').content))

# Convert the DataFrame into a numpy array
a = d.values.astype(np.uint8)

# Convert the numpy array into a Pillow image
im = Image.fromarray(a)

#im.show() # to show the image

import bisect
characters = '▓▒░ '
breakpoints = [64, 128, 192]

# Convert each pixel (each entry in a) to a character based on where it falls, relative to the breakpoints:
im_ascii = '\n'.join(
    ''.join(
        map(lambda pt: characters[bisect.bisect(breakpoints, pt)], row)
    ) for row in a
)

print(im_ascii)

# Optionally, to scale the image first:
im = im.resize((int(im.size[0]*1.5), im.size[1])) # scale width by 1.5
stretched_arr = np.asarray(im)
im_ascii = '\n'.join(
    ''.join(
        map(lambda pt: characters[bisect.bisect(breakpoints, pt)], row)
    ) for row in stretched_arr
)
