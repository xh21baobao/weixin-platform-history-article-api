# -*- encoding: utf-8 -*-
# !/usr/bin/python3
# @Time   : 2019/6/21 17:42
# @File   : simple_example.py

from api import get_history_api

if __name__ == '__main__':
    """ '%3D%3D' 与 '==' 等价"""
    # 每一个公众号公众号都存在的公开的__biz信息
    biz = "MjM5MjAxNDM4MA=="  # 人民日报的 __biz 信息，也可以记做 MjM5MjAxNDM4MA%3D%3D
    # 账号私密的uin信息
    uin = "MTE3Mz********=="  # 微信app登录用户的uin信息，也可以记做 MTE3MzE2NjAxOA%3D%3D

    # 一个较长的公众号数据请求验证密钥 key, 有限时间内的单个公众号的密钥私密信息，下方的key只是样例
    key = "c47853a08ff0b5dfa2d8577abec94139b456b36e84fe805909478b9bd67354a9853abd97e1eb0ac53ab2ee9dccfcfec938e58069028f0d588972db2374137c0f1079a5779ef77afbe35c9a8c882a3117"

    # 自定义的偏移量及最大获取时间线数
    offset = "0"  # 公众号历史消息偏移量，起始位置为0，从当前最新图文发布时间向后递增
    count = "10"  # 由当前偏移量发布图文时间起算，历史连续不同发布时间的发布次数，最大限制为10

    # 调用的api
    result = get_history_api(biz, uin, key, offset, count)
    print(result)  # 获取的请求结果
