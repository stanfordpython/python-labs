"""
Miscellaneous utilities for wallscraper
"""
from fractions import Fraction
import sys
import pathlib

WALLPAPER_FOLDER = pathlib.Path(__file__).parent / 'wallpapers'

def get_aspect_ratio(width, height):
    # Credit to https://en.wikipedia.org/wiki/Aspect_ratio_(image)
    common = [
        (4, 3),    # (COMMON) present-day TV standard
        (16, 10),  # (COMMON) Standard widescreen computer monitor
        (5, 3),    # (COMMON) photography standard
        (16, 9),   # (COMMON) video widescreen standard
    ]

    uncommon = [
        (1, 1),    # Square
        (19, 16),  # Movietone Ratio
        (5, 4),    # Early TV format
        (11, 8),   # Academy-preferred standard
        (3, 2),    # 8-perf 35mm film
        (14, 9),   # Compromise widescreen on some commercials
        (15, 9),   # Nintendo 3DS / 35 mm
        (17, 10),  # Some android tablets
        (7, 4),    # Early 35mm
        (37, 20),  # 35mm US/UK widescreen standard
        (2, 1),    # SuperScope
        (22, 10),  # 70mm standard
        (21, 9),   # Temporary cinema displays
        (3, 1),    # photography standard
    ]

    f = Fraction(width, height)
    for ratio in common:
        for monitor in range(1, 5):
            if f == Fraction(*ratio) * monitor:
                return ratio[0] * monitor, ratio[1]

    for ratio in uncommon:
        if f == Fraction(*ratio):
            return ratio

    # Screens for vertical mobile images
    for ratio in common + uncommon:
        if f == Fraction(ratio[1], ratio[0]):
            return ratio[1], ratio[0]

    sys.stderr.write("Unrecognized dimensions {}x{}: Using {}x{}\n".format(width, height, f.numerator, f.denominator))
    return f.numerator, f.denominator
