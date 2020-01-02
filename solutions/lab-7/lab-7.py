
##################################
# CONVERTING IMAGES TO ASCII ART
##################################

import pandas as pd
import numpy as np
from PIL import Image

# Load the CSV into a pandas DataFrame
d = pd.load_csv('~/Desktop/secret.csv')

# Convert the DataFrame into a numpy array
a = np.asarray(d).astype(np.uint8)

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