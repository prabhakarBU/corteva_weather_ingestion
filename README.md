To run above project:

git clone https://github.com/prabhakarBU/cortevaWeatherIngestion.git

Go the project foler.

Run pip install -r requirements.txt

Run python ingest.py to ingest the raw text files.

Deployment:
Approach 1: ( Cron based )
Could create cron jobs that run in 10 minute intervals ( depending on how often the files are put on the server )
eg. */10 * * * * cd /corteva_weather_ingestion && /usr/bin/python ingest.py > /tmp/ingest.log 2>&1

Approach 2: ( Triggers )
Could use some tool or create another listener that keeps listening and triggers an api call to call 
the ingest function.
Tools that could be used:
-Mage ( a data orchestration tool and also has Api triggers integration )