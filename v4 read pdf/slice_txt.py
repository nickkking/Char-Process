import re
con=0
c=[]
nam=0

f=open(r'1.txt')

for line in f:
    if line.startswith("工单编号"):
        nam=re.findall("工单编号"+"\s\d+",line)
        nam=nam[0]
        print(nam)
        outfile = open(r"C:\Users\aklasim\Desktop\Py6.11 Pdf\t1\\" + "%s" % nam + '.' + 'txt', "a+")
        outfile.write(line)
        outfile.close()
        con = nam

    else:
        outfile = open(r"C:\Users\aklasim\Desktop\Py6.11 Pdf\t1\\" + "%s" % nam + '.' + 'txt', "a+")
        outfile.write(line)
        outfile.close()














