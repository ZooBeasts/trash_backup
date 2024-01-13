# import numpy as np
# from PIL import Image
#
#
#
# a = Image.open("female.png")
# width, height = a.size
# #
# # print(f"Width: {width} pixels")
# # print(f"Height: {height} pixels")
#
# b = Image.open("./templates/11.jpg")
#
#
# new = b.resize(a.size)
# print(new.size)
# new.save("c.png")


from PIL import Image, ImageDraw

# Open the square image
image = Image.open("a.png")

# Create a circular mask
mask = Image.new("L", image.size, 0)
draw = ImageDraw.Draw(mask)
width, height = image.size
radius = min(width, height) // 2
center = (width // 2, height // 2)
draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), fill=255)

# Apply the mask to the image
result = Image.new("RGBA", image.size)
result.paste(image, mask=mask)

# Save or display the circular image
# result.show()
result.save("cir.png")#
