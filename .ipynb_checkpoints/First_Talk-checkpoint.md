## 课程要求

本课程的课程内容在[README](README.md)上可以读到，有任何问题或者建议，请联系授课老师。

本课程需要你对以下内容具有初步的了解，由于课堂时间有限，因此希望你能通过课余的时间进行查漏补缺。

1. Anaconda 

    [Anaconda](https://www.anaconda.com)指的是一个开源的Python发行版本，其包含了Python, R等180多个科学包及其依赖项。这是什么意思呢？Python是一门编程语言，使用这门语言的时候，在写代码这件事情之外，还有很多其他的配套工作，比如运行脚本、下载各种需要用到的库、管理环境等。Anaconda就把这些功能全都集成好了，省去很多琐碎的工作。简单来说，Anaconda帮你管理了在使用Python时用到的包和环境。
    
    Anaconda集成了大部分需要用到的Python包，尤其是数据科学类的包，在数据处理方面，你几乎可以在安装后直接进行使用。
    
    利用自带的conda，Anaconda能够对Python包安装、卸载和更新。Python的一大优势即是丰富的第三方的包，比如数据处理的numpy、数据分析的pandas、和我们做深度学习用到的keras，都是我们所说的包。安装和管理这些包是使用Python的日常。Anaconda是一个便利简洁的包管理器。
    
     下载使用：
    如果你嫌官网下载太慢,这里建议大家使用[清华镜像](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)，找到对应的anaconda版本和操作系统即可。
    
    >注意：建议大家下载稳定版本，最新版本可能存在BUG，Anaconda3-5.3.1版本就比较稳定。百度网盘[Anaconda3-5.3.1链接](https://pan.baidu.com/s/1bhV5orBuYGxtrUb8vXQ9Rg)提取码 pq7x

    下载后按提示安装就可以了。

    安装完Anaconda，就相当于安装了Python、命令行工具Anadonda Prompt、集成开发环境Spyder、交互式笔记本IPython和Jupyter Notebook。


2. Github

    Git是什么？

    Git是目前世界上最先进的分布式版本控制系统（没有之一）。分布式相比于集中式的最大区别在于开发者可以提交到本地，每个开发者通过克隆（git clone），在本地机器上拷贝一个完整的Git仓库。

    Git有什么特点？简单来说就是：高端大气上档次！

    那什么是版本控制系统？ 读一下廖雪峰的[博客](https://www.liaoxuefeng.com/wiki/896043488029600/896067008724000)
    
    Github (Git远程仓库)
    >如果你是一枚Coder，但是你不知道Github，那么我觉的你就不是一个菜鸟级别的Coder，因为你压根不是真正Coder，你只是一个Code搬运工。
    
    什么是 Github?
    Github([官网地址](www.github.com))是一个基于git的代码托管平台，付费用户可以建私人仓库，我们一般的免费用户只能使用公共仓库，也就是代码要公开。
    
    今天，GitHub已是这个星球上最流行的开源托管服务。目前已托管431万git项目，不仅越来越多知名开源项目迁入GitHub，近三年流行的开源库往往在GitHub首发。
    注册账户以及创建仓库。 要想使用github第一步当然是注册github账号了， 在其[官网](https://github.com/)进行注册。 之后就可以创建仓库了（免费用户只能建公共仓库），Create a New Repository，填好名称后Create，之后会出现一些仓库的配置信息。
    
    推荐在本课程中使用**Github Desktop**，具体内容可参见其[官网地址](https://desktop.github.com/)。 并可以在官网下载适合你的版本。
    
    下载：百度云盘(链接：https://pan.baidu.com/s/1UBez48hB0FEXDEOMMsaJqw 密码：6fkr)
    
    下面提供一个友好的帮助文档，可以帮助你一步一步注册Github，并安装Desktop，你可以很方便的将你想要的内容从别人的代码仓库里面clone出来，也可以迅速上传你的代码给别人分享。
    
    [GitHub Desktop图文教程](https://www.jianshu.com/p/a6fc842f501d)
    
3. Markdown

    **Markdown**是一种轻量级标记语言。 它允许人们使用易读易写的纯文本格式编写文档，然后转换成有效的XHTML（或者HTML）文档。这种语言吸收了很多在电子邮件中已有的纯文本标记的特性。由于Markdown的轻量化、易读易写特性，并且对于**图片，图表、数学式**都有支持，目前许多网站都广泛使用Markdown来撰写帮助文档或是用于论坛上发表消息。Markdown可以快速转化为演讲PPT、Word产品文档甚至是用非常少量的代码完成最小可用原型。
    
    **编辑器**，我推荐使用[Typora](https://typora.io/)（[一个极简教程](https://zhuanlan.zhihu.com/p/148825412)），它通吃Windows或者MacOS操作系统。如果你使用印象笔记，有道云笔记，发布微信公众号等都用的上。
    
    给大家几个有效的链接：
    - Markdown指南中文版 [访问](https://www.markdown.xyz/)
    - Markdown 入门指南 简书版本 [访问](https://www.jianshu.com/p/1e402922ee32)
    - 各种不同的编辑器 [访问](https://zhuanlan.zhihu.com/p/69210764)


4. Jupyter Notebook or Jupyter Lab

    Jupyter Notebook是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果。——[Jupyter Notebook官方介绍](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)
    
    简而言之，Jupyter Notebook是以网页的形式打开，可以在网页页面中直接编写代码和运行代码，代码的运行结果也会直接在代码块下显示。如在编程过程中需要编写说明文档，可在同一个页面中直接编写，便于作及时的说明和解释。

    Jupyter Notebook中所有交互计算、编写说明文档、数学公式、图片以及其他富媒体形式的输入和输出，都是以文档的形式体现的。这些文档是保存为后缀名为.ipynb的JSON格式文件，不仅便于版本控制，也方便与他人共享。此外，文档还可以导出为：HTML、LaTeX、PDF等格式。
    
    >好消息：在你安装了Anaconda之后，事实上Jupyter Notebook已经被集成了。

    **本课程的所有教案，我都是通过Jupyter Notebook撰写的。**

    **JupyterLab**对于Jupyter Notebook有着完全的支持。JupyterLab是一个交互式的开发环境，是jupyter notebook的下一代产品，集成了更多的功能。
    
    通过使用JupyterLab，能够以灵活，集成和可扩展的方式处理文档和活动：

    - 可以开启终端，用于交互式运行代码，完全支持丰富的输出
    - 支持Markdown，Python，R，LaTeX等任何文本文件
    - 增强notebook功能
    - 更多插件支持
    
    JupyterLab 目前的版本是1.0版本，如果你安装的是早先的Anaconda，你的JupyterLab版本可能过早，建议你可以使用 pip install jupyterlab --upgrade 来完成升级。
    
    **关于启动目录的问题**
    
    如果clone的目录并不是在JupyterLab （或者是Jupyter Notebook）的默认启动目录，每次我们打开JupyterLab时，在弹出的浏览器界面上是系统默认的文件位置（工作路径），那么我们该如何修改JupyterLab默认的工作路径呢？
    
    1. 在cmd中输入命令使Jupyter产生配置文件：Jupyter_notebook_config.py 
    
    > jupyter notebook --generate-config
    
    2. 通过提示的路径找到刚才生成的配置文件
    
    3. 用记事本打开此配置文档，并用搜索（Ctrl+F）找到如下字段：
    
    > #c.NotebookApp.notebook_dir =

    4. 在后面的引号“”中输入想修改为的默认工作路径，删除前面的#，保存文件
    
    5. 如果是Notebook，可以修改Jupyter Notebook的快捷方式，删掉目标中的%USERPROFILE%并在后面添加上刚才设置好的默认工作路径


### 个人推荐

以下的内容是我个人的推荐，相信对你的学习会有用的。


1. Notebook (笔记软件)

    每一个人都应该：

- 尽早确定你自己想要擅长和从事什么领域。

- 长期关注、收集和整理该领域的高质量信息。

- 定期整理这个信息库，以便取用时效率更高。

    有人总结：80%的人可能都死在了第一步，就是做事情的目的都没有想清楚，没想过，也不知道自己要什么。 有19%的人做到了第二步，有渠道获取高质量的信息，而且有好奇心和执行力，能够长期学习。只有1%的人做到了最后一步。
    
    就是这5个漏斗般的环节——确定领域、高质量信息的获取、收集、整理、取用——每一步的效率，决定了人和人之间的差别。
     
     Evernote 的移动端体验是我用过各种笔记软件中最好的，优秀的功能排版，贴心的快捷输入，还有提醒、待办等等功能。剪藏功能非常棒，用来收集资料，整理思路再好不过了。
     [官网链接](https://www.yinxiang.com/?referer=en)
     
     当然也有很多人吐槽Evernote，有人用OneNote，或者Notion。还有人撰文，[在2020，什么工具能取代Evernote/印象笔记？](https://www.zhihu.com/question/371670197/answer/1383895256)
     
     你可以选择不同的软件，或者自己搭建一个信息收集处理的环境。但是**你必须有一个，如果没有，考虑整一个**。

2. Xmind  （画漂亮的思维导图）

    XMind 是一个全功能的思维导图和头脑风暴软件，为激发灵感和创意而生。应用全球最先进的Eclipse RCP 软件架构，全力打造易用、高效的可视化思维软件，强调软件的可扩展、跨平台、稳定性和性能，致力于使用先进的软件技术帮助用户真正意义上提高生产率。
    
    XMind 与Office的横向集成
    XMind 能与用户其它的Office软件紧密集成，保护用户的投资。“XMind 文件”可以被导出成Word / PowerPoint / PDF / TXT / 图片格式等，也可以在导出时选择仅导出图片，还是仅文字，还是图文混排，所得到的成果直接可以纳入用户的资料库，也可用 Word /Powerpoint /Acrobat等工具直接打开编辑，这样用户就可以和没有安装XMIND的其它用户分享思维图。此外，XMind 还支持导入用户的MindManager和FreeMind文件，使得大量用户在从这两个软件转向XMind时，不会丢失之前绘制的思维导图。
    
    XMind改变了中国人没有自己的思维导图工具的现状。国外的所有软件厂商都没有把中文版列为其发展方向之一，且在处理中文的过程中，几乎无一例外的存在Bug。但XMind没有，它是100%纯中文设计，中文处理非常稳定。以至于新加坡的代理商都以“the best practice of using Chinese”为由代理XMind。且XMind的研发团队在国内，各类服务都比较方便。
    
    做好的思维导图还可以保存到**印象笔记**，你可以一键将思维导图的预览图、Xmind文件和文本导入到你的印象笔记里保存，手机上也能很方便的查看。
    
    **给大家提供几个不错的教程**：
    1. XMind使用教程入门 [链接](https://zhuanlan.zhihu.com/p/47772905)
    2. 思维导图神器Xmind使用指南 [链接](https://zhuanlan.zhihu.com/p/32048362)
    3. Xmind教程：思维导图原来这么简单实用 [链接](https://www.jianshu.com/p/7c488d5e4bdf)
    4. 思维导图软件Xmind教程（B站视频）[视频链接](https://www.bilibili.com/video/av455073858/)
    5. XMind教程- 30分钟搞定思维导图（B站视频）[视频链接](https://www.bilibili.com/video/av883316552/)
    
    下载链接：
    
    百度网盘
    

3. Draw.io （专业的流程图）

    Draw.io 是一个强大简洁的在线的绘图网站，支持流程图，UML图，架构图，原型图等图标。支持Github，Google Drive, One drive等网盘同步，并且永久免费。如果觉得使用Web版不方便，draw.io 也提供了多平台的离线桌面版可供下载。

    在线版：https://www.draw.io/  **我比较推荐大家可以使用在线版**

    PC电脑版：http://t.cn/Aid48ecf
    
    特别的，如果你需要使用数学公式，Draw.io支持Markdown（Latex）的语法。 
    
    给大家提供一些教程：
    1. Draw.io--自认为最好用的流程图绘制软件 [链接](https://www.cnblogs.com/HGNET/p/11893280.html)
    2. Draw.io 新手使用教程[链接](https://zhuanlan.zhihu.com/p/129659662)
    3. Draw.io--在线流程图UML图绘制软件简易教程[链接](https://www.jianshu.com/p/833bb9fb8a96)
    4. draw.io 教程（流程图设计工具）（B站**英文**视频）[视频链接](https://www.bilibili.com/video/av455480944/)
    
    

4. Mendeley （参考文献的整理利器）

    Mendeley主要功能：
- 参考文献管理
- PDF文件阅读与标注
- 自动生成参考文献

    总结优点：

    对文献进行分类，统一管理，文章及其内容搜索功能、Details更新功能强大；方便文献阅读，标记、笔记功能齐全，界面简洁养眼；撰写文章时直接引用Mendeley内添加的文献，文献不缺失；后期统一进行文献格式修改，省事、爽。

    给大家提供一些教程：
    1. Mendeley－一款免费好用的文献管理软件 [链接](https://zhuanlan.zhihu.com/p/28762628)
    2. Mendeley教程-参考文献引用（论文撰写必备！）[链接](https://zhuanlan.zhihu.com/p/32249499)
    3. 文献插入引用（Mendeley）+图示说明+完全上手+免费[链接](https://www.jianshu.com/p/cadf09e84c2e)
    
    下载地址:
    
    开源免费软件，请访问[官网](https://www.mendeley.com/) 


#### 常用网站

代码上有什么不会的地方，或者在策略上希望得到一些启示

1. [CSDN](https://www.csdn.net/) 

    CSDN是全球知名中文IT技术交流平台,创建于1999年,包含原创博客、精品问答、职业培训、技术论坛、资源下载等产品服务,提供原创、优质、完整内容的专业IT技术开发社区。

2. [知乎](https://www.zhihu.com)

    有问题，上知乎。知乎，可信赖的问答社区，以让每个人高效获得可信赖的解答为使命。知乎凭借认真、专业和友善的社区氛围，结构化、易获得的优质内容。

3. [B站](https://www.bilibili.com/) 

    这个大家都非常熟悉吧。不能光看动漫哦。

4. [YouTube](https://youtube.com)

    有很多非常优质的大学课程，如果你可以访问的话，好好学。


### ***数据库 - SQL

MariaDB是MySQL的一个分支，其使用方法和MySQL基本一致。百度百科的基本介绍 [请点击](https://baike.baidu.com/item/mariaDB/6466119?fr=aladdin)

#### MariaDB下载 
MariaDB可以在多种平台上使用，Windows平台的下载版本 MariaDB 10.2.14 稳定版，发布时间2018-03-27

~~下载地址为：[64位](https://downloads.mariadb.org/interstitial/mariadb-10.2.14/winx64-packages/mariadb-10.2.14-winx64.msi/from/http%3A//mirrors.tuna.tsinghua.edu.cn/mariadb/) | [32位](https://downloads.mariadb.org/interstitial/mariadb-10.2.14/win32-packages/mariadb-10.2.14-win32.msi/from/http%3A//mirrors.tuna.tsinghua.edu.cn/mariadb/) （32位可以在百度网盘[下载](https://pan.baidu.com/s/1Q-etGpyKBkdoDdu8eoZVBA) 密码：bpyc）~~

中科大的镜像宕机了，建议大家使用官网[链接](https://mariadb.org/download/)，可以在里面选择镜像，建议可以选择清华的。32位或者64位请按照需要。

安装MariaDB时候需要设置，MariaDB会提示输入root用户的口令，**请务必记清楚** （否则貌似需要重新安装才可以调整口令，另外my.ini文件在所有程序 -> MariaDB 里面）。在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。在安装过程中，其他端口的选择都选择默认3306，主机名称 localhost。

服务器 Windows Server 2003 适合版本 5.5.33a 32位 [下载地址](https://downloads.mariadb.org/interstitial/mariadb-5.5.33a/win32-packages/mariadb-5.5.33a-win32.msi/from/http%3A//ftp.hosteurope.de/mirror/archive.mariadb.org/?serve)

#### MariaDB 驱动 

需要支持Python的MySQL驱动来连接到MySQL服务器。MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：

`$ pip install mysql-connector-python --allow-external mysql-connector-python`  （测试可用）

如果上面的命令安装失败，可以试试另一个驱动：

`$ pip install mysql-connector`  （这个没有经过测试）

#### MariaDB 客户端查看 Navicat 

使用Navicat MySQL版本可以方便查看MySQL 和 MariaDB数据库的内容。

百度网盘 [下载](https://pan.baidu.com/s/12BGID7lWlpKyeKfnCxKsmw)  密码：wqtp

将上述资料下载到硬盘里面即可直接使用，点击根目录底下的 navicat.exe 即可。

软件需要注册：名称和组织不用填写，注册码填写： NAVH-WK6A-DMVK-DKW3

设置连接，新建数据库，修改数据库都可以在Navicat里面完成。

#### Python 连接数据库 

`import mysql.connector`

`conn = mysql.connector.connect(host='**.**.**.**', port=3306, user='root', password='******',database='***',charset='utf8')` 该数据库是手动建立的，请填上相应的密码

`cursor = conn.cursor()` 以上三行是数据库连接命令

`cursor.execute('create table stockname (id varchar(20) primary key, name varchar(20), code varchar(20))')`  建表可以在Navicat中完成

`cursor.execute('insert into stockname (id, name, code) values (%s, %s, %s)', ['1', '中国石油', '600001'])`

`conn.commit()` 完成数据库建表以及插入工作

`cursor.close()` 关闭数据库

#### 使用SQLAlchemy

   SQLAlchemy使用了一个所谓ORM技术：Object-Relational Mapping，简单可以理解成把关系数据库的表结构映射到对象上。也就是使用Class的一个实例去存储一个表，然后可以很方便的使用SQLAlchemy的一些函数来进行数据库表格的操作，而不需要使用大量的SQL语句。

安装方法
`pip install sqlalchemy`

`pip install pymysql`

初始化的方法：
`from sqlalchemy import create_engine`

`engine = create_engine('mysql+pymysql://root:password@localhost:3306/test')`

然后可以使用如：
`engine.execute('select * from ....')`

执行通常的SQL语句来操作数据库。
其他一个非常大的好处，就是可以将Pandas的DataFrame直接读出，或者写入MySQL。
注意使用方法

`pd.io.sql.to_sql(DataFrame, table_in_database, engine, schema = database, if_exists = 'append'or'replace'`

`target_DataFrame = pd.read_sql_query('select * from table',engine)`



### *** 机器学习


   机器学习是一门多领域交叉学科，涉及概率论、统计学、凸分析、算法复杂度理论等多门学科。专门研究计算机怎样模拟或实现人类的学习行为，以获取新的知识或技能，重新组织已有的知识结构使之不断改善自身的性能。
    
   它是人工智能的核心，是使计算机具有智能的根本途径。
    
   1. 机器学习是一门人工智能的科学,该领域的主要研究对象是人工智能，特别是如何在经验学习中改善具体算法的性能。
   2. 机器学习是对能通过经验自动改进的计算机算法的研究。
   3. 机器学习是用数据或以往的经验,以此优化计算机程序的性能标准。
    
    
   如果你想学习，我给大家提供一些教材
   [链接](https://github.com/quantitiveFund/pyQuant/tree/master/Learning/MachineLearning/Reading)。但是如果你没有学会Coding，请回去先学好代码，否则离开代码实现去谈算法是没有意义的！