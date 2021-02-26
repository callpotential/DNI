CREATE TABLE IF NOT EXISTS  ReplacementNumberMap (
	replacementphonenumber VARCHAR(250),
    routingnumber VARCHAR(250),
	poolid INT
);

CREATE TABLE IF NOT EXISTS  SessionInformationLog (
		sessionid INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        poolid INT,
        businessid INT,
        numberroutedsuccessfully BOOLEAN,
        replacementphonenumber VARCHAR(250),
        routingnumber VARCHAR(250),
        poolphonenumber VARCHAR(250),
        ttl DATETIME,
        callstart DATETIME,
        callend DATETIME,
        clickid TEXT,
        clicksource  VARCHAR(250),
        url TEXT
);

CREATE TABLE IF NOT EXISTS  BusinessConfig (
		businessid INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        active BOOLEAN,
        cpmaincustomer BOOLEAN, 
        defaultttl INT, 
        emailnotifications BOOLEAN, 
        emailaddress VARCHAR(250),
        featuretoggle TEXT
);

CREATE TABLE IF NOT EXISTS  AssignmentPool (
	poolid INT,
	businessid INT,
    poolphonenumber VARCHAR(250),
    ttl DATETIME,
    assignedroutingnumber VARCHAR(250),
	sessionid INT
);

