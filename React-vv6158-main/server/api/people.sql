DROP table if EXISTS people CASCADE;

CREATE TABLE people (
    id   SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(30),
    email varchar(30) not null
);


INSERT INTO people(name, email)	
        VALUES ('albert', 'emc2@relative.edu');
INSERT INTO people(name, email)	
        VALUES ('isaac', 'ouch@apple.com');
INSERT INTO people(name, email)	
        VALUES ('leonardo', 'icnivad@code.com');
