# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from datetime import datetime
import codecs
from pathlib import Path

class SaveDataJsonPipeline:
    def process_item(self, item, spider):

        fileName = datetime.strptime(item['date_data'], "%d.%m.%Y+%H:%M").strftime(format="%m%d%Y") + '.json'
        Path(f"Data").mkdir(exist_ok=True)
        folder_name = "Data/" + str(datetime.strptime(item['date_data'], '%d.%m.%Y+%H:%M').year)
        Path(folder_name).mkdir(exist_ok=True)
        try:
            with open('/'.join([folder_name, fileName]),'w') as fp:
                json.dump(list(item['char_data']),fp)
                return item
        except Exception as e:
            print(type(e))
            print(str(e))
            raise

class FormatJSONToDataFrame:
    pass
    
