# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import models

class TeonitespiderPipeline(object):
    def process_item(self, item, spider):

        post = models.Post()
        author = models.Authors()
        link = models.Links()

        author.author = item['author']
        author.save()

        link.link= item['link']
        link.save()

        post.post=item['post']
        post.id_author = author
        post.id_link = link


        return item
