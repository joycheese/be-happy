# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:10:31 2020

@author: yang30
"""


import pandas as pd
import matplotlib.pyplot as plt
from getfile import getfile

def plotjv(filetxt_list):
    import numpy as np    
    lJd=[]
    #读取电压电流数据，并将格式series转换list
    for file in filetxt_list:
        df=pd.read_table(file)
        bias=df.iloc[:,0].tolist()
        I=abs(df.iloc[:,1]-df.iloc[:,3]).tolist()
        
        #列表推导式。电流转为电流密度
        J=[element/0.26 for element in I]
        Jabs=[abs(element) for element in J]
        
        #寻找0V，1.5V的index，前后各走5步
        zeroV=bias.index(0)       #0V附近算出Rsh
        Rsh=(bias[zeroV+5]-bias[zeroV-5])/(J[zeroV+5]-J[zeroV-5])
    
        onefiveV=bias.index(1.5)  #1.5V附近算出Rs
        Rs=(bias[onefiveV+5]-bias[onefiveV-5])/(J[onefiveV+5]-J[onefiveV-5])
    
        print(f'filename： {file}')
        print(f'Jd @ -2V = {abs(J[bias.index(-2)]):.2e} A/cm²')
        print(f'Rsh = {Rsh:.2e} Ω/cm²\nRs = {Rs:.2e} Ω/cm²\n')
        lJd.append(abs(J[bias.index(-2)]))
        '''Vrev=[]
        for element in bias:
            Vrev.append(abs(element))
        Jcorr=[]
        Jsh=[]
        for element in Jabs:
            index=Jabs.index(element)
            Jcorr.append(element-(Vrev[index]-element*Rs)/Rsh)
            Jsh.append((Vrev[index]-element*Rs)/Rsh)'''
    
        plt.yscale('log')
        #plt.xscale('log')
        plt.tick_params(labelsize=23)
        plt.xlabel('bias (V)',size=23)
        plt.ylabel('Jdark (A/${cm^2)}$',size=23)
        plt.xlim(-3,2)
        plt.ylim(5e-13,2e-3)
        plt.grid(True)
        plt.plot(bias,Jabs)
        
        #plt.plot(Vrev,Jcorr)
        #plt.plot(bias,Jsh)
        plt.title('ETL = C60 / LiF / Al',size=26)
        #plt.text(-2.8,1e-7,f'Jd @ -2V = {abs(J[bias.index(-2)]):.2e} A/cm²\nRsh = {Rsh:.2e} Ω/cm²\nRs = {Rs:.2e} Ω/cm²\n',fontsize=15,style='normal')
    mat = np.array(lJd)
    plt.text(-2.8,1e-5,f'Jd @ -2V= {np.mean(mat):.2e} ± {np.std(mat):.2e}({min(lJd):.2e}) A/cm²',fontsize=25,style='normal')
    print(f'Jd @ -2V= {np.mean(mat):.2e} ± {np.std(mat):.2e}({min(lJd):.2e}) A/cm²')
    
#输入文件夹及关键字，路径'\'用'/'代替
plt.figure(figsize = (16,9))  #设置图片大小
filetxt_list=getfile('jv/ps-20200627','.txt','s2','')
plotjv(filetxt_list)

'''filetxt_list=getfile('jv/ps-20200707','.txt','s3','')
plotjv(filetxt_list)'''

'''getfile('jv/ps-20200701','s2','0.01')
plotjv(filetxt_list)
getfile('jv/ps-20200701','s3','0.01')
plotjv(filetxt_list)
filetxt_list=[]'''

plt.show()