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
    vecViolationNum = np.array([])
    for i in range(filelist.size):
        path = basePath + filelist.loc[i].values + sufix
        df = readOnecsv(path[0])
        vecViolationNum = np.append(vecViolationNum, df[df['Name'] == "system.cpu.lsq0.VecMemOrderViolation"]['Perf_Number'].values)
        if(df.size == 0):
            continue
        if (df[df['Name'] == "system.cpu.lsq0.VecMemOrderViolation"]['Perf_Number'].values > 100):
            print(df[df['Name'] == "system.cpu.lsq0.VecMemOrderViolation"])
    x = vecViolationNum
    print(x)
    y = range(filelist.size)
    plt.hist(x,bins=y)
    plt.show()

def getMeanloadtouse():
    filelist = pd.read_csv('./generates/filelist')
    basePath = './generates/'
    sufix = '.csv'
    vecMeanLoadtoUse = np.array([])
    scaleMeanLoadtoUse = np.array([])
    for i in range(filelist.size):
        path = basePath + filelist.loc[i].values + sufix
        df = readOnecsv(path[0])
        vecMeanLoadtoUse = np.append(vecMeanLoadtoUse, df[df['Name'] == "system.cpu.lsq0.vecLoadToUse::mean"]['Perf_Number'].values)
        scaleMeanLoadtoUse = np.append(scaleMeanLoadtoUse, df[df['Name'] == "system.cpu.lsq0.scaleLoadToUse::mean"]['Perf_Number'].values)
    x = vecMeanLoadtoUse
    print(x)
    y = range(filelist.size)
    plt.subplot(2,1,1)
    plt.hist(x,bins=y)
    plt.title("vector Load to use")

    plt.subplot(2,1,2)
    plt.hist(scaleMeanLoadtoUse,bins=y)
    plt.title("scale Load to use")
    plt.show()

getVecViolation()
getMeanloadtouse()

