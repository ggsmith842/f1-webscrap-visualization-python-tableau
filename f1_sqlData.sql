CREATE DATABASE formula1;

use formula1;

CREATE TABLE results(
 resultId DOUBLE,
 raceId DOUBLE,
 driverId DOUBLE,
 position DOUBLE,
 positionText VARCHAR(255),
 primary key(resultId)
);

LOAD DATA LOCAL INFILE 'C:/Users/grant/OneDrive/Documents/f1_analysis/condensed_results.csv'
INTO TABLE results FIELDS terminated by ','
LINES terminated by '\n' IGNORE 1 ROWS
(resultId,raceId,driverId,position,positionText);

CREATE TABLE constructors(
	constructorId DOUBLE,
    constructorRef VARCHAR(255),
    name VARCHAR(255),
    nationality varchar(255),
    url VARCHAR(255),
    X6 varchar(255)
    );
    
LOAD DATA LOCAL INFILE 'C:/Users/grant/OneDrive/Documents/f1_analysis/constructors.csv'
INTO TABLE constructors FIELDS terminated by ','
LINES terminated by '\n' IGNORE 1 ROWS
(constructorId,constructorRef,name,nationality,url,X6);

CREATE TABLE constructor_standings(
	constructorStandingsId double,
    raceId double,
    constructorId double,
    points double,
    position double,
    positionText VARCHAR(255),
    wins double,
    X8 varchar(255),
    primary key (constructorStandingsId)    
    );
    
LOAD DATA LOCAL INFILE 'C:/Users/grant/OneDrive/Documents/f1_analysis/constructorStandings.csv'
INTO TABLE constructor_standings FIELDS terminated by ','
LINES terminated by '\n' IGNORE 1 ROWS
(constructorStandingsId,raceId,constructorId,points,position,positionText,wins,X8);


CREATE TABLE condensed_constructor AS
SELECT name,nationality,wins FROM constructors
LEFT JOIN constructor_standings ON constructors.constructorId=constructor_standings.constructorId;

