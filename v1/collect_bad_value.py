#find the unmatched value
import pandas as pd
import difflib

bad_val = []
df_E2a = pd.read_excel("E2a.xlsx")
f=open(r'E:\新建文件夹\新建文件夹\COI(1).fas')
for line in f:
    if line.startswith(">"):
        new=line.lstrip('>').strip('\n')
        a=difflib.get_close_matches(new,df_E2a['ab.'],1, cutoff=1) # match the same value
        if len(a)==0:
            bad_val.append(new)




