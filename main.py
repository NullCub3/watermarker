
import yaml
from pathlib import Path
from PIL import Image

with open("config.yml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

photos_path = Path(config["photos_dir"])


def merge(im1, im2):
    w = im1.size[0]
    h = im1.size[1]
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, None, im2)

    return im


if __name__ == "__main__":
    print(photos_path)
    print(config)

    # Loop program:
    while True:
        exit()