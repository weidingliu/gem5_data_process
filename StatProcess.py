import pandas as pd
import re

p = re.compile(r'\s*#.*$')
BasePath = './m5out/'

def readOneFile(path):
    df = pd.DataFrame()
    with open(path, "r") as f:
        lines = f.readlines()
    data = []
    for line in lines[2:-2]:
        line = line.strip()
        data.append(p.sub('',line).split())
    df_tmp = pd.DataFrame(data, columns = ['Name', 'Perf_Number','1','2'])
    df_tmp['filename'] = path  # 添加文件名列
    df = pd.concat([df, df_tmp], ignore_index=True)
    df = df[['Name','Perf_Number','filename']]
    return df

def save_df(name,df):
    path = './generates/' + name + '.csv'
    df.to_csv(path)

def GetAll():
    filelist = pd.read_csv('./generates/filelist')
    for i in range(filelist.size):
        path = BasePath + filelist.loc[i].values + '/stats.txt'
        df = readOneFile(path[0])
        save_df(filelist.loc[i].values[0],df)


if __name__ == "__main__":
    GetAll()
    print("stats data clean finish.")

