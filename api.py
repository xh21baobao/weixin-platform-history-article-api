# -*- encoding: utf-8 -*-
# !/usr/bin/python3
# @Time   : 2019/6/21 11:14
# @File   : api.py
from json import loads
from urllib.request import Request
from urllib.request import urlopen
from ssl import _create_unverified_context
from urllib.parse import urlencode

from settings import USER_AGENT


def get_history_api(h_biz, h_uin, h_key, h_offset, h_count):
    """
    获取公众号历史文章的 api 接口
    :param h_biz: 公众号的识别码 例如：人民日报 的 __biz = "MjM5MjAxNDM4MA=="
    :param h_uin: 登陆的微信账号的识别码
    :param h_key: 获取历史信息必要的 key
    :param h_offset: 偏移量
    :param h_count: 历史图文发布的次数，一次是多图文，最大值10，即获取偏移量后最近10次发布的所有图文消息
    :return: 解析好的json格式字典
    """
    def match_item_info(item_dict):
        """
        文章详情获取
        :param item_dict: 包含单个文章信息的字典
        :return: 结构化的文章信息
        """
        article_title = item_dict.get('title', '')
        article_author = item_dict.get("author", "")
        article_digest = item_dict.get("digest", "")
        article_content_url = item_dict.get("content_url", "").replace("&amp;", "&")
        article_cover_url = item_dict.get("cover", "").replace("&amp;", "&")
        article_source_url = item_dict.get("source_url", "").replace("&amp;", "&")
        copyright_stat = item_dict.get("copyright_stat", 0)
        copy_right = 1 if copyright_stat == 11 else 0
        return {
            "article_title": article_title,  # 文章标题
            "article_author": article_author,  # 文章作者
            "article_digest": article_digest,  # 文章摘要
            "article_content_url": article_content_url,  # 文章详情链接
            "article_cover_url": article_cover_url,  # 封面图片链接
            "article_source_url": article_source_url,  # 源文链接
            "article_copy_right": copy_right,  # 原创
        }
    uri_api = "http://mp.weixin.qq.com/mp/profile_ext"
    form_data = {
        "action": "getmsg",
        "__biz": h_biz,
        "offset": h_offset,
        "count": h_count,
        "uin": h_uin,
        "key": h_key,
        "f": "json",
    }
    request = Request(uri_api, data=urlencode(form_data).encode(), headers={
        "User-Agent": USER_AGENT,
    })
    resp_json = loads(urlopen(request, context=_create_unverified_context()).read().decode(), encoding="utf-8")
    article_infos = []
    next_offset = h_offset
    ending = False
    status = 200 if resp_json.get("errmsg", "") == "ok" else 500
    if status == 200:
        next_offset = resp_json.get("next_offset", -1)
        if next_offset == h_offset:
            ending = True
        if next_offset == -1:
            next_offset = h_offset
            status = False
        general_msg_list = resp_json.get("general_msg_list", "")
        if general_msg_list:
            general_msg_list = loads(general_msg_list, encoding="utf-8").get('list', [])
            for general_msg in general_msg_list:
                app_msg_ext_info = general_msg.get("app_msg_ext_info", {})
                article_infos.append(match_item_info(app_msg_ext_info))

                item_list = general_msg.get('multi_app_msg_item_list', [])
                for each_item in item_list:
                    article_infos.append(match_item_info(each_item))

        else:
            status = 500
            next_offset = h_offset

    return {
        "status": status,  # api使用状态
        "biz": h_biz,  # 公众号__biz标识
        "uin": h_uin,  # app登录用户的必要uin参数
        "cur_offset": h_offset,  # 当前请求的偏移量
        "next_offset": next_offset,  # 下一次请求的偏移量offset
        "key": h_key,  # api必备的app key
        "results": {
            "article_count": len(article_infos),  # 获取的文章数量
            "article_infos": article_infos,  # 获取的全部文章
        },
        "ending": ending  # 是否历史文章爬取完毕，依据offset
    }

