#classify序列放入以物种命名的文件夹

import os  #切换路径和创建文件夹
import pandas as pd
from tst import bad_val
from shutil import copy  #复制粘贴贴文件
df_E2a = pd.read_excel("E2a.xlsx")
df_E2a.index = df_E2a['ab.']
file_path = r'E:\新建文件夹\新建文件夹\db'  # 想拆分的文件夹所在路径,也就是一大堆文件所在的路径
save_dir = r'E:\新建文件夹\新建文件夹\class'  # save_dir 是想把复制出来的文件存放在的路径


# 获取 file_path 下的文件和文件夹列表
# 因为 file_path 里面没有文件夹，所以不处理有文件夹的情况
pathDir = os.listdir(file_path)  # os.listdir(file_path) 是获取指定路径下包含的文件或文件夹列表
for filename in pathDir:  # 遍历pathDir下的所有文件filename
    file_name = filename.split('.')[0]  #去除后缀

    if file_name in bad_val:#找不到对应值
        full = '!Not found!'
    else:
        full = df_E2a.name[df_E2a['ab.'].loc[file_name]]#序列缩写对应物种名

    dir_name = full.strip()  # 新的文件夹的命名


    from_path = os.path.join(file_path, filename)  # 旧文件的绝对路径(包含文件的后缀名)
    to_path = save_dir + "\\" + dir_name  # 新文件的绝对路径

    if not os.path.isdir(to_path):  # 创建文件夹（如果路径不存在）
        os.makedirs(to_path)
    copy(from_path, to_path)  # 完成复制
