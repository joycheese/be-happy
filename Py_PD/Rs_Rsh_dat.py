# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 23:52:37 2020

@author: yang30
"""


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
    #读取电压电流数据，并将格式series转换list
    l=[]
    ljsc=[]
    for file in filetxt_list:
        df=pd.read_table(file)
        bias=df.iloc[:,1].tolist()
        I=df.iloc[:,2].tolist()
        
        #电流转为电流密度
        J=[element/0.26 for element in I]
        Jabs=[abs(element) for element in J]
        
        #寻找0V，1.5V的index，前后各走5步
        zeroV=bias.index(0)       #0V附近算出Rsh
        Rsh=(bias[zeroV+5]-bias[zeroV-5])/(J[zeroV+5]-J[zeroV-5])
    
        onefiveV=bias.index(1.5)  #1.5V附近算出Rs
        Rs=(bias[onefiveV+5]-bias[onefiveV-5])/(J[onefiveV+5]-J[onefiveV-5])
    
        print(f'filename： {file}')
        print(f'Rsh = {Rsh:.2e} Ω/cm²\nRs = {Rs:.2e} Ω/cm²')
        print(f'Voc = {bias[Jabs.index(min(Jabs))]:.2f} V')
        print(f'J @ -2 V = {abs(J[bias.index(-1.99)])*1000:.2e} mA/cm²\n')
        l.append(bias[Jabs.index(min(Jabs))])
        ljsc.append(abs(J[bias.index(-1.99)]))
        
        plt.tick_params(labelsize=23)
        plt.yscale('log')
        #plt.xscale('log')
        plt.xlabel('bias (V)',size=25)
        plt.ylabel('J (A/${cm^2)}$',size=25)
        plt.xlim(-2,2)
        #plt.ylim(5e-13,2e-3)
        plt.grid(True)
        plt.plot(bias,Jabs)
        #plt.plot(Vrev,Jcorr)
        #plt.plot(bias,Jsh)
        plt.title('Donor/C60/LiF/Al',size=25)
        #plt.text(-2.8,1e-7,f'Jd @ -2V = {abs(J[bias.index(-2)]):.2e} A/cm²\nRsh = {Rsh:.2e} Ω/cm²\nRs = {Rs:.2e} Ω/cm²\n',fontsize=15,style='normal')
    matVoc=np.array(l)
    matjsc=np.array(ljsc)
    print(f'Voc = {np.mean(matVoc):.2f} ± {np.std(matVoc):.2f}({max(l):.2f}) V')
    print(f'Jlight @ -2V= {np.mean(matjsc)*1000:.2f} ± {np.std(matjsc)*1000:.2f} mA/cm²')
#输入文件夹及关键字，路径'\'用'/'代替
plt.figure(figsize = (16,9))
filetxt_list=getfile('jv/simulator/20200627','.dat','s6','52')
plotjv(filetxt_list)

filetxt_list=getfile('jv/simulator/20200627','.dat','s7','51')
plotjv(filetxt_list)

'''getfile('jv/ps-20200701','s2','0.01')
plotjv(filetxt_list)
getfile('jv/ps-20200701','s3','0.01')
plotjv(filetxt_list)
filetxt_list=[]'''

plt.show()