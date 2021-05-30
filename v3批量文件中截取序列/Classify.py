#classify
import os  # os是用来切换路径和创建文件夹的。
import pandas as pd
from shutil import copy  # shutil 是用来复制黏贴文件的
from tst_docx import tst10

df_c2n = pd.read_excel(r"code2name.xlsx", sheet_name=1)
df_c2n.index = df_c2n['code']
file_path = r'C:\Users\aklasim\Desktop\LAB\序列分割程序+结果\拟叶蠊py\1.3fas'  # 想拆分的文件夹所在路径,也就是一大堆文件所在的路径
save_dir = r'C:\Users\aklasim\Desktop\LAB\序列分割程序+结果\拟叶蠊py\2'  # save_dir 是想把复制出来的文件存放在的路径

# 获取 file_path 下的文件和文件夹列表
# 因为 file_path 里面没有文件夹，所以不处理有文件夹的情况
pathDir = os.listdir(file_path)  # os.listdir(file_path) 是获取指定路径下包含的文件或文件夹列表

r'''for filename in pathDir:  # 遍历pathDir下的所有文件filename
    portion = os.path.splitext(filename)
    if portion[1] == ".docx":
        # 重新组合文件名和后缀名
        newname = portion[0] + ".fas"
        os.rename(r'C:\Users\aklasim\Desktop\LAB\序列分割程序+结果\拟叶蠊py\1\\' + filename, r'C:\Users\aklasim\Desktop\LAB\序列分割程序+结果\拟叶蠊py\1\1\\' + newname)
解码格式错误
'''
for filename in pathDir:
    file_name = filename.strip('.fas').strip()

    if file_name in tst10:
        full = '!un'

    else:
        #file_name=float(file_name)#！！！！！如果index里面是数值类型

        full = df_c2n.name[df_c2n['code'].loc[file_name]]

    dir_name = full.strip()  # 新的文件夹的命名


    from_path = os.path.join(file_path, filename)  # 旧文件的绝对路径(包含文件的后缀名)
    to_path = save_dir + "\\" + dir_name  # 新文件的绝对路径

    if not os.path.isdir(to_path):  # 如果 to_path 目录不存在，则创建
        os.makedirs(to_path)
    copy(from_path, to_path)  # 完成复制黏贴

#Add the Number of files to the folder's name  
path0 = os.listdir(r'C:\Users\aklasim\Desktop\LAB\序列分割程序+结果\拟叶蠊py\2')
for filen in path0:
    path = r'C:\Users\aklasim\Desktop\LAB\序列分割程序+结果\拟叶蠊py\2\\'+filen  # 获取当前路径
    count = 0
    for root, dirs, files in os.walk(path):  # 遍历统计
        for each in files:
            count += 1  # 统计文件夹下文件个数
    os.rename(path, path + ' ' + str(count) + '条')  # 输出结果
