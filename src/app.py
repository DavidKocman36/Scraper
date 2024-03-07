from flask import Flask, render_template
import os
import psycopg2
from scrapy.crawler import CrawlerProcess
from unicodedata import normalize
from scrapy.utils.project import get_project_settings

app = Flask(__name__)

def connect():
    #hostname = 'localhost'
    hostname = 'database'
    username = 'postgres'
    password = '123456'
    database = 'estates'
    return psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

@app.before_request
def init():
    app.before_request_funcs[None].remove(init)

    process = CrawlerProcess(get_project_settings())
    process.crawl("Spider")
    process.start()

@app.route("/")
def hello_world():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM estates")
    estates = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', estates=estates)
 
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8080)