#split into single seq


f=open(r'C:\Users\aklasim\Desktop\jl\co1.fas')

for line in f:
    if line.startswith(">"):
        new=line.lstrip('>').strip('\n').strip()

        #print(type(new))
        '''
        if new in bad_val:
            full = 'Not found!'+ new
        else:
            full = df_E1ce2.name[df_E1ce2['COI'].loc[new]]
            '''
        outfile = open("E:\新建文件夹\新建文件夹\jl\\"+"%s"%new + '.' + 'fas',"w")
        outfile.write(line+next(f))
        outfile.close()





print("Finished")