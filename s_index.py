# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:59:29 2020

@author: Administrator
"""
import data_process
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts

import simple_ols

start_date = '2018-06-01'
end_date = '2020-04-15'
n = 1
ret_list, code = data_process.random_stocks_return_pro(start_date, end_date, n)


cis300 = data_process.pro.index_daily(ts_code='000300.SH')
cis300.set_index(['trade_date'], inplace=True)
st_ret = data_process.tick2ret(cis300['close']).to_frame(name = 'cis300') 

ret_list = pd.concat([ret_list, st_ret], axis = 1 ,join = 'outer', ignore_index = False, sort = False)
ret_list.dropna(axis = 0, how = 'any', inplace = True)


reg = simple_ols.simple_ols(ret_list.iloc[:,0].values, ret_list.iloc[:,1].values)
plt.figure()
plt.scatter(ret_list.iloc[:,1].values, ret_list.iloc[:,0].values,alpha = 0.4)
i = np.linspace(min(ret_list.iloc[:,1].values), max(ret_list.iloc[:,1].values),100)
plt.plot(i, reg.b[0]+reg.b[1]*i, c = 'black')
plt.xlabel('CIS 300')
plt.ylabel(code[0])
plt.title( 'Beta is '+str(np.round(reg.b[1],2))+' and Alpha is '+str(np.round(reg.b[0],2)))
plt.grid()

beta_corr = np.cov(ret_list.iloc[:,0].values, ret_list.iloc[:,1].values)[0,1] / np.var(ret_list.iloc[:,1].values)

print(' Beta by regression is {}, \n \
Beta by covariance is {}.'.format(reg.b[1], beta_corr))