import scrapy
#実行コマンド(同じディレクトリ内で)
#scrapy crawl books_basic
#scrapy crawl books_basic -o book_fantasy.json

class BooksBasicSpider(scrapy.Spider):
    name = 'books_basic'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html']

    def parse(self, response):
        books = response.xpath('//h3')
        #books = response.css('h3')
        for book in books:
            yield {
                #'books':books
                'Title': book.xpath('.//a/@title').get(),
                'URL': book.xpath('.//a/@href').get()
                # 'Title': book.css('a::attr(title)').get(),
                # 'URL': book.css('a::attr(href)').get()
            }
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        # next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
            
            