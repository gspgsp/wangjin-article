# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .sqlutil import SqlUtil
from wangjin.items import ArticleItem

class WangjinPipeline(object):
    def process_item(self, item, spider):
        sqlutil = SqlUtil()
        # 资讯
        if isinstance(item, ArticleItem):
            ret = sqlutil.is_exist('fanwe_article', ['original_id'], item)
            if ret[0] == 1:
                # 更新数据
                sqlutil.update_data('fanwe_article', 'original_id = ' + item['original_id'], item)
            else:
                sqlutil.insert_data('fanwe_article', item)
