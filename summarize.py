import pymysql
import configparser

config = configparser.ConfigParser()
config.read('dbconfig.ini')

connection = pymysql.connect(host=config['mysqlDB']['host'],
                             user=config['mysqlDB']['user'],
                             password=config['mysqlDB']['pass'],
                             db=config['mysqlDB']['db'])


class summarizeWeatherData:

    def summarize():
        print("-------------Starting to Summarize-------------")
        try:
            cursor = connection.cursor()
            cursor = connection.cursor()
            cursor.execute("call cortevaweather.weatherDataSummary()")
            connection.commit()

        except Exception as e:
            print(e)

        finally:
            # close the database connection using close() method.
            print("-------------Done summarizing-------------")
            connection.close()
