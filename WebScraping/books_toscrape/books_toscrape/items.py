# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#スクレイピングで取得したデータを格納する入れ物のようなもの
#アイテムの各フィールドはこのような形で定義し、予め定義していないとデータを格納できません。
#spiderではアイテムを使わずに、辞書に格納することもできる。

import scrapy


class BooksToscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
