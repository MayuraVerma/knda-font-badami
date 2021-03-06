#!/usr/bin/python3

from nameslist import *
from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)
print(f'Add anchors for {ufo}')

# Modify UFO

# Akhands
akhand1 = ('ka_ssa', 'ka_ssa.base', 'ka_ssa.imathra')
akhand2 = ('ja_nya', 'ja_nya.base', 'ja_nya.imathra')
akhands = akhand1 + akhand2

## Position nukta marks
nuktas = ('nukta', 'nukta.alt')
vedic_dots = ('u1CDE', 'u1CDD')
for nukta, vedic_dot in zip(nuktas, vedic_dots):
    vg = font[vedic_dot]
    (xmin, ymin, xmax, ymax) = vg.bounds
    xcenter = (xmin + xmax) / 2
    ycenter = (ymin + ymax) / 2
    # The nukta glyphs are references
    # so the calculations were done on the source glyphs.
    ng = font[nukta]
    ng.appendAnchor('_N', (xcenter, ycenter))

## Position ematra...

#ematra = font['ematra']
#(xmin, ymin, xmax, ymax) = ematra.bounds
#ematra.appendAnchor('_V', (xmax, ymin))

## Position both
for glyph in font:
    bounds = glyph.bounds
    if bounds is None:
        continue
    (xmin, ymin, xmax, ymax) = bounds
    xcenter = (xmin + xmax) / 2

    # ...on some consonants.
    #if glyph.name in ('jha.base', 'ma.base', 'ya.base'):
    #    glyph.appendAnchor('V', (xcenter, ymax + 50))

    # Position sub sub forms
    if (glyph.name.endswith('.sub') or
        glyph.name in ('ra.below', 'ra.below.large', 'ra.below.ra') + akhands):
        # Add anchors.
        glyph.appendAnchor('S', (xmax + 50, -200))
        if glyph.name.endswith('.sub'):
            glyph.appendAnchor('_S', (xmin, 0))

    # Position nuktas on bases
    if glyph.unicode in Vowels + Consonants or glyph.name in akhands:
        glyph.appendAnchor('N', (xcenter, ymin + ycenter))

# Save UFO
font.changed()
font.save()
font.close()
