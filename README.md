## Python in Finance

Applying Python in solving practical issues in finance.  Materials in this repo are designed for students taking my course 《Python在金融中的应用》以及《基于机器学习的投资分析》. 

If you have any question, I would be approachable by email ni.he@qq.com. 

### Software 

+ Python 3.* 

+ [Anaconda](https://www.anaconda.com/) (Spyder)    You can download the latest official version from [here](https://www.anaconda.com/), and if you experienced a bad connection, a mirror site maintained by Tsinghua is available [here](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/).  Tutorial in Chinese is available [here](https://www.jianshu.com/p/62f155eb6ac5). 

  *You could surely use other IDE for programming*

### Data source
+ Tushare  (http://www.tushare.org or https://tushare.pro/)
+ IEX Finance  (https://pypi.org/project/iexfinance/)



### Tentative Curriculum

0. First Talk: What you need to prepare ([slide](First_Talk.md))

`Preliminary Session` 

1. Numpy and matrix operations ([slide and code](/BasicSession/numpy_learn.ipynb))
2. Matplotlib and image processing ([slide and code](/BasicSession/matplotlib_learn.ipynb))
3. Pandas and data processing ([slide and code](/BasicSession/pandas_learn.ipynb))

`Data Session`

1. Data base (SQL and NoSQL):  [MySQL](https://www.mysql.com/) and [MongoDB](https://www.mongodb.com/)  (You can use [MariaDB](https://mariadb.org/) as an alternative of MySQL)  ([slide and code](/BasicSession/database_learn.ipynb))
2. API and Data Retrieval:  [Tushare](http://www.tushare.org ) ([slide and code](/DataSession/API_and_Data_Retrieval.ipynb))

`Program Session`

1. Web Crawler I:  Financial News from [雪球](https://xueqiu.com/)   ([slide and code](/BasicSession/news_learn.ipynb))
2. Web Crawler II:  Daily stock price from [网易财经](https://money.163.com/)  ([slide and code](/BasicSession/stockprice_learn.ipynb))
3. Time series basic: Return, mean, variance, correlation of stock prices, visualization, candle chart, etc ([slide and code](/BasicSession/time_series_learn.ipynb))
4. Statistics Tests ([slide and code](/BasicSession/statistics_learn.ipynb))
5. Nature Language Processing:  Financial sentiment analysis ([slide and code](/BasicSession/nlp_learn.ipynb))

`ML Session`

1. Basic
   1. Learning Regression
   2. Logistic Regression
    

2. Unsupervised Learning:
   1. K-means Clustering in Fund feature detecting
   2. Genetic Algorithm for early warning
   
 
3. Supervised Learning:
   1. Naive Bayes Classifier
   2. Decision Tree
   3. K-nearest neighbor


4. Reinforcement Learning:
   1. Multi-arm Bandit in portfolio selection
   2. Q-learning
   
   
5. Nature Language Processing:
   1. Financial sentiment analysis