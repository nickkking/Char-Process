#screen the unmatched value
import os
import pandas as pd
import difflib
tst10=[]
pp=[]
df_E1ce2 = pd.read_excel(r"code2name.xlsx", sheet_name=1)
code=df_E1ce2['code'].tolist()
scode=[x.strip() for x in code]

for fn in os.listdir(r'C:\Users\aklasim\Desktop\LAB\序列分割程序+结果\拟叶蠊py\1'):
    fnm=fn.strip('.docx').strip()
    pp.append(fnm)
    fit = difflib.get_close_matches(fnm, scode, 1, cutoff=1)
    if len(fit) == 0:
        tst10.append(fnm)

print('sum=',len(pp),len(tst10),"个不100%匹配",tst10)
