#### 什么是爬虫

爬虫：一段自动抓取互联网信息的程序，从互联网上抓取对于我们有价值的信息。


> 通过编程向网络服务器请求数据（HTML表单），然后解析HTML，提取出自己想要的数据


![](<img src = "spider_01.jpg" width = "50%">)

归纳为四大步：

- 根据url获取HTML数据
- 解析HTML，获取目标信息
- 存储数据
- 重复第一步

这会涉及到数据库、网络服务器、HTTP协议、HTML、数据科学、网络安全、图像处理等非常多的内容。





##### 什么是HTML


HTML 是整个网页的结构，相当于整个网站的框架。带“＜”、“＞”符号的都是属于 HTML 的标签，并且标签都是成对出现的。

常见的标签如下：

```python
<html>..</html> 表示标记中间的元素是网页
<body>..</body> 表示用户可见的内容
<div>..</div> 表示框架
<p>..</p> 表示段落
<li>..</li>表示列表
<img>..</img>表示图片
<h1>..</h1>表示标题
<a href="">..</a>表示超链接
```
**CSS**  表示样式，在 CSS 中定义了外观。
**JScript** 表示功能。交互的内容和各种特效都在 JScript 中，JScript 描述了网站中的各种功能。

如果用人体来比喻，HTML 是人的骨架，并且定义了人的嘴巴、眼睛、耳朵等要长在哪里。CSS 是人的外观细节，如嘴巴长什么样子，眼睛是双眼皮还是单眼皮，是大眼睛还是小眼睛，皮肤是黑色的还是白色的等。JScript 表示人的技能，例如跳舞、唱歌或者演奏乐器等。


>HTML (HyperText Markup Language) is the most basic building block of the Web. It defines the meaning and structure of web content. Other technologies besides HTML are generally used to describe a web page's appearance/presentation (CSS) or functionality/behavior (JavaScript).

一个HTML的例子



#### 关于爬虫的合法性

几乎每一个网站都有一个名为 robots.txt 的文档，当然也有部分网站没有设定 robots.txt。对于没有设定 robots.txt 的网站可以通过网络爬虫获取没有口令加密的数据，也就是该网站所有页面数据都可以爬取。如果网站有 robots.txt 文档，就要判断是否有禁止访客获取的数据。

https://xueqiu.com/robots.txt


User-agent: * 代表的所有的搜索引擎种类，

Disallow: /admin/ 这里定义是禁止爬寻admin目录下面的目录

Disallow: /require/ 这里定义是禁止爬寻require目录下面的目录

Disallow: /ABC/ 这里定义是禁止爬寻ABC目录下面的目录

Disallow: /cgi-bin/*.htm 禁止访问/cgi-bin/目录下的所有以”.htm”为后缀的URL(包含子目录）。

Disallow: /*?* 禁止访问网站中所有包含问号 (?) 的网址

Disallow: /.jpg$ 禁止抓取网页所有的.jpg格式的图片

Disallow:/ab/adc.html 禁止爬取ab文件夹下面的adc.html文件。



#### 使用 requests 库请求网站
安装 requests 库

pip install requests


####爬虫的基本原理

网页请求的过程分为两个环节：
- Request （请求）：每一个展示在用户面前的网页都必须经过这一步，也就是向服务器发送访问请求。
- Response（响应）：服务器在接收到用户的请求后，会验证请求的有效性，然后向用户（客户端）发送响应的内容，客户端接收服务器响应的内容，将内容展示出来，就是我们所熟悉的网页请求.


网页请求的方式也分为两种：
- GET：最常见的方式，一般用于获取或者查询资源信息，也是大多数网站使用的方式，响应速度快。
- POST：相比 GET 方式，多了以表单形式上传参数的功能，因此除查询信息外，还可以修改信息。

所以，在写爬虫前要先确定向谁发送请求，用什么方式发送。





### 使用 GET 方式抓取数据

import requests        #导入requests包
url = 'https://xueqiu.com/'
res = requests.get(url)        #Get方式获取网页数据

print(res.text)



#### 为什么要设置headers?

在请求网页爬取的时候，输出的text信息中会出现抱歉，无法访问等字眼，这就是禁止爬取，需要通过反爬机制去解决这个问题。

headers是解决requests请求反爬的方法之一，相当于我们进去这个网页的服务器本身，假装自己本身在爬取数据。

对反爬虫网页，可以设置一些headers信息，模拟成浏览器取访问网站 。

#### headers 哪里找

谷歌或者火狐浏览器，在网页面上点击：右键–>检查

headers中有很多内容，主要常用的就是user-agent 和 host，他们是以键对的形式展现出来，如果user-agent 以字典键对形式作为headers的内容，就可以反爬成功，就不需要其他键对；否则，需要加入headers下的更多键对形式。



### 使用 GET 方式抓取数据

import requests        #导入requests包
url = 'https://xueqiu.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
res = requests.get(url, headers = headers)        #Get方式获取网页数据
res.encoding = 'utf-8'  # 保证中文的显示
print(res.text)





#### 使用POST 方式

import requests        #导入requests包
import json

def get_translate(word):
    # General Request URL
    url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
    form_data = {'from':'zh', 'to':'en', 'query':word, 'transtype':'translang', 'simple_means_flag':'3', 'sign':'777849.998728', 'token':'8fdc86c1912abf9a6792ab0df40760c5', 'domain':'common'}
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Cookie':'BIDUPSID=BD1F6031E6E1F58EBA5780A6882450DB; PSTM=1511924987; BDUSS=2F1RlhGZEZGZzJFOE1RZExnazN2bWZTTWc4aWswVWRnOTFKUWh3UjA1MVJZblpiQUFBQUFBJCQAAAAAAAAAAAEAAACIDXkhbmloZTc4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFHVTltR1U5bZ; H_WISE_SIDS=139560_141910_100805_142081_142208_142066_135847_141001_138596_140853_141916_142002_137758_138878_137985_141200_140173_131246_137746_138165_107319_138883_140260_141838_140632_139043_140202_140592_136861_138585_141651_140988_141900_140113_140324_140579_133847_131423_140367_140965_136537_141102_110085_141941_127969_140593_131953_139887_140995_138425_138943_141190_141924; BDUSS_BFESS=2F1RlhGZEZGZzJFOE1RZExnazN2bWZTTWc4aWswVWRnOTFKUWh3UjA1MVJZblpiQUFBQUFBJCQAAAAAAAAAAAEAAACIDXkhbmloZTc4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFHVTltR1U5bZ; delPer=0; PSINO=3; ZD_ENTRY=bing; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; session_name=cn.bing.com; MCITY=-%3A; BAIDUID=32A052A10603308B16C560D6C9D060BE:FG=1; BAIDUID_BFESS=F170A5773764B336959E01B66D608AFB:FG=1; session_id=1604470913738; H_PS_PSSID=1424_33043_32947_33059_31253_32971_32706_32961_32846; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1605020596; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1605020596; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjsv5_shitong=1.0_7_50d6a0d85be4941d2e489f60c1c0ce1e8ce8_300_1605020594794_124.160.64.90_b1c9306c; yjs_js_security_passport=64e43975da70565c859cacfcc9d315009e61e875_1605020596_js'
        }
    #请求表单数据
    response = requests.post(url,data=form_data, headers=headers)
    #将Json格式字符串转字典
    content = json.loads(response.text)
    print(content)


get_translate('中国银行')