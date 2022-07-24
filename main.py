import yaml
from pathlib import Path
from PIL import Image
import logging

with open("config.yml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

photos_path = Path(config["photos_dir"])
logging.basicConfig(level=config["logging_level"])


def merge(im1, im2):
    w = im1.size[0]
    h = im1.size[1]
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, None, im2)

    return im


if __name__ == "__main__":

    # Check to make sure that all the folders are present in the photos directory
    for x in config["folders"]:
        tempPath = photos_path / config["folders"][x]
        if tempPath.exists():
            logging.debug(str(x) + " folder was found!")
        else:
            raise Exception("Filestructure Error, '" + str(x) + "' folder does not exist")

    # Check to make sure all the watermarks are in the folder
    water_path = photos_path / config["folders"]["WATERMARK"]
    for x in config["watermarks"]:
        for y in config["watermarks"][x]:
            checkFileDir = water_path / config["watermarks"][x][y]
            if checkFileDir.is_file():
                logging.debug(str(y) + " watermark file was found!")
            else:
                raise Exception("File Error, '" + str(y) + "' watermark does not exist")

    # Loop program:
    # while True:
