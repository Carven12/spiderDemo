import scrapy
import logging

from spiderDemo.items import SpiderDemoItem


class DownloadMovieSpider(scrapy.Spider):

    name = "download_movie"

    url = 'http://www.7nmg.com/show/5815.html'

    domains = 'http://www.7nmg.com'

    def start_requests(self):
        return[scrapy.Request(url=self.url, callback=self.get_detail)]

    def get_detail(self, response):
        for each in response.css('li.dslist-group-item a'):
            # 初始化模型对象
            item = SpiderDemoItem()
            # 文件名
            item['fileName'] = each.css('::text').extract()[0]
            # 文件URL
            item['filePlayerUrl'] = self.domains + each.attrib['href']
            logging.info('文件名：' + item['fileName'])
            logging.info('文件播放地址：' + item['filePlayerUrl'])
            yield scrapy.Request(url=item['filePlayerUrl'], callback=self.parse, meta={'item': item})

    def parse(self, response):
        logging.info('解析播放页面中...')
        item = response.meta['item']
        urls = response.css('iframe::attr(src)').extract()
        if len(urls) != 0:
            logging.info('深度解析播放页面中...')
            url = urls[0]
            yield scrapy.Request(url=url, callback=self.parse, meta={'item': item})
        else:
            item['fileDownLoadUrl'] = response.css('video.dplayer-video.dplayer-video-current').extract()[0]
            logging.info('文件下载地址：' + item['fileDownLoadUrl'])
            yield item


