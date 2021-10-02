#将docx转为txt
import os
from docx import Document
from tqdm import tqdm #progressBar
p1=r'C:\Users\ImpWa\Desktop\catchkeyindocx'
p2='.\p17'
def docx2txt(path,path1):

    for filename in os.listdir(path):
        if filename.endswith('.docx') and not filename.startswith('~$'):
            file_path = os.path.join(path, filename)
            document = Document(file_path)
            txt_path = os.path.join(path1, str(filename.strip('.docx'))+'.txt')#terminal path
            if not os.path.isdir(path1):  # 如果 _path 目录不存在，则创建
                os.makedirs(path1)
            f = open(txt_path, 'w', encoding='utf-8')#utf-8！！！！！！！！！！！！！！


            for paragraph in tqdm(document.paragraphs):#进度条
                f.write(paragraph.text.strip('.docx').strip()+'\n')
            f.close()



if __name__ == '__main__':
    docx2txt(p1,p2)