import scrapy
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


class OzonSpider(scrapy.Spider):
    name = "ozon"

    def start_requests(self):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.get("https://www.ozon.ru/")
        driver.implicitly_wait(0.5)
        driver.find_element(By.XPATH, '//*[@id="stickyHeader"]/div[1]/div/button/div[2]').click()
        driver.find_element(By.XPATH, '//*[@id="15500"]/div[2]/div[1]/div[1]/div[1]/a[2]').click()
        driver.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/input').click()
        urls = []

        while urls.len() < 101:
            elements = driver.find_elements(By.CLASS_NAME, 'i9a')
            urls = urls + elements
            driver.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/a/div[2]').click()
        driver.quit()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        os = response.xpath('//*[@id="section-characteristics"]/div[2]/div[1]/div[2]/dl[4]/dd/text()').get()
        yield os
