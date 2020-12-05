"""
需求：爬取带搜索参数的搜狗页面
UA检测：User-Agent(请求载体的身份标识)
        门户网站的服务器会检车对应请求的载体身份标识，
    如果检测到请求的载体身份标识为某一款浏览器，
    视该请求为正常的请求
        如果监测到请求的载体身份标识不基于款浏览器，
    则标识该请求为不正常的请求，是一个爬虫程序
UA伪装：让爬虫对应的请求载体身份标识伪装成浏览器
"""

import requests

if __name__ == "__main__":
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    url = "https://www.sogou.com/web?q"
    # 处理URL携带的参数，封装到字典中
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    # 对指定的url发起的请求对应的url是携带参数的
    # 并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)
    page_test = response.text
    file_name = "./requests_item/{}{}".format(kw, '.html')
    with open(file_name, 'w', encoding='utf-8') as f:\
        f.write(page_test)
    print_result = "{} {}".format(file_name, 'save done！')
    print(print_result)

