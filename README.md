## Python in Finance

Applying Python in solving practical issues in finance.  Materials in this repo are designed for students taking my course 《Python在金融中的应用》以及《基于机器学习的投资分析》. 

If you have any query or would like to contribute, I would be very happy to hear from you by email ni.he@qq.com. 

### Software 

+ Python 3.* 

+ [Anaconda](https://www.anaconda.com/) (Spyder)    You can download the latest official version from [here](https://www.anaconda.com/), and if you experienced a bad connection, a mirror site maintained by Tsinghua is available [here](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/).  Tutorial in Chinese is available [here](https://www.jianshu.com/p/62f155eb6ac5). 

  *You could surely use other IDE for programming*

### Data source
+ Tushare  (http://www.tushare.org or https://tushare.pro/)
+ IEX Finance  (https://pypi.org/project/iexfinance/)



### Tentative Curriculum


#### Part I

0. First Talk: What you need to prepare ([slide](First_Talk.md))

`Preliminary Session` 

1. Numpy and matrix operations ([slide and code](/BasicSession/numpy_learn.ipynb))
2. Matplotlib and image processing ([slide and code](/BasicSession/matplotlib_learn.ipynb))
3. Pandas and data processing ([slide and code](/BasicSession/pandas_learn.ipynb))

`Data Session`

1. Data base (SQL and NoSQL):  [MySQL](https://www.mysql.com/) and [MongoDB](https://www.mongodb.com/)  (You can use [MariaDB](https://mariadb.org/) as an alternative of MySQL)  ([slide and code](/DataSession/database_learn.ipynb))
2. API and Data Retrieval:  [Tushare](http://www.tushare.org ) ([slide and code](/DataSession/API_and_Data_Retrieval.ipynb))

`Program Session`

1. Web Crawler I:  Financial News from [雪球](https://xueqiu.com/)   ([slide and code](/ProgramSession/spider01_learn.ipynb))
2. Web Crawler II:  Daily stock price from [网易财经](https://money.163.com/)  ([slide and code](/ProgramSession/spider02_learn.ipynb))
3. Time series basic: Return, mean, variance, correlation of stock prices, visualization, candle chart, etc ([slide and code](/ProgramSession/time_series_learn.ipynb))
4. Statistics Tests ([slide and code](/ProgramSession/statistics_learn.ipynb))
5. Nature Language Processing:  Financial sentiment analysis ([slide and code](/ProgramSession/nlp_learn.ipynb))


#### Part II

`Case Study`

1. Bond Pricing

2. Porfolio Management


`ML Session`

1. Basic
   1. Learning Regression
   2. Logistic Regression
    

2. Unsupervised Learning:
   1. K-means Clustering (Fund feature detecting)
   2. Genetic Algorithm  (early warning)
   3. Self-Organizing Map ()
   
 
3. Supervised Learning:
   1. Naive Bayes Classifier
   2. Decision Tree (Find the best indicator)
   3. K-nearest neighbor


4. Reinforcement Learning:
   1. Multi-Arm Bandit (portfolio selection)
   2. Q-learning
   
   
5. Nature Language Processing:
   1. Financial sentiment analysis