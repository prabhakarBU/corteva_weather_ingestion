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

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='cortevaweather')

urls = [
    'https://raw.githubusercontent.com/corteva/code-challenge-template/main/wx_data/USC00110072.txt',
    'https://raw.githubusercontent.com/corteva/code-challenge-template/main/wx_data/USC00110187.txt',
    'https://raw.githubusercontent.com/corteva/code-challenge-template/main/wx_data/USC00110338.txt',
    'https://raw.githubusercontent.com/corteva/code-challenge-template/main/wx_data/USC00111280.txt',
    'https://raw.githubusercontent.com/corteva/code-challenge-template/main/wx_data/USC00111436.txt',
    'https://raw.githubusercontent.com/corteva/code-challenge-template/main/wx_data/USC00112140.txt',
    'https://raw.githubusercontent.com/corteva/code-challenge-template/main/wx_data/USC00112193.txt',
    'https://raw.githubusercontent.com/corteva/code-challenge-template/main/wx_data/USC00112348.txt',
    'https://raw.githubusercontent.com/corteva/code-challenge-template/main/wx_data/USC00112483.txt',
    ]

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
            print(parsefileurl.path)
            print(os.path.basename(parsefileurl.path))
            filename = os.path.basename(parsefileurl.path)[0:os.path.basename(parsefileurl.path).index('.')]
            print (filename)
            cursor = connection.cursor()
            inserted = 0
            for line in range(len(df)):
                # print(df.iloc[line, 0], df.iloc[line, 1],df.iloc[line, 2],df.iloc[line, 3])
                sql = "INSERT IGNORE INTO weatherData (origin, weatherdate, maxtemp, mintemp, precipitation) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql,(filename,df.iloc[line, 0], df.iloc[line, 1],df.iloc[line, 2],df.iloc[line, 3]))
                connection.commit()
                inserted+=cursor.rowcount
                # connection.close()
            
            print ("Ended Ingesting date and time : ")
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("Total records consumed = {}".format(inserted))

    except Exception as e:
        print(e)

    finally:
        # close the database connection using close() method.
        connection.close()
    
def main():
    # ingest(urls)
    summarize.summarizeWeatherData.summarize()



if __name__ == "__main__":
    main()
