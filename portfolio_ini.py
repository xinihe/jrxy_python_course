# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 02:15:33 2020
@author: Ni He
"""

import data_process
import numpy as np
import matplotlib.pyplot as plt

def get_stock_data(start_date, end_date, num_assets):
    return data_process.random_stocks_return_pro(start_date, end_date, num_assets)
    

def port_stat(ret_list, num_assets, num_ports):

    weights = np.random.random([num_ports,num_assets])
    weights = weights / (np.mat(np.sum(weights, axis = 1)).T* np.ones([1,num_assets]))
    cov_matrix = np.cov(ret_list.T)
    
    risk_matrix = weights * cov_matrix * weights.T
    ports_risks = np.sqrt(np.diag(risk_matrix))
    ports_returns = np.array(weights * np.mat(np.mean(ret_list.values, axis = 0)).T)
    
    return ports_risks, ports_returns, cov_matrix
    
    


start_date='2017-07-01'
end_date='2020-3-30'
num_assets = 3
ret_list = get_stock_data(start_date, end_date, num_assets)


# calculate portfolio with 2 assets
num_ports = 100
n = 2
ports_risks, ports_returns, cov_matrix = port_stat(ret_list.iloc[:,:n], n, num_ports)

plt.figure()
plt.scatter(ports_risks, ports_returns, alpha=0.4)
plt.scatter(np.sqrt(np.diag(cov_matrix)), np.mean(ret_list.iloc[:,:n].values, axis = 0), c = '#FF0000', alpha=0.4)


# calculate portfolio with more than 2 assets

num_ports = 500
n = 3
ports_risks, ports_returns, cov_matrix = port_stat(ret_list.iloc[:,:n], n, num_ports)

plt.figure()
plt.hist(ports_risks, bins = 20)
plt.show()

print('The average risks of components stocks is: ' + str(np.mean(np.sqrt(np.diag(cov_matrix)))))
print('The average risks of portfolios is: ' + str(np.mean(ports_risks)))

plt.figure()
plt.scatter(ports_risks, ports_returns, alpha=0.4)
plt.scatter(np.sqrt(np.diag(cov_matrix)), np.mean(ret_list.iloc[:,:n].values, axis = 0), c = '#FF0000', alpha=0.4 )


## potential of diversification 
#num_ports = 100
#min_risks = []
#for n in range(2,10):
#    ports_risks, ports_returns, cov_matrix = port_stat(ret_list.iloc[:,:n], n, num_ports)
#    min_risks.append(np.min(ports_risks))
#plt.figure()
#plt.plot(min_risks)
#plt.scatter(range(len(min_risks)), min_risks, alpha = 0.9)
    
