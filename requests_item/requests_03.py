# 破解百度翻译，爬取百度翻译返回结果

import requests
import json
import sys

if __name__ == "__main__":
    # step1: 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # step2: UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.1'
    }
    # step3: post请求参数处理
    data = {
        'kw': 'dog'
    }
    # step4: 发送请求
    response = requests.post(url=post_url, data=data, headers=headers)
    # step5: 获取响应数据：json()方法返回的是obj(在确认返回数据是json类型时才可以使用json方法)
    obj_dict = response.json()
    # step6: 获取当前文件目录,生成文件存储路径
    save_path = sys.path[0]
    file_path = "{}\{}".format(save_path, 'dog.json')
    # step7: 进行持久化存储
    save_file = open(file_path, 'w', encoding='utf-8')
    json.dump(obj_dict, fp=save_file, ensure_ascii=False)
    print('done！！')
    