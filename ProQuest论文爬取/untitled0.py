# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:19:21 2019

@author: asusl
"""

import pandas as pd

data=pd.read_excel(r'C:\Users\asusl\Desktop\ProQuest -All.xlsx')
dd=pd.DataFrame(data[2])
otherlist=[]
for i in dd[2]:
    olist=[]
    aa=i.split("',")
    for j in aa:
        olist.append(j)
    otherlist.append(olist)
a=pd.DataFrame(otherlist)
a.to_excel(r'C:\Users\asusl\Desktop\1.xlsx')