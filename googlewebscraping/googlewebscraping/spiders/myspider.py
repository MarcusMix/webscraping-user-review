import scrapy
import time
import pyautogui
from selenium.webdriver.chrome.service import Service as ChromeService
from googlewebscraping.spiders.web_driver import web_driver
from selenium.webdriver.common.by import By

class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = [
        "https://play.google.com/store/apps/details?id=br.com.winker",
        "https://play.google.com/store/apps/details?id=com.ionicframework.winkerapp199584",
        "https://play.google.com/store/apps/details?id=agile.ti.mobile.condomob",
        "https://play.google.com/store/apps/details?id=com.disney.disneyplus",
        "https://play.google.com/store/apps/details?id=com.whatsapp",
        "https://play.google.com/store/apps/details?id=com.nu.production",
        "https://play.google.com/store/apps/details?id=com.instagram.android",
        "https://play.google.com/store/apps/details?id=com.mercadolibre",
        "https://play.google.com/store/apps/details?id=com.zhiliaoapp.musically",
        "https://play.google.com/store/apps/details?id=com.zzkko"
    ]

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.driver = web_driver()

    
    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(2)
        
        botao_classificacoes = self.driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/c-wiz[4]/section/header/div/div[2]/button')
        botao_classificacoes.click()
        time.sleep(2)
        
        combobox_avaliacoes = self.driver.find_element(By.XPATH, '//*[@id="sortBy_1"]/div[2]')
        combobox_avaliacoes.click()        
        time.sleep(2)
        
        pyautogui.click(x=393, y=428) 
        time.sleep(2)

        html = self.driver.page_source
        sel_response = scrapy.Selector(text=html)

        page_name = sel_response.css('h1.Fd93Bb::text').get()
    
        for item in sel_response.css('div.RHo1pe'):
            div_star = item.css('div.iXRFPc')
            if div_star:
                star = div_star.xpath('@aria-label').get()
            yield {
                'app_name' : page_name,
                'user_reviewer': item.css('div.X5PpBb::text').get(),
                'date': item.css('span.bp9Aid::text').get(),
                'stars': star,
                'commentary' : item.css('div.h3YV2d::text').get(),
                'user_response' : item.css('div.I6j64d::text').get(),
                'date_response' : item.css('div.I9Jtec::text').get(),
                'response' : item.css('div.ras4vb + div::text').get()
            }

    def closed(self, reason):
        self.driver.quit()
