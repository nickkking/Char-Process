import re
con=0
nam=0
#补充描述：描述：属征：
def catch():
    c = []
    f=open(r'C:\Users\ImpWa\Desktop\catchkeyindocx\p17\邱师兄博士论文-非终版.txt',encoding='UTF-8')
    lines=f.readlines()
    #print(lines[0])
    p=0
    for line in lines:
        nam = re.findall(("^5\.[3-4].+"), line)
        des =re.findall("^描述.+",line)
        des1=re.findall("^补充描述.+",line)
        des2=re.findall("^属征.+",line)
        if nam:
            p+=1
            print(nam)
            c.append(nam[0])
        if des:
            i=lines.index(line)
            #print(i)
            c.append(des[0])
            while True:
                t = lines[i + 1]
                if re.findall("^分布.+", t) or re.findall("^生物学.+", t):
                    break
                else:
                    c.append(t)
                    #print(i)
                    i=i+1
        if des1:
            i=lines.index(line)
            #print(i)
            c.append(des1[0])
            while True:
                t = lines[i + 1]
                if re.findall("^分布.+", t) or re.findall("^生物学.+", t):
                    break
                else:
                    c.append(t)
                    #print(i)
                    i=i+1
        if des2:
            i=lines.index(line)
            #print(i)
            c.append(des2[0])
            while True:
                t = lines[i + 1]
                if re.findall("^分布.+", t) or re.findall("^生物学.+", t):
                    break
                else:
                    c.append(t)
                    #print(i)
                    i=i+1

   # print(c)
    #print(p)
    f.close()

    f = open(r'p17\t221.txt', 'w+', encoding='utf-8')
    for i in range(len(c)):
        #print(c[i])
        f.write(c[i]+'\n')
    f.close()

if __name__=='__main__':
    catch()











