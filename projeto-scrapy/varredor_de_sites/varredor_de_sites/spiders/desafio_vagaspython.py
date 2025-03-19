import scrapy
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
import urllib
from time import sleep

def iniciar_driver():
    chrome_options = Options()
    LOGGER.setLevel(logging.WARNING)
    arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--headless']
    for argument in arguments: 
        chrome_options.add_argument(argument)
    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': 'D:\\Storage\\Desktop\\projetos selenium\\downloads',
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    # inicializando o webdriver
    driver = webdriver.Chrome(options=chrome_options)
    # Navegar até um site

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]

    )
    return driver, wait

class ProductScraperSpider(scrapy.Spider):
    name = 'vagaspython'
    links_coletados_das_vagas = set()


    def start_requests(self):
        urls = ['https://www.vagas.com.br/vagas-de-python?']
        for url in urls:
            encoded_url = urllib.parse.quote(url, safe=':/?=&')
            yield scrapy.Request(url=encoded_url, callback=self.parse, meta = {'next_url': encoded_url})

    def parse(self, response):
        driver, wait = iniciar_driver()
        driver.get(response.meta['next_url'])
        yield from self.parse_extracao(driver, wait)

    def parse_extracao(self, driver, wait):
        response_webdriver = Selector(text=driver.page_source)

        for vaga in response_webdriver.xpath('//li[@class="vaga odd " or @class="vaga even "]'):
            link_vaga = vaga.xpath('.//a[@class="link-detalhes-vaga"]/@href').get()
            if link_vaga is not None and link_vaga not in self.links_coletados_das_vagas:
                self.links_coletados_das_vagas.add(link_vaga)
                yield{
                    'cargo': vaga.xpath('.//a[@class="link-detalhes-vaga"]/text()').get(),
                    'nome_empresa': vaga.xpath('.//span[@class="emprVaga"]/text()').get(),
                    'local': vaga.xpath('./footer//span[@class="vaga-local"]/text()[2]').get(),
                    'link_vaga': 'https://www.vagas.com.br/vagas-de-python' + link_vaga
                }

        try:
            botao_mostrar_vagas = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//section[@class="grupoDeVagas"]//a[@data-grupo="todasVagas"]'))
                )
            if botao_mostrar_vagas is not None:
                botao_mostrar_vagas.click()
                print('Botao Clicado')
                sleep(10)
                yield from self.parse_extracao(driver, wait)
        except Exception as error:
                print(error)
                print('Chegamos a ultima pagina')
                driver.quit()



