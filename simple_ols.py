# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:13:47 2020

@author: Ni He
"""
from scipy import c_
import numpy as np
import scipy

class simple_ols():
    
    def __init__(self,y,x):
        
        self.y = y
        self.x = scipy.c_[np.ones(x.shape[0]),x]
        self.estimate()
        
    def estimate(self):
        
         # estimating coefficients, and basic stats
        self.inv_xx = scipy.linalg.inv(np.dot(self.x.T,self.x))
        # b = inv(x.T * x)*x*y
        self.b = np.dot(self.inv_xx, np.dot(self.x.T,self.y))                 # estimate coefficients

        self.nobs = self.y.shape[0]                     # number of observations
        self.ncoef = self.x.shape[1]                    # number of coef.
        self.df_e = self.nobs - self.ncoef              # degrees of freedom, error 
        self.df_r = self.ncoef - 1                      # degrees of freedom, regression 

        self.e = self.y - np.dot(self.x,self.b)            # residuals
        self.sse = np.dot(self.e,self.e)/self.df_e         # SSE
        self.se = np.sqrt(np.diagonal(self.sse*self.inv_xx))  # coef. standard errors
        self.t = self.b / self.se                       # coef. t-statistics
        self.p = (1-scipy.stats.t.cdf(abs(self.t), self.df_e)) * 2    # coef. p-values

        self.R2 = 1 - self.e.var()/self.y.var()         # model R-squared
        self.R2adj = 1-(1-self.R2)*((self.nobs-1)/(self.nobs-self.ncoef))   # adjusted R-square

        self.F = (self.R2/self.df_r) / ((1-self.R2)/self.df_e)  # model F-statistic
        self.Fpv = 1-scipy.stats.f.cdf(self.F, self.df_r, self.df_e)  # F-statistic p-value

    def dw(self):
        """
        Calculates the Durbin-Waston statistic
        
        where there is a (linear) correlation between the error term for one observation and the next.
        dw takes on values between 0 and 4. A value of dw = 2 means there is no autocorrelation. 
        A value substantially below 2 (and especially a value less than 1) means that the data is 
        positively autocorrelated, i.e. on average a data element is close to the subsequent data 
        element. A value of dw substantially above 2 means that the data is negatively 
        autocorrelated, i.e. on average a data element is far from the subsequent data element.
        """
        de = np.diff(self.e,1)
        dw = np.dot(de,de) / np.dot(self.e,self.e);

        return dw

    def omni(self):
        """
        Omnibus test for normality
        """
        
        return scipy.stats.normaltest(self.e) 
    
#    def check_normality(testData):
#    #20<样本数<50用normal test算法检验正态分布性
#    if 20<len(testData) <50:
#       p_value= stats.normaltest(testData)[1]
#       if p_value<0.05:
#           print"use normaltest"
#           print "data are not normal distributed"
#           return  False
#       else:
#           print"use normaltest"
#           print "data are normal distributed"
#           return True
#     
#    #样本数小于50用Shapiro-Wilk算法检验正态分布性
#    if len(testData) <50:
#       p_value= stats.shapiro(testData)[1]
#       if p_value<0.05:
#           print "use shapiro:"
#           print "data are not normal distributed"
#           return  False
#       else:
#           print "use shapiro:"
#           print "data are normal distributed"
#           return True
#       
#    if 300>=len(testData) >=50:
#       p_value= lillifors(testData)[1]
#       if p_value<0.05:
#           print "use lillifors:"
#           print "data are not normal distributed"
#           return  False
#       else:
#           print "use lillifors:"
#           print "data are normal distributed"
#           return True
#     
#    if len(testData) >300: 
#       p_value= stats.kstest(testData,'norm')[1]
#       if p_value<0.05:
#           print "use kstest:"
#           print "data are not normal distributed"
#           return  False
#       else:
#           print "use kstest:"
#           print "data are normal distributed"
#           return True
    
    def JB(self):
        """
        Calculate residual skewness, kurtosis, and do the JB test for normality
        """

        # Calculate residual skewness and kurtosis
        skew = scipy.stats.skew(self.e) 
        kurtosis = 3 + scipy.stats.kurtosis(self.e) 
        
        # Calculate the Jarque-Bera test for normality
        JB = (self.nobs/6) * (np.square(skew) + (1/4)*np.square(kurtosis-3))
        JBpv = 1-scipy.stats.chi2.cdf(JB,2);

        return JB, JBpv, skew, kurtosis

    def ll(self):
        """
        Calculate model log-likelihood and two information criteria
        """
        
        # Model log-likelihood, AIC, and BIC criterion values 
        ll = -(self.nobs*1/2)*(1+np.log(2*np.pi)) - (self.nobs/2)*np.log(np.dot(self.e,self.e)/self.nobs)
        aic = -2*ll/self.nobs + (2*self.ncoef/self.nobs)
        bic = -2*ll/self.nobs + (self.ncoef*np.log(self.nobs))/self.nobs

        return ll, aic, bic
        
        
    