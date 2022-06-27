# 2022-06-05
此仓库已用Scrapy重构


# python所需要的库：
+ pip install scrapy
+ pip install pymongo
+ pip install aiohttp
# 使用方法：
1. 请进入`porn`文件夹，与`settings.py`文件同级，创建`units.py`文件，内容模板如下：
```python

proxy_url = '你使用的代理ip服务商提供的接口地址'
MONGO_URI = 'mongodb://127.0.0.1:27017/'#数据库地址

```
2. 运行项目
```shell
scrapy crawl PornSpider
```

# 说明：
+ 该网站现视频为m3u8格式文件，但也可以变成视频，可参考第三方包`m3u8_to_MP4`
+ 此脚本仅供交流学习使用
+ 如有其他更多更好的建议请告诉我
+ 网站规则随时可能会改变，后续可能无法及时更新，请自行研究

# 关于作者：
邮箱：1176103825@qq.com


# 如果你愿意，可以请我喝杯卡布奇诺：

<img src="https://github.com/xinghe98/91porn/blob/master/src/1.jpg" width = "537" height = "728" alt="付款码" align=center />
