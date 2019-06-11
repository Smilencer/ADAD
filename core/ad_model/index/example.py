import numpy as np
# import pandas as pd

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
from keras.models import *


def diagnosis_AD_index(test):
    model = load_model('core/ad_model/index/adatten.m')
    # 模型输入：输入三次患者量表数据，顺序为['AGE','PTGENDER','FDG','MMSE','RAVLT.forgetting','FAQ','CDRSB.bl']

    # test = [[
    # 	[77.3,1,5.575461927,27.0,8.0,7.0,1.5],
    # 	[77.3,1,5.51286926,25.0,3.0,2.0,1.5],
    # 	[77.3,1,5.317821432,22.0,2.0,10.0,1.5]
    #     ]]
    test = np.array(test)
    print('test',test)
    test = test/255.
    result = model.predict(test)
    for i in result:
        i = i.tolist()
    maxi = i.index(max(i))
    if maxi == 2:
        print('痴呆')
        return '痴呆'
    elif maxi == 1:
        print('认知障碍')
        return '认知障碍'
    elif maxi == 0:
        print('正常')
        return '正常'
    print(result)
