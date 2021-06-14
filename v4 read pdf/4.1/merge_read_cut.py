#merge all pdfs
import os
from PyPDF2 import PdfFileMerger

pth=os.getcwd()


target_path = pth+'/pdf'#所有pdf所在文件夹

pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

file_merger = PdfFileMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)     # 合并pdf文件

file_merger.write("merge.pdf")
#########################################################################################
#read
import os,pdfplumber

file = os.path.expanduser(".\merge.pdf")

with pdfplumber.open(file) as pdf:
    for i in range(0,len(pdf.pages)):
        first_page = pdf.pages[i]

        text = first_page.extract_text()
        with open('all.txt', 'a') as f:
            print(text)
            f.write(text)

#######################################cut#######################################################
import re,os
con=0
c=[]
nam=0

f=open(r'all.txt')
txtfd=os.getcwd()+"\\txt"
if not os.path.isdir(txtfd):  # 如果 _path 目录不存在，则创建
                os.makedirs(txtfd)
for line in f:
    if line.startswith("工单编号"):
        nam=re.findall("工单编号"+"\s\d+",line)
        nam=nam[0]
        print(nam)
        outfile = open(txtfd + "\\%s" % nam + '.' + 'txt', "a+")
        outfile.write(line)
        outfile.close()
        con = nam

    else:
        outfile = open(txtfd + "\\%s" % nam + '.' + 'txt', "a+")
        outfile.write(line)
        outfile.close()
