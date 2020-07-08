# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:30:05 2020

@author: yang30
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

#指定data文件所在路径文件夹
os.chdir(r'C:\Users\yang30\Desktop\data\jv\simulator\20200606')
file_chdir=os.getcwd()
filetxt_list=[]

#将所有符合条件的文件列入filetxt_list
for root,dirs,files in os.walk(file_chdir):
    for file in files:
        if 's3' in os.path.splitext(file)[0] and '-5' in os.path.splitext(file)[0] and '.dat'==os.path.splitext(file)[1]:
            filetxt_list.append(file)

#把符合条件的数据绘图
plt.yscale('log')
plt.xlabel('bias (V)')
plt.ylabel('Current Density (A/${cm^2)}$')
plt.xlim(-3,2)
plt.grid(True)
    
for file in filetxt_list:
    df=pd.read_table(file)
    bias=df.iloc[:,1].tolist()
    I=abs(df.iloc[:,2]).tolist()

    J=[]
    for element in I:
        J.append(element/0.26)
    
    plt.plot(bias,J)


plt.show()