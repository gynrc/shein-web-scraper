import scrapy
from ..items import SheinwebscraperItem


class SheinspiderSpider(scrapy.Spider):
    name = "sheinspider"
    allowed_domains = ["shein.com"]
    start_urls = ["https://www.shein.com/Women-Dresses-c-1727.html?ici=www_tab01navbar06&src_module=topcat&src_tab_page_id=page_home1680895637672&src_identifier=fc%3DWomen%60sc%3DDRESSES%60tc%3D0%60oc%3D0%60ps%3Dtab01navbar06%60jc%3Dreal_1727&srctype=category&userpath=category-DRESSES"]

    def parse(self, response):
        items = SheinwebscraperItem()
        name = response.css('.S-product-item__link').css('::text').getall()
        price = response.css('.normal-price-ctn__sale-price').css('::text').getall()
        image_link = response.css('.S-product-item__img-submain::attr(src)').getall()
        
        items['name'] = name
        items['price'] = price
        items['image_link'] = image_link

        yield items
