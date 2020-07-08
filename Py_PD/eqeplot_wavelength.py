# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:57:36 2020

@author: yang30
"""


import pandas as pd
import matplotlib.pyplot as plt
from getfile import getfile

filetxt_list=getfile('eqe\eqe20200621','.xlsx','-2V','s6')

#把符合条件的数据绘图

plt.xlabel('wavelength (nm)')
plt.ylabel('EQE (%)')
plt.xlim(400,1050)
plt.ylim(0,80)
plt.grid(True)
    
for file in filetxt_list:
    dfeqe=pd.read_excel(file)
    EQE=dfeqe.iloc[:,1].tolist()
    wavelength=dfeqe.iloc[:,0].tolist()
    
    plt.plot(wavelength,EQE,label=file)

plt.legend()   
plt.show()