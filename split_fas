import os
file_path=os.path.abspath(r"E:\新建文件夹\新建文件夹")
a = ">"
f=open(r'E:\新建文件夹\新建文件夹\COI(1).fas')
for line in f:
    if line.startswith(">"):
        new=line.lstrip('>').strip('\n')
        outfile = open("E:\新建文件夹\新建文件夹\db\\"+"%s"%new + '.' + 'fas',"w")
        outfile.write(line+next(f))
        outfile.close()
    


print("Finished") #分析完成标记
