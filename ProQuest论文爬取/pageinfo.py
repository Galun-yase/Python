# -*- coding: utf-8 -*-
import requests
import re
import pandas as pd
import time
 
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
     
def parsePage(ilt, html):
    try:
        subject=re.findall(r'<font>(.*?)</font>.?<span>;</span>',html,re.S|re.M)
        other=re.findall(r'<div class="display_record_indexing_data">(.*?)</div>',html,re.S|re.M)

        
        ilt.append([subject,other[1:]])            
    except:
        print("")
 
def printGoodsList(ilt):
    for g in ilt:
        print(g)
 
infoList = []

data=pd.read_excel(r'C:\Users\asusl\Desktop\urllist.xlsx')
urllist1=[]
data.applymap(lambda x:urllist1.append(x))
urllist2=[]
for i in urllist1:
    if(i in urllist2):
        continue
    else:
        urllist2.append(i)        
#urllist=['2838BB30E76CC32276EFD5E1B025962E','D72352741A19C5B0671323BB4A6DCC2A']
time_start=time.time()
for i in urllist2[10000:21000]:
    try:
        url = 'http://www.pqdtcn.com/thesisDetails/'+str(i)
        html = getHTMLText(url)   
        parsePage(infoList, html)
    except OSError:
        pass
    continue
time_end=time.time()
print('totally cost',(time_end-time_start)/60)
df = pd.DataFrame(infoList)
df.to_excel(r'C:\Users\asusl\Desktop\ProQuest.xlsx',index=False)

