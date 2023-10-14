	
-- Delete schema if it exists
DROP SCHEMA simple_schema CASCADE;

-- Create a schema 
CREATE SCHEMA simple_schema;

-- Set Path
SET search_path TO simple_schema;

-- Create a table for general users
CREATE TABLE generic_user (
	username VARCHAR(255) PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
	firstname VARCHAR(255) NOT NULL,
	lastname VARCHAR(255) NOT NULL,
	background VARCHAR(255),
	CONSTRAINT chk_background CHECK (background = 'student' OR background = 'mentor')
    
);

-- Create a table specifically for student users
CREATE TABLE student (
	username VARCHAR(255) PRIMARY KEY,
    interest VARCHAR(255) NOT NULL,
	FOREIGN KEY (username) REFERENCES generic_user(username)
);

-- Create a table specifically for research mentor users
CREATE TABLE mentor (
	username VARCHAR(255) PRIMARY KEY,
	biography VARCHAR(255) NOT NULL,
    subject VARCHAR(255) NOT NULL,
	FOREIGN KEY (username) REFERENCES generic_user(username)
);


-- Create a table specifically for lab information
CREATE TABLE lab (
	labID VARCHAR(5) PRIMARY KEY,
    subject VARCHAR(255) NOT NULL,
	labname VARCHAR(255) NOT NULL,
	mentor VARCHAR(255) NOT NULL,
	FOREIGN KEY (mentor) REFERENCES mentor(username)
	
);

-- Create a table specifically for individual research opportunities
CREATE TABLE opportunity (
	oppID VARCHAR(5),
    subject VARCHAR(255) NOT NULL,
	description VARCHAR(255) NOT NULL,
	mentor VARCHAR(255) NOT NULL,
	PRIMARY KEY (oppId, mentor),
	FOREIGN KEY (mentor) REFERENCES mentor(username)
);



-- Privilege Management
GRANT ALL PRIVILEGES ON DATABASE research_match TO postgres;
GRANT ALL PRIVILEGES ON SCHEMA simple_schema TO postgres;
-- GRANT ALL PRIVILEGES ON TABLE research_match.users TO postgres;	
