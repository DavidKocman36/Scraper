# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
from psycopg2.extras import Json


class RealityscraperPipeline:
    def __init__(self):
        hostname = 'localhost'
        username = 'postgres'
        password = '123456'
        database = 'estates'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        
        self.cur = self.connection.cursor()
        
        self.cur.execute("""
        DROP TABLE IF EXISTS estates;
        CREATE TABLE IF NOT EXISTS estates(
            id serial PRIMARY KEY, 
            name text,
            images json     
        )
        """)

    def process_item(self, item, spider):
        sql = "insert into estates (name, images) values (%s,%s)"
        self.cur.execute(sql, (item["name"], Json(item["images"])))

        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

