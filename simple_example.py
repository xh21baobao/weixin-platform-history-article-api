# -*- encoding: utf-8 -*-
# !/usr/bin/python3
# @Time   : 2019/6/21 17:42
# @File   : simple_example.py

from api import get_history_api

if __name__ == '__main__':
    """ '%3D%3D' 与 '==' 等价"""
    # 每一个公众号公众号都存在的公开的__biz信息
    biz = "MjM5MjAxNDM4MA=="  # 人民日报的 __biz 信息，也可以记做 MjM5MjAxNDM4MA%3D%3D
    # 账号私密的uin信息，私密信息部分已****注释，换成自己的账号uin
    uin = "MTE3MzE2NjAxOA=="  # 微信app登录用户的uin信息，也可以记做 MTE3Mz********%3D%3D

    # 一个较长的公众号数据请求验证密钥 key, 有限时间内的单个公众号的密钥私密信息，下方的key只是样例
    key = "45382ee80ea507801b0ff835bc3c41487737f61a1b82cace7858864ed6439d79a82a11ae4e4132de29f92ee9670c8baf039647fcbefddc637adf0e2a94385ad6b540c18c4b16ea184a23e4fee0bac6d3"

    # 自定义的偏移量及最大获取时间线数
    offset = "0"  # 公众号历史消息偏移量，起始位置为0，从当前最新图文发布时间向后递增
    count = "10"  # 由当前偏移量发布图文时间起算，历史连续不同发布时间的发布次数，最大限制为10

    # 调用的api
    result = get_history_api(biz, uin, key, offset, count)
    print(result)  # 获取的请求结果
