# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

#作品表
class PostsItem(scrapy.Item):
    # define the fields for your item here like:
    table_name = 'posts' #表名
    pid = Field() #'作品表主键'
    title = Field()  # '作品表主键'
    thumbnail = Field()  # '视频缩略图'
    preview = Field()  # '视频预览图'
    video = Field()  # '视频链接'
    video_format = Field()  # '视频格式：4K 等'
    category = Field()  # '作品分类'
    duration = Field()  # '播放时长'
    created_at = Field()  # '发表时间'
    description = Field()  # '作品描述'
    play_counts = Field()  # '播放次数'
    like_counts = Field()  # '被点赞次数'

#创作者表
class ComposersItem(scrapy.Item):
    table_name = 'composers'  # 表名
    cid = Field()  # '创作者表主键'
    banner = Field()  # '用户主页banner图片'
    avatar = Field()  # '用户头像'
    verified = Field()  # '是否加V'
    name = Field()  # '名字'
    intro = Field()  # '自我介绍'
    like_counts = Field()  # '被点赞次数'
    fans_counts = Field()  # '被关注数量'
    follow_counts = Field()  # '关注数量'
    location = Field()  # '所在位置'
    career = Field()  # '职业'

#评论表
class CommentsItem(scrapy.Item):
    table_name = 'comments'  # 表名
    commentid = Field()  # '评论表主键'
    pid = Field()  # '评论的作品ID'
    cid = Field()  # '评论人ID'
    avatar = Field()  # '评论人头像'
    uname = Field()  # '评论人名称'
    created_at = Field()  # '发表时间'
    content = Field()  # '评论内容'
    like_counts = Field()  # '被点赞次数'
    reply = Field()  # '回复其他评论的ID，如果不是则为0'

#视频创作中间表
class CopyrightsItem(scrapy.Item):
    table_name = 'copyrights'  # 表名
    pcid = Field()  # '主键，由pid_cid组成'
    pid = Field()  # '对应作品表主键'
    cid = Field()  # '对应作者表主键'
    roles = Field()  # '担任角色'





