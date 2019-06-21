# WeChatPlatformArticle
微信公众号历史文章爬取api
@author：詹生松
@api site: https://github.com/xzkzdx/WeChatPlatformArticle


### 所需工具
1、环境依赖：建议使用 python3
2、请下载源码自行调试： git clone git@github.com:xzkzdx/WeChatPlatformArticle.git
3、建议使用fiddler抓包工具，或手写类似fiddler代理转发的工具


### 关于接口参数的获取
1、使用fiddler抓包工具获取必要的请求参数例如：uin 与 key
2、biz 也就是 __biz ，获取方式在公众号历史消息链接里，复制公众号历史消息的链接，找到&__biz=xxx==&中xxx==部分，样例代码给的是人民日报的__biz


### 调用api返回的json结果
```angular2
# api调用结果的字段描述
api_result = 
{
    "status": status,  # api使用状态 200 正常，400请求错误
    "biz": h_biz,  # 公众号__biz标识
    "uin": h_uin,  # app登录用户的必要uin参数
    "cur_offset": h_offset,  # 当前请求的偏移量
    "next_offset": next_offset,  # 下一次请求的偏移量offset  status不为200时，会与cur_offset一致，用于调试
    "key": h_key,  # api必备的app key
    "results": {
        "article_count": len(article_infos),  # 获取的文章数量
        "article_infos": article_infos,  # 获取的全部文章信息
    },
    "ending": ending  # 是否历史文章爬取完毕，依据offset，可用于自定义增量爬取的结束条件
}
# 文章信息字段描述
article_infos = [{
    "article_title": article_title,  # 文章标题
    "article_author": article_author,  # 文章作者
    "article_publish_time": article_publish_time,  # 文章发布时间
    "article_digest": article_digest,  # 文章摘要
    "article_content_url": article_content_url,  # 文章详情链接
    "article_cover_url": article_cover_url,  # 封面图片链接
    "article_source_url": article_source_url,  # 源文链接
    "article_copy_right": copy_right,  # 1原创  0非原创
},]
```

#### 样例：simple_example.py
```angular2

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

```

### 赞助

![image](https://github.com/xzkzdx/image/blob/master/B0A68029F4378AD2D625296986E9BA98.png){:height="100" width="100"}