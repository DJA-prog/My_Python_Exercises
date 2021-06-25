import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('6.jpg', 6)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)
hsl = first_color.hsl # e.g. (230, 255, 203)
proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
print(f"Red: {rgb[0]}")
print(f"Red: {rgb.r}")
print(f"Grn: {rgb.g}")
print(f"Blu: {rgb.b}")
print(f"saturation: {hsl[1]}")
print(f"saturation: {hsl.s}")
