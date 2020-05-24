## Prediction/Regression Evaluation Indicators



Assume we have:

Prediction $$\hat{y} = {\hat{y}_1,\hat{y}_2, \dots \hat{y}_n }$$

Actual  $$y = {y_1,y_2, \dots y_n }$$



### Mean Square Error (MSE)



$$MSE = \frac{1}{n}\sum^n_{i=1}(\hat{y}_i - y_i)^2 $$

~~~Python
# import numpy as np
def mse(y_true, y_pred):
    return np.mean(np.sum((y_true - y_pred).dot(y_true - y_pred)))

#from sklearn import metrics
#metrics.mean_squared_error(y_true, y_pred)
~~~



### Root Mean Square Error (RMSE)



$$RMSE = \sqrt{\frac{1}{n}\sum^n_{i=1}(\hat{y}_i - y_i)^2} $$

~~~Python
# import numpy as np
def mse(y_true, y_pred):
    return np.sqrt(np.mean(np.sum((y_true - y_pred).dot(y_true - y_pred))))

#from sklearn import metrics
#np.sqrt(metrics.mean_squared_error(y_true, y_pred))
~~~



### Mean Absolute Percentage Error (MAPE)



~~~Python
# import numpy as np
def mape(y_true, y_pred):
    return np.mean(np.abs((y_pred - y_true) / y_true)) * 100
~~~



### Symmetric Mean Absolute Percentage Error (SMAPE)

$$ SMAPE = \frac{100\%}{n}\sum^n_{i=1} \frac{|\hat{y}_i- y_i|}{(|\hat{y}_i|+ |y_i|)^2} $$

~~~Python
# import numpy as np
def smape(y_true, y_pred):
    return 2.0 * np.mean(np.abs(y_pred - y_true) / (np.abs(y_pred) + np.abs(y_true))) * 100
~~~





### The sum of squares due to error (SEE)



### $$R^2$$ Coefficient of determination





### Degree-of-freedom adjusted $$R^2$$



###  Explained Variance Score



### Median absolute error



### Mean squared logarithmic error







### Confusion Matrix 

- Accuracy

  

- Precision

  

- Recall

  

- F1 (H - mean)



###  Receiver Operating Characteristic Curve (ROC) 



### Area Under Curve (AUC)





