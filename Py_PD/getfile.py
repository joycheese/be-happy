# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 23:30:15 2020

@author: yang30
"""


import os

#指定data文件所在路径文件夹，默认母目录为C:\Users\yang30\Desktop\data\
def getfile(folder, file_format, keyword1, keyword2):
    os.chdir(('C:/Users/yang30/Desktop/data/'+folder).replace('/','\\'))
    file_chdir=os.getcwd()

    #将所有符合条件的文件列入filetxt_list
    filetxt_list=[]
    for root,dirs,files in os.walk(file_chdir):
        for file in files:
            if file_format in os.path.splitext(file)[1] and keyword1 in os.path.splitext(file)[0] and keyword2 in os.path.splitext(file)[0]:
                filetxt_list.append(file)
    return filetxt_list
