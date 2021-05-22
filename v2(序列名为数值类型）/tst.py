#find the unmatched value
import pandas as pd
import difflib

bad_val = []
pp = []
df_E1ce2 = pd.read_excel(r"C:\Users\aklasim\Desktop\jl\E1CE2.xlsx", sheet_name=1)


code=df_E1ce2['COI'].tolist()
scode=[str(x) for x in code]
#code=repr(code)用不了



f=open(r'C:\Users\aklasim\Desktop\jl\co1.fas')
for line in f:
    if line.startswith(">"):
        new=line.lstrip('>').strip('\n').strip()
        pp.append(new)
        a=difflib.get_close_matches(new,scode,1, cutoff=1)
        if len(a)==0:
            bad_val.append(new)


print(len(bad_val),"个匹配不上",'\n',bad_val)

