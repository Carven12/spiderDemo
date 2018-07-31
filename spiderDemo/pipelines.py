# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request
import os


class SpiderdemoPipeline(object):
    def process_item(self, item, spider):

        # 下载地址
        downloadUrl = item['fileDownLoadUrl']

        # 文件存放地址
        localFileUrl = 'D:\迅雷下载\大长今'

        local = os.path.join(localFileUrl, item['fileName'] + '.mp4')

        urllib.request.urlretrieve(downloadUrl, local, self.Schedule)

    def Schedule(a, b, c):
        """
        a:已经下载的数据块
        b:数据块的大小
        c:远程文件的大小
       """
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        print
        '%.2f%%' % per
