# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 23:50:16 2020
@author: NI HE
"""

# load data from multiple data source
import tushare as ts
import numpy as np
import pandas as pd
from datetime import datetime
from iexfinance.stocks import get_historical_data
import matplotlib.pyplot as plt
from scipy import stats


tushare_token = '1c8b06446534ae510c8c68e38fc248b99f89ac3814cb55645ae2be72'  # 请在 tushare.pro 网站注册并且告知学生身份，可以取得你的token
pro = ts.pro_api(tushare_token)

def collect_stock_data(code, start_date, end_date, is_chinese = 1):
    my_token = 'pk_20fe28167fc34f56adba1d341120cb0e' 
    if is_chinese == 1:
        try:
            stk_data = ts.get_hist_data(code,start = ''.join(start_date.split('-')), end = ''.join(end_date.split('-')))
            return stk_data
        except:
            print('Stock '+code+' could not collect from Tushare.')
    else:
        # Foreign stock information from IEX finance
        start = datetime(int(start_date.split('-')[0]), int(start_date.split('-')[1]), int(start_date.split('-')[2]))
        end   = datetime(int(end_date.split('-')[0]), int(end_date.split('-')[1]), int(end_date.split('-')[2]))

        try:
            stk_data_dict = get_historical_data(code, start, end, token=my_token)
            # convert to pd
            data = {}
            for  key, value in stk_data_dict.items():
                data[key] = list(value.values())
            stk_data = pd.DataFrame.from_dict(data, orient='index', columns=['open', 'high', 'low', 'close','volume'])
            return stk_data
        except:
            print('Could not get the data from IEX finance')
        
    


def collect_stock_data_pro(code, start_date, end_date):
    try:
        stk_data = pro.daily(ts_code = code, start_date = ''.join(start_date.split('-')), end_date = ''.join(end_date.split('-')))
        
        return stk_data
    except:
        print('Stock '+code+' could not collect from Tushare Pro')
    

def tick2ret(price):
    return 100 * (price - price.shift(1)).div(price.shift(1))[1:]

# randomly choose n stocks, return their codes
def random_pick_stocks_code(n):
    industry = ts.get_industry_classified()
    ind = [x[0] for x in list(np.random.randint(low = 0, high = len(industry), size = (n, 1)))]
    return industry.iloc[ind]['code'] 

def random_pick_stocks_code_pro(n): 
    stock_list = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    ind = [x[0] for x in list(np.random.randint(low = 0, high = len(stock_list), size = (n, 1)))]
    return list(stock_list.iloc[ind]['ts_code'])



def bus_date_interval(start_date, end_date):
    ds = [int(d) for d in start_date.split('-')]
    de = [int(d) for d in end_date.split('-')]
    return np.round(250/365 * (datetime(de[0],de[1],de[2]) - datetime(ds[0],ds[1],ds[2])).days)
    



def random_stocks_return(start_date, end_date, n):
    ret_list = pd.DataFrame()
    for c in random_pick_stocks_code(n):
        st = collect_stock_data(c,start_date,end_date)    
        st_ret = tick2ret(st['close']).to_frame(name = c) 
        ret_list = pd.concat([ret_list, st_ret], axis = 1 ,join = 'outer', ignore_index = False, sort = False)
    ret_list.dropna(axis = 0, how = 'any', inplace = True)
    return ret_list

def random_stocks_return_pro(start_date, end_date, n):
    ret_list = pd.DataFrame()
    codes = [i for i in random_pick_stocks_code_pro(n)]
    for c in codes:
        st = collect_stock_data_pro(c,start_date,end_date)
        st.set_index(["trade_date"], inplace=True)
        st_ret = tick2ret(st['close']).to_frame(name = c) 
        ret_list = pd.concat([ret_list, st_ret], axis = 1 ,join = 'outer', ignore_index = False, sort = False)
    ret_list.dropna(axis = 0, how = 'any', inplace = True)
    return ret_list, codes



def picked_stocks_return_pro(start_date, end_date, codes):
    ret_list = pd.DataFrame()
    for c in codes:
        st = collect_stock_data_pro(c,start_date,end_date)
        # if the stock has less than 80% of available data, we would give up that stock 
        if len(st.dropna(axis = 0, how = 'any', inplace = False)) < 0.8 * bus_date_interval(start_date, end_date):
            continue
        st.set_index(["trade_date"], inplace=True)
        st_ret = tick2ret(st['close']).to_frame(name = c) 
        ret_list = pd.concat([ret_list, st_ret], axis = 1 ,join = 'outer', ignore_index = False, sort = False)
    ret_list.dropna(axis = 0, how = 'any', inplace = True)
    return ret_list



def merge_with_cis300(ret_list):
    cis300 = pro.index_daily(ts_code='000300.SH')
    cis300.set_index(['trade_date'], inplace=True)
    st_ret = tick2ret(cis300['close']).to_frame(name = 'cis300') 
    ret_list = pd.concat([ret_list, st_ret], axis = 1 ,join = 'outer', ignore_index = False, sort = False)
    ret_list.dropna(axis = 0, how = 'any', inplace = True)
    return ret_list


def corr_analysis(ret_list):
    ret_cov = np.corrcoef(ret_list.values.T)
    return ret_cov

def multi_corr(ret_list_pair, winlen = 50, N = 100):
    print('Correlation coefficent between '+ret_list_pair.columns.values[0]+' and '+ret_list_pair.columns.values[1]+' is: ' + str(np.round(np.corrcoef(ret_list_pair.T)[0,1], 3)))
    corr_list = []
    for i in range(N):
        start = np.random.randint(len(ret_list_pair) - winlen)
        corr_list.append(np.corrcoef(ret_list_pair.iloc[start:start+winlen,0],ret_list_pair.iloc[start:start+winlen,1])[0,1])        
    print('Average correlation is: '+str(round(np.mean(corr_list),3))+' with std= '+ str(round(np.std(corr_list),3)))  
    # Display
    plt.figure()
    plt.hist(corr_list, bins=20)
    plt.show()  
    print('Kurtosis is: '+ str(round(stats.kurtosis(corr_list),3)) + '; Shewness is ' + str(round(stats.skew(corr_list),3)))


    
def main():   
    # specify start/end dates
    start_date='2017-07-01'
    end_date='2020-3-30'
    n = 5
    ret_list, name = random_stocks_return_pro(start_date, end_date, n)
    
    multi_corr(ret_list.iloc[:,0:2])



#if __name__ == '__main__':
#    main()