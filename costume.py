import sys
from PIL import Image

images =[]

# iterate over your cmd line arguments except the first one, which is the name of the script
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# save the first image to the file, append all other images to it, then set duration and loop forever
images[0].save('costume.gif', save_all=True, append_images=images[1:], duration=200, loop=0)
