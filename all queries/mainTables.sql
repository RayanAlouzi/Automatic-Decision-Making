DROP TABLE IF EXISTS users;


CREATE TABLE users (
    uid CHAR(15) NOT NULL,
    name TEXT, 
    pwd TEXT, 
    age INT,
    primary key (uid)
);

CREATE TABLE decisionMade(
    uid CHAR(15) NOT NULL,
    did char(5) NOT NULL,
    decisiontype text, 
    primary key (uid,did)
);
