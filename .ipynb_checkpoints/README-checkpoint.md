## Python in Finance

Applying Python in solving practical issues in finance.  Materials in this repo are designed for students taking my course 《Python在金融中的应用》以及《基于机器学习的投资分析》 浙江工商大学 金融学院. 

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

0. First Talk: What you need to prepare - Very important ([slide](First_Talk.md))

`Basic Session` 

1. Numpy and matrix operations ([slide and code](/BasicSession/numpy_learn.ipynb))
2. Matplotlib and image processing ([slide and code](/BasicSession/matplotlib_learn.ipynb))
3. Pandas and data processing ([slide and code](/BasicSession/pandas_learn.ipynb))



该部分需要比较熟练的掌握，首先大家要搞懂讲义上的命令，另外要了解以下的重点。


1. 了解Numpy的基础操作，它比python中自带的list或者dict要快很多。 numpy类似于list，和Matlab比较相似。 需要了解Numpy的算数运算、比较运算、矩阵运算。Numpy中的索引是非常重要的部分，需要清楚的了解二维列表的索引，尤其是行和列的区别。
2. Pandas首先需要了解，一种类似于一维数组的对象Series， 它由一组数据（各种NumPy数据类型）以及一组与之相关的数据标签（即索引）组成，然后是表格型的数据结构。每列可以是不同的值类型（数值，字符串，布尔值等）。可以被看做由Series组成的大字典， DataFrame。 熟悉处理多种数据类型和转换，知道如何从如xls，csv，以及MySQL中导入DataFrame。 了解如何选择数据、对数据进行赋值、删除、合并、筛选、分组、聚合等等。了解如何做可视化数据，独立于matplotlib进行数据展示，简单作图。
3. Matplotlib是一个 Python 的 2D绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形。可以绘制线图、散点图、等高线图、条形图、柱状图、3D 图形、甚至是图形动画等等。需要了解什么是Axis，如何使用subplot, scatter, hist, plot, bar, stackplot等作图基本命令，并且了解如何使用colorbar, legend, set_title等做标注的命令。

`Data Session`

1. Data base (SQL and NoSQL):  [MySQL](https://www.mysql.com/) and [MongoDB](https://www.mongodb.com/)  (You can use [MariaDB](https://mariadb.org/) as an alternative of MySQL)  ([slide and code](/DataSession/database_learn.ipynb))
2. API and Data Retrieval:  [Tushare](http://www.tushare.org ) ([slide and code](/DataSession/API_and_Data_Retrieval.ipynb))

主要是了解如何通过API取得外部数据，并将数据库用于数据的存储和处理。同时需要能够结合之前所学基本操作，了解如何通过API，数据库等进行数据的操作和分析。

1. 了解API是什么，知道API运作的基本原理，知道如何通过API可以快速读取在服务器端的数据，了解JSON格式和Requests命令的用途。通过讲义上面的例子了解如何使用API取得数据。特别需要了解Tushare数据服务，知道如何通过该API，获得各种股票数据，如何结合之前所学寻找特定的数据并进行简单的处理。
2. 了解数据库的用途，什么是数据库，SQL是什么样的数据库。能够在自己本机上安装并且运行MySQL或者是MariaDB数据库，有条件的应该将数据库安装在云端。了解如何将数据写入以及读出数据库，基本的sql代码的撰写，尤其是通过pandas的相关命令完成数据的读和写操作。了解如何使用Navicat这个图形化操作工具。MongoDB不做要求，但是希望能多加了解和使用。数据库的操作可以使处理数据，尤其是大型数据的能力显著增强。

`Program Session`

1. Web Crawler I:  Financial News from [雪球](https://xueqiu.com/)   ([slide and code](/ProgramSession/spider01_learn.ipynb))
2. Web Crawler II:  Daily stock price from [网易财经](https://money.163.com/)  ([slide and code](/ProgramSession/spider02_learn.ipynb))
3. Time series basic: Return, mean, variance, correlation of stock prices, visualization, etc ([slide and code](/ProgramSession/time_series_learn.ipynb))
4. Nature Language Processing:  Financial sentiment analysis ([slide and code](/ProgramSession/nlp_learn.ipynb))
5. Quantative analysis: Sharpe ratio, Information ratio, Maxmium Drawnback, etc ([slide and code](/ProgramSession/quant_learn.ipynb))
6. Statistics Tests: T test, Chi Square test, OLS ([slide and code](/ProgramSession/statistics_learn.ipynb))

该部分相对内容更多，需要大家认真复习。爬虫是Python的重要应用，可以得到各种各类的数据，时间序列分析是金融数据处理的基础知识，自然语言处理是一项目前比较热门的技术，量化分析是目前私募公募基金、信托等多种投资和资管机构常用的技术，统计检验是今后学习计量经济学的基础。

1. 爬虫是什么，python爬虫的主要架构。 简单了解什么是HTML，以及CSS。学会使用requests进行网页请求，其中需要掌握get的方法。了解如何设置headers中的相关部分。了解cookie的含义，并知道如何取出cookie内容。掌握当网页含有JSON格式的信息时候，如何快捷的将数据输出。了解如何使用BeautifulSoup来进行网页的解析，了解BeautifulSoup在处理html标签时候的特点及能力。了解如何结合正则表达式取得网页中的信息，最后格式化的输出。知道xpath的基本操作方法。两个单元的爬虫，介绍的内容比较初步，当网页比较复杂的时候，需要运用动态网页的自动化测试工具，如selenium实现浏览器的驱动，还有如何应付服务器的反爬，以及网页验证等，需要大家进一步的学习和实践。 
2. 时间序列可以用于趋势分析与预测，它主要是研究自身的变化规律的，并不仅仅是关于时间的回归。能做时间序列的软件很多，SAS、R、SPSS、Eviews、matlab等等。 要求大家掌握移动平均，指数移动平均的做法，可以绘制K线图，并进行简单分析。掌握如何计算股票序列的收益情况，波动率，以及夏普比例的计算。了解什么是相关性，如何通过函数进行相关性的计算，如何展示相关系数矩阵。希望大家能够熟练应用Numpy和Pandas两个包进行时间序列的处理、分析、可视化的展示。
3. 金融市场中，对传统的数字信息的分析已经不能满足学者、量化研究者的需要，借助于机器学习特别是自然语言处理相关工具、算法的发展， 对文本信息的系统结构化解读是当今学界与业界的一大热点。要求大家了解金融文本处理的应用场景和典型方案。知道如何使用LAC和Jieba进行中文分词，词性标准等功能。了解什么是关键词的提取，两种关键词提取算法的大概意义，并可以根据jieba中提供的相应的函数包进行关键词提取。了解什么是舆情分析，如何使用SnowNLP的函数包进行中文文本分析，并实现舆情的打分。学会结合爬虫对于新闻进行舆情分析打分。 
4. 量化投资部分的内容需要大家初步了解什么是量化投资，以及它的优势。了解量化投资的思想和策略，并借助Python 语言进行实现。了解数据获取，策略回测，发送交易信号的全过程。了解如何通过Tushare去获取相应的股票信息，并实现夏普比例，信息比例的计算，了解什么是最大回撤，如何计算最大回撤。知道如何去查找发现交易策略（建议了解优矿、聚宽、米筐、同花顺、京东量化，万矿、掘金量化）以及因子库，大致了解量化交易策略，建议大家可以了解海龟交易策略。 
5. 统计检验是统计学中的重中之重，在实际中有着广泛的应用。要求假设检验中的t检验，及其在实际中的应用。如何通过试验数据和实际数据来进行单样本t检验和独立双样本t检验，大致了解卡方检验的意义及其代码实现。了解回归算法，特别是通过最小二乘进行参数估计的回归，如何用代码来进行参数估计，以及如何使用scipy函数包进行参数估计。基本了解如何使用pandas和seaborn进行回归分析及结果展示。


#### Part II

`Case Study`

1. Bond Pricing

2. Porfolio Management ([slide and code](https://github.com/xinihe/jrxy_portfolio_management))


`ML Session`

0. Introducation ([slide and code](/AdvancedSession/MachineLearningBasic.md))

1. Basic
   1. Learning Regression (LASSO and Ridge)
   2. Logistic Regression
   
2. Unsupervised Learning:
   1. K-means Clustering -- feature detecting ([slide and code](/AdvancedSession/k-means.ipynb))
   2. Genetic Algorithm -- early warning
   3. Self-Organizing Map 
   
3. Supervised Learning:
   1. Naive Bayes Classifier  ([slide and code](/MLSession/bayes_learn.ipynb))
   2. Decision Tree (Find the best indicator) ([slide and code](/AdvancedSession/decision_tree.ipynb))
   3. K-nearest neighbor 


4. Reinforcement Learning:
   1. Multi-Arm Bandit (portfolio selection)
   2. Q-learning
   
5. Nature Language Processing:
   1. Financial sentiment analysis



#### Exam （Independent Work）

1. exam 2020 ([link](/Exam/python_finance_2020.md))
2. exam 2021 ([link](/Exam/python_finance_2021.ipynb))

