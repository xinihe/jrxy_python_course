# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 02:15:33 2020
@author: Ni He
"""

import data_process
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['axes.unicode_minus']=False

def get_stock_data(start_date, end_date, num_assets):
    return data_process.random_stocks_return_pro(start_date, end_date, num_assets)
    

def port_stat(ret_list, num_assets, num_ports, short_sell = 0):

    weights = np.random.random([num_ports,num_assets]) if short_sell == 0 else np.random.randn(num_ports,num_assets)
    weights = weights / (np.mat(np.sum(weights, axis = 1)).T* np.ones([1,num_assets]))
    cov_matrix = np.cov(ret_list.T)
    
    risk_matrix = weights * cov_matrix * weights.T
    ports_risks = np.sqrt(np.diag(risk_matrix))
    ports_risks = ports_risks.reshape(-1,1)
    ports_returns = np.array(weights * np.mat(np.mean(ret_list.values, axis = 0)).T)
    
    return ports_risks, ports_returns, cov_matrix, weights
    



start_date='2017-07-01'
end_date='2020-3-30'
num_assets = 5
# Random stocks from whole market
ret_list, codes = get_stock_data(start_date, end_date, num_assets)
# Known stocks
codes = ['300368.SZ', '000563.SZ', '300168.SZ', '600084.SH', '300204.SZ']
ret_list = data_process.picked_stocks_return_pro(start_date, end_date, codes)

# calculate portfolio with 2 assets
num_ports = 100
n = 2
ports_risks, ports_returns, cov_matrix, weights = port_stat(ret_list.iloc[:,:n], n, num_ports)

plt.figure()
plt.scatter(ports_risks, ports_returns, alpha=0.4)
plt.scatter(np.sqrt(np.diag(cov_matrix)), np.mean(ret_list.iloc[:,:n].values, axis = 0), c = '#FF0000', alpha=0.4)


# calculate portfolio with more than 2 assets

num_ports = 500
n = 3
ports_risks, ports_returns, cov_matrix, weights = port_stat(ret_list.iloc[:,:n], n, num_ports, short_sell = 0)

plt.figure()
plt.scatter(ports_risks, ports_returns, alpha=0.4)
plt.scatter(np.sqrt(np.diag(cov_matrix)), np.mean(ret_list.iloc[:,:n].values, axis = 0), c = '#FF0000', alpha=0.4 )


# Average diversification
plt.figure()
plt.hist(ports_risks, bins = 20)
plt.show()
print('The average risks of components stocks is: ' + str(np.mean(np.sqrt(np.diag(cov_matrix)))))
print('The average risks of portfolios is: ' + str(np.mean(ports_risks)))


# Capital Allocation Line
def sharpe(ports_risks, ports_returns, risk_free_rate):
    return (ports_returns - risk_free_rate) / ports_risks

risk_free_rate = 0.02
ind_max_sharpe = np.argmax(sharpe(ports_risks, ports_returns, risk_free_rate))

plt.figure()
plt.scatter(ports_risks, ports_returns, alpha=0.4)
plt.scatter(np.sqrt(np.diag(cov_matrix)), np.mean(ret_list.iloc[:,:n].values, axis = 0), c = 'darkblue', alpha= 1 )
plt.scatter([0,ports_risks[ind_max_sharpe]], [risk_free_rate, ports_returns[ind_max_sharpe]], alpha=1, c = 'red')
plt.plot(np.array([0,ports_risks[ind_max_sharpe]]),np.array([risk_free_rate, ports_returns[ind_max_sharpe]]), alpha=0.3, c = 'red')


# Complete optimal portfolio

def utility_func(cports_risks, cports_returns, aversion):
    return cports_returns - 0.005 * aversion * cports_risks * cports_risks

aversion = 6
num = 50
cports_risks = np.linspace(0,ports_risks[ind_max_sharpe], num = num) 
cports_returns = np.linspace(risk_free_rate,ports_returns[ind_max_sharpe], num = num)
index_comp_port = np.argmax(utility_func(cports_risks, cports_returns, aversion))

plt.figure()
# opportunity sets
plt.scatter(ports_risks, ports_returns, alpha=0.4)
# original assets
plt.scatter(np.sqrt(np.diag(cov_matrix)), np.mean(ret_list.iloc[:,:n].values, axis = 0), c = 'darkblue', alpha= 1 )
# Risk free asset and max sharpe portfolio
plt.scatter([0,ports_risks[ind_max_sharpe]], [risk_free_rate, ports_returns[ind_max_sharpe]], alpha= 0.5, c = 'red')
# Capital allocation line
plt.plot(np.array([0,ports_risks[ind_max_sharpe]]),np.array([risk_free_rate, ports_returns[ind_max_sharpe]]), alpha= 0.3, c = 'red')
# Complete optimal portfolio
plt.scatter(cports_risks[index_comp_port], cports_returns[index_comp_port], alpha= 1, c = 'darkred')

# Optimal weights

weights_on_risk_free = 1 - index_comp_port / num
weights_on_risky = (index_comp_port / num) * np.array(weights[ind_max_sharpe,:])

optimal_weights = [weights_on_risk_free, weights_on_risky.tolist()[0]]

print('Invest {:.5f}% on risk free assets'.format(100*np.round(weights_on_risk_free,5)))

for i in range(n):
    print('Invest {0}% on Stock {1}'.format(100*np.round(weights_on_risky.tolist()[0][i],5),codes[i]))
    
    
## with short position 
num_ports = 500
n = 3
ports_risks, ports_returns, cov_matrix, weights = port_stat(ret_list.iloc[:,:n], n, num_ports, short_sell = 0)

plt.figure()
plt.scatter(ports_risks, ports_returns,  alpha=0.4)
plt.scatter(np.sqrt(np.diag(cov_matrix)), np.mean(ret_list.iloc[:,:n].values, axis = 0), c = '#FF0000', alpha=0.4 )

ports_risks, ports_returns, cov_matrix, weights = port_stat(ret_list.iloc[:,:n], n, num_ports, short_sell = 1)
plt.scatter(ports_risks, ports_returns, c = 'lime',  alpha=0.4)



## potential of diversification 
#num_ports = 100
#min_risks = []
#for n in range(2,10):
#    ports_risks, ports_returns, cov_matrix = port_stat(ret_list.iloc[:,:n], n, num_ports)
#    min_risks.append(np.min(ports_risks))
#plt.figure()
#plt.plot(min_risks)
#plt.scatter(range(len(min_risks)), min_risks, alpha = 0.9)
    
