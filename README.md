# Varredor-vagas-python
Este projeto é um varredor de dados, mais especificamente de vagas python onde as informações são retiradas do site Indeed, utilizando scrapy e selenium para fazer a extração dos campos desejados.

## Requisitos

Certifique-se de ter o Python instalado em seu ambiente. Para este projeto, utilizamos as seguintes bibliotecas:

- Scrapy: Framework de scraping.

- Selenium: Para interação com o site via WebDriver.

- WebDriver: Usado pelo Selenium para controlar o navegador.

- ScrapeOps: Middleware para proxies e proteção contra fake user agents (não está explicitamente configurado no código, mas pode ser integrado se necessário).

## Dependências
Antes de rodar o projeto, instale as dependências necessárias executando:

```bash
pip install -r requirements.txt
```

## Como Usar
Para iniciar o projeto, execute o comando abaixo para rodar a spider que fará o scraping das vagas de emprego:

```bash
scrapy crawl "nome da spider" -O arquivo.csv
```
Neste caso o nome da Spider seria vagaspython

O tipo de arquivo pode ser de sua preferência como .csv ou .json etc...