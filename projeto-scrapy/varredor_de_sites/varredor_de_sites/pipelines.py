# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
'''from itemadapter import ItemAdapter


class VarredorDeSitesPipeline:
    def process_item(self, item, spider):
        return item'''


from itemadapter import ItemAdapter
import openpyxl
import openpyxl.workbook
from varredor_de_sites.settings import XLSX_PATH
campos = ['cargo', 'nome_empresa', 'local', 'link_vaga']

class VarredorXLSX(object):
    planilha = None
    sheet = None

    def open_spider(self, spider):
        self.planilha = openpyxl.Workbook()
        self.sheet = self.planilha.active
        self.sheet.append(campos)
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.sheet.append([adapter.get(campo) for campo in campos])
        return item
    def close_spider(self, spider):
        self.planilha.save(XLSX_PATH)

