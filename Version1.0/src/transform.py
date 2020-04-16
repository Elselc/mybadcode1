from PIL import Image
import os


def transform_to(path: str, ergebnistyp: str):
    im = Image.open(path)
    png_path = os.path.splitext(path)[0] + "." + ergebnistyp
    im.save(png_path)
