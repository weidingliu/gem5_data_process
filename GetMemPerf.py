import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

def readOnecsv(path):
    pd_temp = pd.read_csv(path)
    return pd_temp

def getMemPerf(df):
    p = re.compile(r'system\.cpu\.lsq0\..')
    indexs = []
    for i in range(len(df.index)):
        line = df.iloc[i]
        if(re.match(p,line['Name'])):
            indexs.append(i)
    df_out = df.iloc[indexs]
    print(df_out)

# df = readOnecsv("./generates/vs2r.v-0.csv")
# getMemPerf(df)

def getVecViolation():
    filelist = pd.read_csv('./generates/filelist')
    basePath = './generates/'
    sufix = '.csv'
    vecViolationNum = []
    for i in range(filelist.size):
        path = basePath + filelist.loc[i].values + sufix
        df = readOnecsv(path[0])
        vecViolationNum.append(df[df['Name'] == "system.cpu.lsq0.VecMemOrderViolation"]['Perf_Number'].values)
    print(vecViolationNum)
    x = np.array(vecViolationNum)
    y = range(filelist.size)
    print(y)
    plt.hist(x,bins=y,)
    plt.show()

getVecViolation()
        

