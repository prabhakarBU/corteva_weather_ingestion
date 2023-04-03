import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='cortevaweather')


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
