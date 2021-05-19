import os
import pandas as pd
file_path=os.path.abspath(r"E:\新建文件夹\新建文件夹")
df_E2a = pd.read_excel("E2a.xlsx")
df_ce2e = pd.read_excel("E:\pythonProject1\CE2E.xlsx")

df_E2a.index = df_E2a['ab.']
a = ">"

f=open(r'E:\新建文件夹\新建文件夹\COI(1).fas')
for line in f:
    if line.startswith(">"):
        new=line.lstrip('>').strip('\n')

        full = df_E2a.name[df_E2a['ab.'].loc[new]]
        outfile = open("E:\新建文件夹\新建文件夹\db\\"+"%s"%full + '.' + 'fas',"w")
        outfile.write(line+next(f))
        outfile.close()
        break



print("Finished") #分析完成标记
