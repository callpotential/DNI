CREATE TABLE IF NOT EXISTS  ReplacementNumberMap (
	replacementphonenumber VARCHAR(250),
    routingnumber VARCHAR(250),
	poolid INT
);

CREATE TABLE IF NOT EXISTS  SessionInformationLog (
		sessionid INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        poolid INT,
        businessid INT,
        numberroutedsuccessfully VARCHAR(250),
        replacementphonenumber VARCHAR(250),
        routingnumber VARCHAR(250),
        poolphonenumber VARCHAR(250),
        callstart DATETIME,
        callend DATETIME,
        clicksource  VARCHAR(250),
        url TEXT,
		utm_source VARCHAR(250),
        utm_medium VARCHAR(250),
        utm_campaign VARCHAR(250),
        utm_adgroup VARCHAR(250),
        utm_keyword VARCHAR(250),
        utm_device VARCHAR(250),
        utm_brandtype VARCHAR(250),
        utm_content VARCHAR(250),
        gclsrc VARCHAR(250),
        gclid VARCHAR(250),
        fbclid VARCHAR(250),
        clickid VARCHAR(250)
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

