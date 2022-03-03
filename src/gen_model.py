import os

import PIL
from PIL import Image

import connect_database


def get_id(file_name):
    res = ""
    for c in file_name:
        if '0' <= c <= '9':
            res += c
    return res


check = (
    (46, 52), (47, 52), (46, 53), (47, 53), (46, 54), (47, 54), (46, 55), (47, 55), (46, 56), (47, 56), (46, 57),
    (47, 57),
    (46, 58), (47, 58), (46, 59), (47, 59), (46, 60), (47, 60), (46, 61), (47, 61), (46, 62), (47, 62), (46, 63),
    (47, 63),
    (62, 52), (63, 52), (62, 53), (63, 53), (62, 54), (63, 54), (62, 55), (63, 55), (62, 56), (63, 56), (62, 57),
    (63, 57),
    (62, 58), (63, 58), (62, 59), (63, 59), (62, 60), (63, 60), (62, 61), (63, 61), (62, 62), (63, 62), (62, 63),
    (63, 63))


def get_model(pix):
    for point in check:
        if pix[point[0], point[1]][3] == 255:
            return 'steve'
    return 'alex'


if __name__ == '__main__':
    db = connect_database.open_database_mc_skin()
    for root, dirs, files in os.walk('../../pythonProject5/downloadPNG/'):
        for file in files:
            try:
                img = Image.open('../../pythonProject5/downloadPNG/' + file)
                lst = list()
                bands = img.getbands()
                passageway = ''
                for band in bands:
                    passageway = passageway + band
                connect_database.update_skin_set_passageway_by_id(db=db, skin_id=get_id(file), passageway=passageway)
                if passageway == 'RGBA' and img.size[0] == 64 and img.size[1] == 64:
                    connect_database.update_skin_set_model_by_id(db=db, model=get_model(img.load()),
                                                                 skin_id=get_id(file))

                img.close()
            except PIL.UnidentifiedImageError:
                pass
    connect_database.close_database(db=db)
