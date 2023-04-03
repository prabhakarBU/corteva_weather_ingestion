DELIMITER $$
DROP PROCEDURE IF EXISTS cortevaweather.weatherDataSummary;

CREATE PROCEDURE cortevaweather.weatherDataSummary()
BEGIN

	INSERT IGNORE INTO cortevaweather.weatherDataSummary
	SELECT origin,year(weatherdate) as weatheryear,
		avg(CASE WHEN maxtemp != -9999 THEN maxtemp ELSE 0 END),
		avg(CASE WHEN mintemp != -9999 THEN mintemp ELSE 0 END),
		sum(CASE WHEN precipitation != -9999 THEN precipitation ELSE 0 END) 
		from cortevaweather.weatherData
		group by 1,2;
    
END$$

DELIMITER ;