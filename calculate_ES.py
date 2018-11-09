# coding=utf-8
import numpy as np
import math
import queue

from scipy.signal import hilbert
from scipy.fftpack import fft

def cal_es(signal,window_size):
    ''' 返回window_size 大小的包络谱信号'''

    # 计算hilbert 信号值
    BA=hilbert(signal)
    hb_signal=np.abs(BA)

    hb2=np.power(hb_signal,2)

    signal2=np.power(signal, 2)

    es2=hb2+signal2
    hb_signal =[]
    for i in es2:
        hb_signal.append(np.sqrt(i))

    # 计算傅立叶信号值
    fft_signal=fft(hb_signal,window_size)
    es=np.abs(fft_signal)/len(fft_signal)

    return es
