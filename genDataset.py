# script to generate samples saved with npy format
# each dataset having 360 samples
# Data with same rpm is grouped as one dataset which comprises four bearing condtions with 90 samples for each condition

# Data come from http://csegroups.case.edu/bearingdatacenter/pages/download-data-file
# rotational speed：1797rpm and 1730rmp
# frequency: 12KHZ
# 从给定的数据集中随机截取size个样本点 截num_size个样本每种条件

# 取driven end 的数据，从原始的数据总抽取我们需要的用于训练的数据集
# label normal,inner,ball,outer:0,1,2,3


import numpy as np
import pandas as pd
from scipy import io
import re
import Global_V  # 全局变量

path = 'mat-data/'
deep = '14'
sub_path = ['1797', '1730', '1772', '1750']
LABEL_NAME = Global_V.LABEL_NAME
SAVE_PATH = 'SLHP_verify/'

NUM_SAMPLE = 100                        # 样本数
SEGMENT_NUM = Global_V.WINDOW_LENGTH    # 混杂数据段的条数
SIZE = Global_V.WINDOW_WIDE             # 数据采样窗口
SPECIES = Global_V.NUM_LABELS           # 数据种类

for i in range(len(sub_path)):
    sig = []
    for j in range(len(LABEL_NAME)):
        features_struct = io.loadmat(path + deep + '/' + sub_path[i] + '/' + LABEL_NAME[j] + '.mat')
        keys = list(features_struct.keys())

        name = []
        for x in keys:
            name.append(re.findall(r'[X0-9]*_DE_[a-z]*', x))

        for x in name:
            if x != []:
                De = x[0]

        DE = pd.DataFrame(features_struct[De])
        DE.columns = ['DE']
        De = np.array(DE).reshape(len(DE))
        sig.append(De)

    dataset = []
    label = []

    for j in range(NUM_SAMPLE):
        data = []

        # 生成normal样本
        for segmentNum in range(SEGMENT_NUM):
            np.random.seed(segmentNum * j + segmentNum)
            x = np.random.randint(12000)
            data.append(sig[0][x:x + SIZE])
        dataset.append(data)
        label.append(0)

        # 生成异常样本
        for species in range(1, SPECIES):
            data = []
            np.random.seed(species + 542)
            insert = np.random.randint(90, size=1)

            for segmentNum in range(SEGMENT_NUM):
                np.random.seed(segmentNum * j + segmentNum)
                x = np.random.randint(12000)
                if (segmentNum in insert):
                    data.append(sig[species][x:x + SIZE])
                else:
                    data.append(sig[0][x:x + SIZE])
            dataset.append(data)
            label.append(species)
    print(np.shape(dataset))

    np.save(SAVE_PATH + sub_path[i] + '_train.npy', dataset)
    np.save(SAVE_PATH + sub_path[i] + '_label.npy', label)

'''
for x in dataset:
    es_data.append(calculate_ES.cal_es(x,window_size))
    np.save('pre-data/'+sub_path[i]+'_train.npy',es_data)
    np.save('pre-data/'+sub_path[i]+'_label.npy',label)
'''
