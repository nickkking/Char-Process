# coding = utf-8
p1='p17/t21.txt'
p2='b21.txt'

def clearBlankLine(p1,p2):
    file1 = open(p1, 'r', encoding='utf-8') # 要去掉空行的文件
    file2 = open(p2, 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            if line.startswith('Fig') or line.startswith('图'):
                continue
            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine(p1,p2)

