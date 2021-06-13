# -*- coding: utf-8 -*-

import re,pandas as pd,numpy as np
from pandas import DataFrame
import os

pathDir=os.listdir(r'C:\Users\aklasim\Desktop\Py6.11 Pdf\t1')
pt=(r'C:\Users\aklasim\Desktop\Py6.11 Pdf\t1')


cols=['工单编号','上级工单编号','项目编号','工单描述','上级工单描述','施工单位','合同号','计划服务费','开工日期','完工日期','作业类型','通知单创建','通知单批准','计划','待审','下达','验收确认','完工确认','完工时间','打印者','打印日期','工序号','工作中心','控制码','工序内容','计划量','签证','物料编码','物料描述','单位计划量','出库量','签证']
l=[]
x=0
l1=[]
dfb = pd.DataFrame(columns=['工单编号', '上级工单编号', '项目编号', '工单描述', '上级工单描述', '施工单位', '合同号', '计划服务费','开工日期', '完工日期', '作业类型', '通知单创建', '通知单批准', '计划', '待审', '下达', '验收确认','完工确认', '完工时间', '打印者', '打印日期', '工序号', '工作中心', '控制码', '工序内容', '计划量',
'签证', '物料编码', '物料描述', '单位计划量', '出库量', '签证', '单位', '数量确认'])

for filename in pathDir:
    x=x+1
    df = pd.DataFrame(index=range(30), columns=cols)


    def gg(rg,n):
        e=[]
        f = open(pt + '\\' + filename, encoding='gbk')
        for line in f:
            d=re.search(rg,line)

            if d:
                d=str(d.group())
                e.append(d)
        print(e)

        df[n]=pd.Series(e)
        f.close()
    desc=gg('工单描述\s\S+','工单描述')#desc = re.findall('工单描述\s\S+', line)
    n=gg('工单编号\s\d+','工单编号')
    up_n=gg('上级工单编号\s\d+','上级工单编号')    #sup_desc = re.findall('上级工单描述\s\d+', line)
    pro_n=gg('项目编号\s\d+','项目编号')    #pro_co=re.findall('项目编号\s\d+',line)
    unit=gg('施工单位\s\S+','施工单位')#unit= re.findall('施工单位\s\S+', line)
    contr_co=gg('合同号\s\d+','合同号')    #contr_co = re.findall('合同号\s\d+', line)
    cost=gg('计划服务费\s+\d+\,*\d*\.\d+','计划服务费')#cost = re.findall('计划服务费\s+\d+\,*\d*\.\d+', line)
        #if len(cost)>0:
        #    money=cost[0].split()[1]
    start_d=gg('开工日期\s\S+','开工日期')#start_d = re.findall('开工日期\s\S+', line)
    over_d=gg('完工日期\s\S+','完工日期')#over_d = re.findall('完工日期\s\S+', line)
    worktp = gg('作业类型\s\S+', '作业类型')#worktp = re.findall('作业类型\s\S+', line)
        #ntc_crt = re.findall('通知单创建\s\S+', line)
        #ntc_pmt = re.findall('通知单批准\s\S+', line)
        #plan = re.findall('计划\s\S+', line)
        #ass= re.findall('待审\s\S+', line)
        #order= re.findall('下达\s\S+', line)
        #acpt_ck = re.findall('验收确认\s\S+', line)
        #fns_ck = re.findall('完工确认\s\S+', line)
        #fns_tm = re.findall('完工时间\s\S+', line)
        #printer = re.findall('打印者：\S+', line)
        #prt_d = re.findall('打印日期：\d+-\d+-\d+', line)
    ntc_crt = gg('通知单创建\s\S+', '通知单创建')
    ntc_pmt = gg('通知单批准\s\S+', '通知单批准')
    plan = gg('计划\s\S+', '计划')
    ass= gg('待审\s\S+', '待审')
    order= gg('下达\s\S+', '下达')
    acpt_ck = gg('验收确认\s\S+', '验收确认')
    fns_ck = gg('完工确认\s\S+', '完工确认')
    fns_tm = gg('完工时间\s\S+', '完工时间')
    printer = gg('打印者：\S+', '打印者')
    prt_d = gg('打印日期：\d+-\d+-\d+', '打印日期')

    wp_num = []
    wk_ctr = []
    ctr_code = []
    wp_contts = []
    cert = []

    f = open(pt + '\\' + filename, encoding='gbk')
    for line in f:
        proc_set = re.findall('(^\d+)\s(\D+\d*)(\D+\d*)\s((\S*\d*\s*\.*)+)(\d+\.*\d*\D+)+\n', line)#426
        if proc_set:# 工序号/工作中心/控制码/工序内容/签证
            sets=list(proc_set[0])
            wp_num.append(sets[0])
            wk_ctr.append (sets[1])
            ctr_code.append (sets[2])
            wp_contts.append (sets[3])
            cert.append (sets[5])

    df['工序号']=pd.Series(wp_num)
    df['工作中心']=pd.Series(wk_ctr)
    df['控制码']=pd.Series(ctr_code)
    df['工序内容']=pd.Series(wp_contts)
    df['签证']=pd.Series(cert)

    wp_num = []
    mat_code = []
    mat_descr = []
    msr_unit = []
    all_num = []
    cert=[]
    f.close()
    f = open(pt + '\\' + filename, encoding='gbk')
    for line in f:

        mat_set = re.findall('(^\d+)\s(\d+)\s((\S*\s*)+)\s(\D)\s((\d\.*\d*\s*)+)\n', line)  # 140
        if mat_set:  # 工序号/物料编码/物料描述/单位/数量确认/计划量/出库量/签证
            sets = list(mat_set[0])
            wp_num.append(sets[0])
            mat_code.append(sets[1])
            mat_descr.append(sets[2])
            msr_unit.append(sets[4])
            all_num.append(sets[5])
            cert.append(sets[6])

    df['工序号']=pd.Series(wp_num)
    df['物料编码']=pd.Series(mat_code)
    df['物料描述']=pd.Series(mat_descr)
    df['单位']=pd.Series(msr_unit)
    df['数量确认']=pd.Series(all_num)
    df['签证']=pd.Series(cert)
    filename=int(x)
    print(dfb.columns)
    print(df.columns)
    dfb=pd.concat([dfb,df])
    f.close()
dfb=dfb.dropna(axis=0,how='all')
dfb.to_csv('C:/Users/aklasim/Desktop/Py6.11 Pdf/t2\！.csv',index=False,encoding='gbk')
#df.to_csv('C:/Users/aklasim/Desktop/Py6.11 Pdf/t2\%s.csv'%filename,encoding='gbk',index=False)

# f=open(r"1.txt")
# f=open(r"t1/工单编号 500042728.txt")

# def fb(a):
#     e=[]
#     for line in f:
#         d=re.findall(a,line)
#         if d:
#             e.append(d)
#     print(e)
#     e=DataFrame(e)
#     print(e)
#     return e


# for line in f:
#     d=re.search('工单编号\s\d+',line)
#
#     if d:
#         d=str(d.group())
#         l.append(d)
# df['工单编号'].append(l)

# for line in f:
#     proc_set = re.findall('(^\d+)\s(\D+\d*)(\D+\d*)\s((\S*\d*\s*\.*)+)(\d+\.*\d*\D+)+\n', line)#426
#     if proc_set:# 工序号/工作中心/控制码/工序内容/签证
#         sets=list(proc_set[0])
#         wp_num = sets[0]
#         wk_ctr = sets[1]
#         ctr_code = sets[2]
#         wp_contts = sets[3]
#         cert = sets[5]
# for line in f:
#     mat_set = re.findall('(^\d+)\s(\d+)\s((\S*\s*)+)\s(\D)\s((\d\.*\d*\s*)+)\n', line)  # 140
#     if mat_set:  # 工序号/物料编码/物料描述/单位/数量确认/计划量/出库量/签证
#         sets = list(mat_set[0])
#         wp_num = sets[0]
#         mat_code = sets[1]
#         mat_descr = sets[2]
#         msr_unit = sets[4]
#         all_num = sets[5]
#         cert=sets[6]
#         print(msr_unit)

