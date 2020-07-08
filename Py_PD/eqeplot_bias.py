# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:10:54 2020

@author: yang30
"""


import pandas as pd
import matplotlib.pyplot as plt
from getfile import getfile

#指定data文件所在路径文件夹，默认母目录为C:\Users\yang30\Desktop\data\          
filetxt_list=getfile('eqe\eqe20200621','.xlsx','940','s6')

#把符合条件的数据绘图
plt.figure(figsize = (16,9))
plt.tick_params(labelsize=23)
plt.xlabel('bias (V)',size=23)
plt.ylabel('EQE',size=23)
plt.xlim(-5,0)
plt.title('NiO/polyTPD/PTB7-Th:AOT3/C60:LiF/Al',size=26)
plt.grid(True)
    
for file in filetxt_list:
    dfeqe=pd.read_excel(file)
    EQE=dfeqe.iloc[:,1].tolist()
    bias=dfeqe.iloc[:,0].tolist()
    
    plt.plot(bias,EQE)

plt.legend()   
plt.show()