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

## OBS:

Lembrar sempre de estar na pasta certa e dentro do ambiente virtual scrapy para rodar a aplicação

Exemplo

```bash
cd 'C:\Users\Usuario\Desktop\Projetos Github\varredor-de-vagas-python\Varredor-vagas-python\projeto-scrapy\varredor_de_sites'

.\scrapy\Scripts\activate
```

## Exportação de Dados com Pipeline para Excel

Este projeto utiliza uma pipeline personalizada para exportar automaticamente os dados coletados pela spider para uma planilha no formato .xlsx, facilitando a visualização e análise dos resultados em softwares como Excel ou Google Sheets.

## Tecnologias utilizadas

- openpyxl: biblioteca responsável pela criação e manipulação da planilha Excel.

- itemadapter: permite acessar os campos do item de forma padronizada, independentemente do tipo de objeto retornado pela spider (por exemplo, dict ou Item do Scrapy).

## Vantagens

Não é necessário utilizar a opção -O arquivo.csv na execução da spider, pois os dados são salvos automaticamente em uma planilha .xlsx.

## Configuração

O caminho do arquivo Excel é definido em settings.py através da constante XLSX_PATH, permitindo manter um local padrão para a saída da planilha. A pipeline também é registrada no settings.py, centralizando a configuração e evitando a necessidade de alteração na spider.