#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
def baiduFanyi(word):
    """百度翻译单词查询"""
    url = 'https://fanyi.baidu.com/sug'
    header = {
        "User-Agent": "Mozilla/5.0"
    }
    data = {
        'kw': word
    }
    response = requests.post(url, headers=header, data=data)
    resData = response.json()  # 把返回的json数据转为字典
    print(resData)
    result = resData['data'][0].get('v')
    return result
if __name__ == '__main__':
    word = input('input world')
    print(baiduFanyi(word))