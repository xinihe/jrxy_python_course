# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 02:15:33 2020

@author: Ni He
"""

import data_process
import numpy as np
import matplotlib.pyplot as plt


start_date='2017-07-01'
end_date='2020-3-30'
n = 5
ret_list = data_process.random_stocks_return(start_date, end_date, n)


# calculate portfolio risk based on covariance matrix
num_ports = 500
num_assets = 5
weights = np.random.random([num_ports,num_assets])
weights = weights / (np.mat(np.sum(weights, axis = 1)).T* np.ones([1,num_assets]))

cov_matrix = np.cov(ret_list.T)

risk_matrix = weights * cov_matrix * weights.T
ports_risks = np.sqrt(np.diag(risk_matrix))

plt.figure()
plt.hist(ports_risks, bins = 20)
plt.show()

print('The average risks of components stocks is: ' + str(np.mean(np.sqrt(np.diag(cov_matrix)))))
print('The average risks of portfolios is: ' + str(np.mean(ports_risks)))

ports_returns = np.array(weights * np.mat(np.mean(ret_list.values, axis = 0)).T)
plt.figure()
plt.scatter(ports_risks, ports_returns)