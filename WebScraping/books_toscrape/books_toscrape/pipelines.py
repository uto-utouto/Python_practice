# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#Webサイトから取得したデータのクレンジング、チェック、DBへの更新などの処理
#を記述するのに利用する

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BooksToscrapePipeline:
    def process_item(self, item, spider):
        return item
