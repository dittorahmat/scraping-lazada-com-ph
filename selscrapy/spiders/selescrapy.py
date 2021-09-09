import scrapy
from scrapy.utils.project import get_project_settings
from selenium.webdriver import Chrome, ChromeOptions
from selscrapy.items import SelscrapyItem

class SelescrapySpider(scrapy.Spider):
    name = 'selescrapy'
    allowed_domains = ['lazada.com.ph']

    def start_requests(self):
        settings = get_project_settings()
        driver_path = settings.get('CHROME_DRIVER_PATH')
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(executable_path=driver_path, options=options)

        driver.get('https://www.lazada.com.ph/shop-laptops/')
        driver.implicitly_wait(60)
        link_elements = driver.find_elements_by_css_selector('div._8JShU > a')
        for link_el in link_elements:
            href = link_el.get_attribute("href")
            yield scrapy.Request(href)

        driver.quit()

    def parse(self, response):
        item = SelscrapyItem()
        item['price'] = response.css('#module_product_price_1 > div > div > span ::text').get()
        item['name'] = response.css('h1 ::text').get()
        yield item

