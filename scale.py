# 归一化数据集

import numpy as np
import shutil
import Global_V


def scale(dataset):
    max = float("-inf")
    min = float("inf")
    for x in dataset:
        ma = np.max(x)
        mi = np.min(x)
        if ma > max:
            max = ma
        if mi < min:
            min = mi
    res = [(x-min) / (max - min) for x in dataset]
    return res


PATH = Global_V.PATH
# DEEP='14/'
SPEEDS = ['1730', '1797', '1750', '1772']
TRAIN = Global_V.TRAIN_FILE_EXTENSION
LABEL = Global_V.LABEL_FILE_EXTENSION

SAVE_PATH = 'scale/'
for speed in SPEEDS:
    train_path = PATH + speed + TRAIN
    label_path = PATH + speed + LABEL
    train = np.load(train_path)
    label = np.load(label_path)

    train = scale(train)

    np.save(PATH + SAVE_PATH + speed + TRAIN, train)
    shutil.copyfile(label_path, PATH + SAVE_PATH + speed + LABEL)
# np.save(SAVE_PATH+SPEED+LABEL,label)
