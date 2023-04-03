CREATE DATABASE cortevaweather;

CREATE TABLE cortevaweather.weatherData (
 origin varchar(255) not null,
 weatherdate date not null,
 maxtemp int not null,
 mintemp int not null,
 precipitation int default 0,
 primary key (origin, weatherdate)
);

CREATE TABLE cortevaweather.weatherDataSummary (
 stationId varchar(255) not null,
 year smallint not null,
 averageMaxTemp FLOAT default 0,
 averageMinTemp FLOAT default 0,
 totalPrecipitation FLOAT default 0,
 primary key (stationId, year)
);