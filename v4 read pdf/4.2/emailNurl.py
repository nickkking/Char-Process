# -*- coding: utf-8 -*-

import re,os
import pandas as pd
x=0
cols=['Company Name','Email','Website']
dfb = pd.DataFrame(columns=cols)


pt=(r'.\t1')
pathDir=os.listdir(pt)

for filename in pathDir:
    x=x+1
    df = pd.DataFrame(index=range(2), columns=cols)
    l = []
    w=[]
    m=[]
    #pt = (r'C:\Users\aklasim\Desktop\py625\1.txt')
    f = open(pt + '\\' + filename, encoding='utf-8')
    for line in f:

        nm = re.match('[A-Z]\d\s\d+', line)#426
        wb = re.findall(r'www.[a-zA-Z0-9\_\-\.]+[com|cn|net]', line, re.IGNORECASE)  # 匹配模式
        em = re.findall(r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?",line, re.IGNORECASE)
        #p=re.findall('(^\d+)\s(\d+)\s((\S*\s*)+)\s(\D+|M3)\s((\d\.*\d*\s*)+)\n', line)
        if nm:
            #1678
            try:
                nm=line+next(f)
            except StopIteration:pass

            l.append(nm)
        if wb:
            wb=wb[0]
            w.append(wb)
        if em:
            em=em[0]
            m.append(em)


    df['Company Name']=pd.Series(l)
    df['Email']=pd.Series(m)
    df['Website']=pd.Series(w)
    dfb = pd.concat([dfb, df])
    f.close()
    print(x)
dfb=dfb.dropna(axis=0,how='all')
dfb.to_csv(r'C:\Users\aklasim\Desktop\py625\3c.csv',index=False,encoding='utf-8')
#df.to_csv(r'C:\Users\aklasim\Desktop\py625\company name.csv',index=False,encoding='gbk')
#df.to_excel(r'C:\Users\aklasim\Desktop\py625\company name.xlsx',index=False,encoding='utf-8')

print(x)
