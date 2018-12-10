# -*- coding: utf-8 -*-
import json
import re

import scrapy
# from scrapy.spiders import CrawlSpider,Rule #导入爬虫类，规则
# from scrapy.linkextractors import LinkExtractor #导入链接类


from ..items import PostsItem, CommentsItem, CopyrightsItem, ComposersItem

#cookies
cookies = {"Authorization":"0A2E37B018B077BE418B074D9618B07A43418B07C3526C6E7C92"}

def convert_int(s):
    if s:
        return int(s.replace(',', ""))
    return 0
ci = convert_int

class DiscoverySpider(scrapy.Spider):
    name = 'discovery'
    allowed_domains = ['xinpianchang.com',"openapi-vtom.vmovier.com"]
    start_urls = ['http://www.xinpianchang.com/channel/index/sort-like']

    # rules = (
    #     Rule(
    #         LinkExtractor(allow=('page\-\d+',),
    #                       restrict_xpaths=('//div[@class="page-wrap"]')
    #                       ),
    #         # 符合正则的链接,restrict_xpaths使用xpath表达式，和allow共同作用过滤链接
    #         callback='parse_item',  # 回调函数
    #         follow=True,  # 是否跟随
    #     ),
    # )

    #重写start_requests
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,dont_filter=True,cookies=cookies)

    #列表页
    def parse(self, response):
        post_list = response.xpath('//ul[@class="video-list"]/li')
        for post in post_list:
            pid = post.xpath('./@data-articleid').extract_first() #视频id
            thumbnail = post.xpath('./a/img/@_src').extract_first() #视频缩略图

            #详情
            url = "http://www.xinpianchang.com/a%s?from=ArticleList" % pid

            # 需要使用item
            item = PostsItem()
            item['pid'] = pid
            item['thumbnail'] = thumbnail

            yield scrapy.Request(url=url, callback=self.parse_post, meta={'item': item})

        # #爬取其他页的内容
        page_urls = response.xpath('//div[@class="page-wrap"]//a/@href').extract()
        for page_url in page_urls:
            yield scrapy.Request(url=page_url,cookies=cookies)


    #视频详情
    def parse_post(self, response):
        item = response.meta['item']
        pid = item['pid']
        #title
        title = response.xpath('/html/body/div[8]/div[2]/div[1]/div[1]/div[1]/div[2]/h3/text()').extract_first()
        #category
        category_list = response.xpath('//span[@class="cate v-center"]/a/text()').extract()
        category = '-'.join([cate.strip() for cate in category_list])
        #created_at
        created_at = response.xpath('//span[@class="update-time v-center"]/i/text()').extract_first()
        #play_counts
        play_counts = response.xpath('//i[@data-curplaycounts]/@data-curplaycounts').extract_first()
        #like_counts
        like_counts = response.xpath('//span[@data-counts]/@data-counts').get()
        #description
        description = response.xpath('//p[contains(@class,"desc")]/text()').get()
        if description:
            description = description.strip()
        else:
            description = "暂无描述"

        item['title'] = title
        item['category'] = category
        item['created_at'] = created_at
        item['play_counts'] = play_counts
        item['like_counts'] = like_counts
        item['description'] = description

        #视频资源
        vid = re.findall('vid: \"(.+?)"',response.text)[0]
        url = "https://openapi-vtom.vmovier.com/v3/video/%s?expand=resource,resource_origin?" % vid
        yield scrapy.Request(url=url,callback=self.parse_video, meta={'item': item})

        #评论信息
        comment_url = "http://www.xinpianchang.com/article/filmplay/ts-getCommentApi?id=%s&ajax=0&page=1" % pid
        yield scrapy.Request(url=comment_url, callback=self.parse_comment,meta={'currentpid': pid,'currentpage':1},cookies=cookies)

        #作者信息
        composers_list = response.xpath('//div[@class="filmplay-creator right-section"]/ul[@class="creator-list"]/li')
        for composers in composers_list:
            composers_id = composers.xpath('./a/@data-userid').get()
            url = "http://www.xinpianchang.com/u%s?from=articleList" % composers_id
            yield scrapy.Request(url=url,callback=self.parse_composers,meta={'c_id':composers_id})

            #每一个作者
            copyrights_item = CopyrightsItem()
            copyrights_item['pcid'] = "%s_%s" % (pid, composers_id)
            copyrights_item['pid'] = pid
            copyrights_item['cid'] = composers_id
            copyrights_item['roles'] = composers.xpath('.//*[contains(@class,"role")]/text()').get()
            yield copyrights_item


    # 视频资源
    def parse_video(self,response):
        item = response.meta['item']

        res = json.loads(response.text)
        #preview
        preview = res['data']["video"]["cover"]
        # video
        video = res['data']["resource"]["default"]["url"]
        # video_format
        video_format = res['data']["resource"]["default"]["profile_code"]
        #duration
        duration = res['data']["resource"]["default"]["duration"]

        item['preview'] = preview
        item['video'] = video
        item['video_format'] = video_format
        item['duration'] = duration

        yield item

    # 评论数据
    def parse_comment(self, response):
        item = CommentsItem()
        currentpid = response.meta['currentpid']
        currentpage= response.meta['currentpage']

        jsonres = json.loads(response.text)
        # 总页数
        totalpage = jsonres['data']['total_page']
        # 这页的数据
        comment_list = jsonres['data']['list']
        for comment in comment_list:
            commentid = comment['commentid']  # '评论表主键'
            pid = comment['articleid']  # '评论的作品ID'
            cid = comment['userInfo']['userid']  # '评论人ID'
            avatar = comment['userInfo']['face']  # '评论人头像'
            uname = comment['userInfo']['username']  # '评论人名称'
            created_at = comment['addtime_int']  # '发表时间'
            content = comment['content']  # '评论内容'
            like_counts = comment['count_approve']  # '被点赞次数'

            reply = comment['reply']  # '回复其他评论的ID，如果不是则为0'
            if len(reply) > 0:
                reply = comment['reply']['commentid']
            else:
                reply = '0'

            item['commentid'] = commentid
            item['pid'] = pid
            item['cid'] = cid
            item['avatar'] = avatar
            item['uname'] = uname
            item['created_at'] = created_at
            item['content'] = content
            item['like_counts'] = like_counts
            item['reply'] = reply

            yield item

        if currentpage <= totalpage:
            currentpage += 1
            comment_url = "http://www.xinpianchang.com/article/filmplay/ts-getCommentApi?id=%s&ajax=0&page=%d" % (currentpid,currentpage)
            yield scrapy.Request(url=comment_url, callback=self.parse_comment, meta={'currentpid': currentpid,'currentpage':currentpage},
                                 cookies=cookies)

    #作者
    def parse_composers(self, response):
        # '创作者表主键'
        cid = response.meta['c_id']
        # '用户主页banner图片'
        banner = response.xpath('//div[@class="banner-wrap"]/@style').get()
        banner = re.findall('background-image:url\((.+?)\)',banner[0])
        # '用户头像'
        avatar = response.xpath('//span[@class="avator-wrap-s"]/img/@src').get()
        # '是否加V'
        verified = response.xpath('//span[@class="avator-wrap-s"]/span[contains(@class,"author-v")]').get()
        verified = "yes" if verified else "no"
        # '名字'
        name = response.xpath('//div[@class="creator-info"]/p[1]/text()').get()
        # '自我介绍'
        intro = response.xpath('//div[@class="creator-info"]/p[2]/text()').get()

        # '被点赞次数' 人气
        like_counts = ci(response.xpath('//div[contains(@class,"creator-detail")]/span[1]/span[2]/text()').get())
        # '被关注数量',
        fans_counts = ci(response.xpath('//div[contains(@class,"creator-detail")]/span[2]/span[2]/text()').get())
        # '关注数量',
        follow_counts = ci(response.xpath('//div[contains(@class,"creator-detail")]/span[3]/span[2]/text()').get())

        # '所在位置',
        location = response.xpath('//div[contains(@class,"creator-detail")]/span[5]/text()').get()
        location = location if location else ""

        # '职业',
        career = response.xpath('//div[contains(@class,"creator-detail")]/span[7]/text()').get()
        career = career if career else ""

        composer_item = ComposersItem()
        composer_item['cid'] = cid
        composer_item['banner'] = banner
        composer_item['avatar'] = avatar
        composer_item['verified'] = verified
        composer_item['name'] = name
        composer_item['intro'] = intro
        composer_item['like_counts'] = like_counts
        composer_item['fans_counts'] = fans_counts
        composer_item['follow_counts'] = follow_counts
        composer_item['location'] = location
        composer_item['career'] = career
        yield composer_item















