Url Checker
==========================

Detect the availability of the URLs with txt file or webpage
---
+ Requirements

> Python3

+ Usage

  - Local
  > python3 url_checker.py url.txt ( one URL per line )

  - Web
  > python3 url_checker.py https://xxx.com/x.txt ( will collect all URLs on page )
  
批量检测在线或本地文本中 URL 的有效性
---
+ 环境需求

> Python3

+ 用法

  * 验证本地文本文件中的 url：运行以下命令
  > python3 url_checker.py url.txt ( 一行一条 url )

  * 在线文本文件
  > python3 url_checker.py https://xxx.com/x.txt ( 将会收集该网址中的所有 url 并验证 )

  * 结果
  > 会生成三个 txt 文件
  
  |文件|内容|
  |---|----|
  |result.txt|有效 url|
  |urlBroken.txt|失效 url|
  |urlJsError.txt|撞上江苏内墙的 url|
