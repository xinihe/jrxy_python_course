## 课程要求

本课程的课程内容在[README](README.md)上可以读到，有任何问题或者建议，请联系授课老师。

本课程需要你对以下内容具有初步的了解，由于课堂时间有限，因此希望你能通过课余的时间进行查漏补缺。

1. Anaconda 

    [Anaconda](https://www.anaconda.com)指的是一个开源的Python发行版本，其包含了Python, R等180多个科学包及其依赖项。这是什么意思呢？Python是一门编程语言，使用这门语言的时候，在写代码这件事情之外，还有很多其他的配套工作，比如运行脚本、下载各种需要用到的库、管理环境等。Anaconda就把这些功能全都集成好了，省去很多琐碎的工作。简单来说，Anaconda帮你管理了在使用Python时用到的包和环境。
    
    Anaconda集成了大部分需要用到的Python包，尤其是数据科学类的包，在数据处理方面，你几乎可以在安装后直接进行使用。
    
    利用自带的conda，Anaconda能够对Python包安装、卸载和更新。Python的一大优势即是丰富的第三方的包，比如数据处理的numpy、数据分析的pandas、和我们做深度学习用到的keras，都是我们所说的包。安装和管理这些包是使用Python的日常。Anaconda是一个便利简洁的包管理器。
    
     下载使用：
    如果你嫌官网下载太慢,这里建议大家使用[清华镜像](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)，找到对应的anaconda版本和操作系统即可。

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



### 个人推荐

以下的内容是我个人的推荐，相信对你的学习会有用的。


1. Notebook (Evernote)


2. Xmind


3. Draw.io

4. Mendeley 


代码上有什么不会的地方，或者在策略上希望得到一些启示

1. CSDN

2. 知乎

3. B站 

4. YouTube


有一些cheatsheet提供给大家，也许有点用处