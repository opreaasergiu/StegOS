from PIL import Image
from PIL import ImageChops

image1 = "cat2.jpg"
image2 = "douaimagini2.png"
img_difference = "difference.png"

im1 = Image.open(image1)
im2 = Image.open(image2)

diff = ImageChops.difference(im2, im1)

diff.save(img_difference)