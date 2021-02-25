INSERT INTO `dni`.`assignmentpool` (`businessid`,`poolphonenumber`,`ttl`,`assignedroutingnumber`,`sessionid`)
VALUES(1290390360,"234-223-4001",now(),"234-223-4011",1);
INSERT INTO `dni`.`assignmentpool` (`businessid`,`poolphonenumber`,`ttl`,`assignedroutingnumber`,`sessionid`)
VALUES(1290390360,"234-223-4002",now(),"234-223-4011",1);
INSERT INTO `dni`.`assignmentpool` (`businessid`,`poolphonenumber`,`ttl`,`assignedroutingnumber`,`sessionid`)
VALUES(1290390360,"234-223-4003",now(),"234-223-4011",1);
INSERT INTO `dni`.`assignmentpool` (`businessid`,`poolphonenumber`,`ttl`,`assignedroutingnumber`,`sessionid`)
VALUES(1290390360,"234-223-4004",now(),"234-223-4011",1);
INSERT INTO `dni`.`assignmentpool` (`businessid`,`poolphonenumber`,`ttl`,`assignedroutingnumber`,`sessionid`)
VALUES(1290390360,"234-223-4005",now(),"234-223-4011",1);
SELECT * FROM dni.assignmentpool;

INSERT INTO `dni`.`businessconfig` (`businessid`,`active`,`cpmaincustomer`,`defaultttl`,`emailnotifications`,`emailaddress`,`featuretoggle`)
VALUES(1290390360,True,True,120,True,"abusiness@business.com",null);
SELECT * FROM dni.businessconfig;

INSERT INTO `dni`.`replacementnumbermap` (`replacementphonenumber`, `routingnumber`, `businessid`)
VALUES ("234-123-4323", "234-223-4011", 1290390360);
SELECT * FROM dni.replacementnumbermap;

INSERT INTO `dni`.`sessioninformationlog`
(`sessionid`,`businessid`,`numberroutedsuccessfully`,`replacementphonenumber`,`routingnumber`,
`poolphonenumber`,`ttl`,`callstart`,`callend`,`clickid`,`clicksource`,`url`)
VALUES (1,1290390360,True,"234-123-4323","234-223-4011","234-223-4001",DATE_ADD(now(),interval 2 hour),NULL,NULL, 
"?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2Bsmart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB","Google",
"https://www.cubesmart.com/illinois-self-storage/chicago-self-storage/?utm_source=google&utm_medium=cpc&utm_campaign=G_IL_Chicago_Brand_BMM&utm_adgroup=CubeSmart_Core+Brand&utm_keyword=%2Bsmart%20%2Bcube%20%2Bstorage&utm_device=m&utm_brandtype=Brand&gclsrc=aw.ds&&gclid=Cj0KCQiAj9iBBhCJARIsAE9qRtCMZfs_I3sK0nm4J6wC9hmDFahTbCWy3pwi453o_cfTaWCvcK2PRKcaArn5EALw_wcB");


