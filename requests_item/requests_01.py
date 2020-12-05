# -*- coding:utf-8 -*-
#- 需求：爬取搜狗首页的页面数据

import requests
import sys


if __name__ == "__main__":
    # step 1：指定URL
    url = "https://www.sogou.com/"
    # step 2：发起请求
    # get方法会返回一个响应对象
    response = requests.get(url=url)
    # step 3：获取响应数据
    # text返回的是字符串形式的响应数据
    page_text = response.text
    # 获取当前文件路径，并生成保存文件位置
    save_path = sys.path[0]
    file_name = "{}/sogou.html".format(save_path)
    # step 4：持久化存储
    with open(file_name, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    
    print("爬取数据结束！！！")

