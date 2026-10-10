import os
import pillow_heif
from PIL import Image

pillow_heif.register_heif_opener()


def main(images):
    for img in images:
        image = Image.open(f"./images/{img}")
        filename_list = image.filename.split("/")
        filename_noext = filename_list[len(filename_list) - 1]
        print(filename_noext)
        filename = filename_noext.split(".")[0]
        image.convert("RGB").save(f"./output/{filename}.jpg", "JPEG")


if __name__ == "__main__":
    images = os.listdir(f"./images/")
    main(images)
