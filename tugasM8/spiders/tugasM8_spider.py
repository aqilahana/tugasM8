import scrapy

class Tugasm8SpiderSpider(scrapy.Spider):
    name = "tugasM8_spider"

    start_urls = ["https://store.playstation.com/en-id/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/"]

    def parse(self, response): # mengambil judul dan harga game
        titles = response.css("span.psw-t-body.psw-c-t-1.psw-t-truncate-2.psw-m-b-2::text").getall()
        prices = response.css("span.psw-m-r-3::text").getall()

        for title, price in zip(titles, prices): # masukan ke dictionary satu persatu data yang telah diambil
            yield{
                "Nama Game" : title.strip(),
                "Harga" : price.strip()
            }

        for i in range(2, 17): # untuk ambil data next page, dimulai dari 2 sampai 16 (ditambah 1 karena range)
            next_url = f"https://store.playstation.com/en-id/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/{i}"
            yield scrapy.Request(next_url, callback=self.parse)
        

