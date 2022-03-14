import hmac
import hashlib
import os

import PIL
from PIL import Image

from src import connect_database


def gen_hash(value):
    message = value.encode("utf-8")
    return hmac.new(message, digestmod=hashlib.md5).hexdigest().upper()


def get_id(file_name):
    res = ""
    for c in file_name:
        if '0' <= c <= '9':
            res += c
    return res


if __name__ == '__main__':
    db = connect_database.open_database_mc_skin()
    for root, dirs, files in os.walk('../../pythonProject5/downloadPNG/'):
        for file in files:
            try:
                lst = list()
                img = Image.open('../../pythonProject5/downloadPNG/' + file)
                skin_string = ''
                info = img.load()
                for i in range(0, img.size[0]):
                    for j in range(0, img.size[1]):
                        lst.append(info[i, j])
                print(str(lst))
                connect_database.update_skin_sha256_by_id(db=db, skin_id=get_id(file),
                                                                  sha256=gen_hash(str(lst)))

                img.close()
            except PIL.UnidentifiedImageError:
                pass
    connect_database.close_database(db=db)
