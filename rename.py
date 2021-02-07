# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:02:02 2019

@author: qnh12
"""


# -*- coding: utf-8 -*-

import os
### 对图像和标注文件重命名
path = "D:\\develop_workspace\\VisDrone2019-DET-val\\annotations"  #根据自己需要修改，转化完image|转化annotations

filelist = os.listdir(path) #该文件夹下所有的文件（包括文件夹）

count=1

for file in filelist:

    print(file)

for file in filelist:   #遍历所有文件

    Olddir=os.path.join(path,file)   #原来的文件路径

    if os.path.isdir(Olddir):   #如果是文件夹则跳过

        continue

    filename=os.path.splitext(file)[0]   #文件名

    filetype=os.path.splitext(file)[1]   #文件扩展名

    # Newdir=os.path.join(path,str(count).zfill(6)+filetype)  #os.path.join路径拼接，并用字符串函数zfill 以0补全所需位数
    Newdir=os.path.join(path,str(count)+filetype)  #os.path.join路径拼接，并用字符串函数zfill 以0补全所需位数
    os.rename(Olddir,Newdir)#重命名

    count+=1
