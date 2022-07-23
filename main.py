
import yaml
import pathlib

with open("config.yml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

print(config["photos_dir"])
