CREATE TABLE IF NOT EXISTS  ReplacementNumberMap (
	replacementphonenumber VARCHAR(12),
    routingnumber VARCHAR(12),
	businessid INT(10)
);

CREATE TABLE IF NOT EXISTS  SessionInformationLog (
		sessionid INT(20) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        businessid INT(10),
        poolid INT(10),
        numberroutedsuccessfully BOOLEAN,
        replacementphonenumber VARCHAR(12),
        routingnumber VARCHAR(12),
        poolphonenumber VARCHAR(12),
        ttl DATETIME,
        call_start DATETIME,
        call_end DATETIME,
        clickid TEXT,
        clicksource  VARCHAR(250),
        url TEXT
);

CREATE TABLE IF NOT EXISTS  BusinessConfig (
		businessid INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        cpmaincustomer BOOLEAN, 
        defaultttl BOOLEAN, 
        emailnotifications BOOLEAN, 
        emailaddress VARCHAR(250),
        featuretoggle TEXT
);

CREATE TABLE IF NOT EXISTS  AssignmentPool (
	businessid INT(10),
    poolphonenumber VARCHAR(12),
    ttl DATETIME,
    assignedroutingnumber VARCHAR(12),
	sessionid INT(20)
)

