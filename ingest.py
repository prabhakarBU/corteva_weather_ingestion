import urllib.request
import requests
from urllib.parse import urlparse
from urllib.request import urlopen
import urllib
import pandas as pd
import pymysql
import datetime
import os
import summarize
import json
import configparser

config = configparser.ConfigParser()
config.read('dbconfig.ini')

print('config read----')
print(config['mysqlDB']['host'])
print('localhost')

connection = pymysql.connect(host=config['mysqlDB']['host'],
                             user=config['mysqlDB']['user'],
                             password=config['mysqlDB']['pass'],
                             db=config['mysqlDB']['db'])

with open("urls.json", "r", encoding="utf8") as file_object:
    urls = json.load(file_object)

def ingest(files):
    try:
        for file in files:
            print ("Started Ingesting date and time : ")
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            # data = urlopen(file)
            # data.split("\n")
            df = pd.read_table(file, skiprows=0, header=None, sep='\t')
            # df.to_sql('weatherData', connection, if_exists='append', dtype={
            # 'origin': object,
            # 'weatherdate': object,
            # 'maxtemp': int,
            # 'mintemp': int,'precipitation':int})
            # print(df)
            parsefileurl = urlparse(file)
            # print(parsefileurl.path)
            # print(os.path.basename(parsefileurl.path))
            filename = os.path.basename(parsefileurl.path)[0:os.path.basename(parsefileurl.path).index('.')]
            # print (filename)
            cursor = connection.cursor()
            inserted = 0
            for line in range(len(df)):
                # print(df.iloc[line, 0], df.iloc[line, 1],df.iloc[line, 2],df.iloc[line, 3])
                sql = "INSERT IGNORE INTO weatherData (origin, weatherdate, maxtemp, mintemp, precipitation) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql,(filename,df.iloc[line, 0], df.iloc[line, 1],df.iloc[line, 2],df.iloc[line, 3]))
                connection.commit()
                inserted+=cursor.rowcount
            
            print ("Ended Ingesting date and time : ")
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("Total records consumed = {}".format(inserted))

    except Exception as e:
        print(e)

    finally:
        connection.close()
    
def main():
    ingest(urls['urls'])
    summarize.summarizeWeatherData.summarize()



if __name__ == "__main__":
    main()