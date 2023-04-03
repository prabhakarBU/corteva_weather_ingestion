To clone above project:
```git clone https://github.com/prabhakarBU/cortevaWeatherIngestion.git```

Next,go the project folder 'corteva_weather-ingestion'

Create the database:
Run ```Data-Model.sql``` to create the database and the tables required.
Run the **Stored Procedure** ```weatherDataSummary.sql``` that creates the data model to summarize the analyzed data.

Run the following command to install the modules required:
```pip install -r requirements.txt```

Configure your Database:
Update your database details under ``` dbconfig.ini ``` file :
```
[mysqlDB]
host = localhost
db = cortevaweather
user = root
pass = root
```


If you are ingesting hosted files using Apis: ( default for this project )
Add the path to urls under ```urls.json``` under 'urls' node array.
Our ingest function will read those urls.

Run ``` python ingest.py ``` to ingest the raw text files.

Deployment/Scheduling:
Approach 1: ( Cron based )
Could create cron jobs that run in 10 minute intervals ( depending on how often the files are put on the server )
``` eg. */10 * * * * cd /corteva_weather_ingestion && /usr/bin/python ingest.py > /tmp/ingest.log 2>&1 ```

Approach 2: ( Triggers )
Could use some tool or create another listener that keeps listening and triggers an api call to call 
the ingest function.<br/>
Tools that could be used:</br>
-Mage ( a data orchestration tool and also has Api triggers integration )</br>