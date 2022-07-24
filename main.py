
import yaml
from pathlib import Path
from PIL import Image

with open("config.yml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


def merge(im1, im2):
    w = im1.size[0]
    h = im1.size[1]
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, None, im2)

    return im


def setup():
    image1 = Image.open('images/image1.jpg')
    image2 = Image.open('images/image2.png')

    result = merge(image1, image2)
    # result.save('images/imageresult.png')

    print(Path.cwd())
    result.show()


# Start program:
setup()

# Loop program:
while True:
    exit()