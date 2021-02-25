CREATE TABLE IF NOT EXISTS  ReplacementNumberMap (
	replacementphonenumber VARCHAR(250),
    routingnumber VARCHAR(250),
	businessid INT(10)
);

CREATE TABLE IF NOT EXISTS  SessionInformationLog (
		sessionid INT(20) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        businessid INT(10),
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
		businessid INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        active BOOLEAN,
        cpmaincustomer BOOLEAN, 
        defaultttl INT(10), 
        emailnotifications BOOLEAN, 
        emailaddress VARCHAR(250),
        featuretoggle TEXT
);

CREATE TABLE IF NOT EXISTS  AssignmentPool (
	businessid INT(10),
    poolphonenumber VARCHAR(250),
    ttl DATETIME,
    assignedroutingnumber VARCHAR(250),
	sessionid INT(20)
);

