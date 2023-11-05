import scrapy
# import pandas as pd

class Tugasm8SpiderSpider(scrapy.Spider):
    name = "tugasM8_spider"
    # allowed_domains = ["bit.ly"]
    start_urls = ["https://store.playstation.com/en-id/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/"]

    def parse(self, response):
        titles = response.css("span.psw-t-body.psw-c-t-1.psw-t-truncate-2.psw-m-b-2::text").getall()
        prices = response.css("span.psw-m-r-3::text").getall()

        for title, price in zip(titles, prices):
            yield{
                "Nama Game" : title.strip(),
                "Harga Game" : price.strip()
            }

        for i in range(1, 17):
            next_url = f"https://store.playstation.com/en-id/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/{i}"
            yield scrapy.Request(next_url, callback=self.parse)
        

