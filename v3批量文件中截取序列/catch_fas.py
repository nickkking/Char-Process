#catch the seq in txt files
import os  

pathDir=os.listdir(r'C:\Users\aklasim\Desktop\LAB\序列分割程序+结果\拟叶蠊py\1.1')
pt=(r'C:\Users\aklasim\Desktop\LAB\序列分割程序+结果\拟叶蠊py\1.1')

for filename in pathDir:
    f = open(pt+'\\'+filename,encoding='utf-8')
    fn=filename.strip('.txt')

    for line in f:
        if line.startswith(">"):
            new = line.lstrip('>').strip('\n').strip()

            try:
                while True:
                    nl = next(f)
            except StopIteration:
                pass
              
            outfile = open(r"C:\Users\aklasim\Desktop\LAB\序列分割程序+结果\拟叶蠊py\1.3\\" + fn+ '.' + 'fas', "w")
            outfile.write(line+nl)
            outfile.close() 
            
                

    print("Finished"+fn)


