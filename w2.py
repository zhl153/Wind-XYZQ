# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 13:37:22 2018

@author: lzhzhl
"""

from WindPy import w

def pro(year,zs):    
    proportion=[0,0,0] 
    for i in year: 
        n=0      
        for j in i.Data[0]:              
            if j in zs[0].Data[0]:
                proportion[0]+=i.Data[1][n]
            elif j in zs[1].Data[0]:
                proportion[1]+=i.Data[1][n]
            elif j in zs[2].Data[0]:
                proportion[2]+=i.Data[1][n]
            n+=1     
    proportion=[x/(100*len(year)) for x in proportion]
    return proportion

def get_data(years_date,stocks):
    zs=[]
    data_code1="date="+years_date+";windcode=000016.SH;field=wind_code"
    data_code2="date="+years_date+";windcode=000300.SH;field=wind_code"
    data_code3="date="+years_date+";windcode=000905.SH;field=wind_code"
    zs.append(w.wset("sectorconstituent",data_code1))
    zs.append(w.wset("sectorconstituent",data_code2))
    zs.append(w.wset("sectorconstituent",data_code3))
    
    year_stocks=[]
    for stock in stocks:
        stock_num="rptdate="+years_date+";windcode="+stock+";field=stock_code,proportiontototalstockinvestments"
        year_stocks.append(w.wset("allstockhelddetaill3",stock_num))
    return year_stocks,zs

w.start()
stat=[]

###
y="2014-12-31"
s=["000414.OF","000585.OF","000667.OF","000672.OF","000753.OF","000754.OF"]
ys,zs=get_data(y,s)
stat.append(pro(ys,zs))

###
y="2015-06-30"
s=["000414.OF","000585.OF","000667.OF","000672.OF","000753.OF","000754.OF","000844.OF","000992.OF","001059.OF","519062.OF"]
ys,zs=get_data(y,s)
stat.append(pro(ys,zs))

###
y="2015-12-31"
s=["000414.OF","000585.OF","000667.OF","000672.OF","000753.OF","000754.OF","000844.OF","000992.OF","001059.OF","519062.OF","001641.OF","001791.OF"]
ys,zs=get_data(y,s)
stat.append(pro(ys,zs))

###
y="2016-06-30"
s=["000414.OF","000585.OF","000667.OF","000672.OF","000753.OF","000754.OF","000844.OF","000992.OF","001059.OF","519062.OF","001641.OF","001791.OF","001896.OF","002224.OF"]
ys,zs=get_data(y,s)
stat.append(pro(ys,zs))

###
y="2016-12-31"
s=["000414.OF","000585.OF","000667.OF","000672.OF","000753.OF","000754.OF","000844.OF","000992.OF","001059.OF","519062.OF","001641.OF","001791.OF","001896.OF","002224.OF","002527.OF","002655.OF","002804.OF"]
ys,zs=get_data(y,s)
stat.append(pro(ys,zs))

###
y="2017-06-30"
s=["000414.OF","000585.OF","000667.OF","000672.OF","000753.OF","000754.OF","000844.OF","000992.OF","001059.OF","519062.OF","001641.OF","001791.OF","001896.OF","002224.OF","002527.OF","002655.OF","002804.OF"]
ys,zs=get_data(y,s)
stat.append(pro(ys,zs))

###
y="2017-12-31"
s=["000414.OF","000585.OF","000667.OF","000672.OF","000753.OF","000754.OF","000844.OF","000992.OF","001059.OF","519062.OF","001641.OF","001791.OF","001896.OF","002224.OF","002527.OF","002804.OF"]
ys,zs=get_data(y,s)
stat.append(pro(ys,zs))

print(stat)

shangzheng=[stat[0][0],stat[1][0],stat[2][0],stat[3][0],stat[4][0],stat[5][0],stat[6][0]]
hushen=[stat[0][1],stat[1][1],stat[2][1],stat[3][1],stat[4][1],stat[5][1],stat[6][1]]
zhongzheng=[stat[0][2],stat[1][2],stat[2][2],stat[3][2],stat[4][2],stat[5][2],stat[6][2]]
t=[1,2,3,4,5,6,7]
'''
###
import matplotlib.pyplot as plt
from pylab import * 
mpl.rcParams['font.sans-serif'] = ['SimHei'] 

plt.bar(t,shangzheng,0.2,label="上证50")
plt.bar([x+0.2 for x in t],hushen,0.2,label="沪深300")
plt.bar([x+0.4 for x in t],zhongzheng,0.2,label="中证500")
plt.xticks([x+0.3 for x in t],('2014-12','2015-06','2015-12','2016-06','2016-12','2017-06','2017-12'))
plt.legend(loc='best')
plt.show()

###
'''
import pandas as pd
import seaborn as sns

years=['2014-12','2015-06','2015-12','2016-06','2016-12','2017-06','2017-12']
ty=['上证50','沪深300','中证500']
stat_pd=[]

n=0
for i in stat:    
    y=years[n]
    m=0
    for j in i:        
        stat_pd.append([y,ty[m],j])
        m+=1
    n+=1
    
stat_sns=pd.DataFrame(data=stat_pd,columns=['年度','类型','占比'])
sns.set(context='notebook',style='ticks')
sns.set_style({"font.sans-serif":['simhei','Droid Sans Fallback']})
plot=sns.catplot(x='年度',y='占比',hue='类型',data=stat_sns,kind='bar',palette='Set1')
'''      
'''





