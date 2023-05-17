-- Create the candidate table
CREATE TABLE candidate (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(50),
  role VARCHAR(50),
  education VARCHAR(50)
);

-- Insert some sample data into the candidate table
INSERT INTO candidate (id, name, role, education)
VALUES (1, 'John Smith', 'Developer', 'Computer Science'),
       (2, 'Jane Doe', 'Designer', 'Graphic Design');

-- Create the certificate table
CREATE TABLE certificate (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(50),
  fee DECIMAL(8, 2)
);

-- Insert some sample data into the certificate table
INSERT INTO certificate (id, name, fee)
VALUES (1, 'Oracle Certified Professional Java SE 11 Developer', 245),
       (2, 'AWS Certified Solutions Architect - Associate', 150);

-- Create the candidate_certificates table
CREATE TABLE candidate_certificates (
  candidate_id INT NOT NULL,
  certificate_id INT NOT NULL,
  on_date DATE,
  PRIMARY KEY (candidate_id, certificate_id),
  FOREIGN KEY (candidate_id) REFERENCES candidate(id),
  FOREIGN KEY (certificate_id) REFERENCES certificate(id)
);

-- Insert some sample data into the candidate_certificates table
INSERT INTO candidate_certificates (candidate_id, certificate_id, on_date)
VALUES (1, 1, '2022-01-01'),
       (1, 2, '2022-02-01'),
       (2, 2, '2022-03-01');

-- Create the skillset table
CREATE TABLE skillset (
  id INT NOT NULL PRIMARY KEY,
  skill_name VARCHAR(50)
  proficiency_level VARCHAR(30)
);

-- Insert some sample data into the skillset table
INSERT INTO skillset (id, skill_name, proficiency_level)
VALUES (123, 'Java', 'Intermediate'),
    	 (456, 'HTML', 'Advanced'),
       (789, 'Photoshop', 'Advanced'),
       (213, 'Illustrator', 'Intermediate'),
       (546, 'Data Analysis', 'Advanced'),
       (879, 'AWS', 'Intermediate'),
       (321, 'Python', 'Advanced');

-- Create the candidate_skillset table
CREATE TABLE candidate_skillset (
  candidate_id INT NOT NULL,
  skillset_id INT NOT NULL,
  years_experience INT,
  last_used DATE,
  PRIMARY KEY (candidate_id, skill_id),
  FOREIGN KEY (candidate_id) REFERENCES candidate(id),
  FOREIGN KEY (skill_id) REFERENCES skill(id)
);

-- Insert some sample data into the candidate_skillset table
INSERT INTO candidate_certificates (candidate_id, skillset_id, years_experience, last_used)
VALUES (1, 123, 3, '2023-01-16'),
    	 (2, 456, 4, '2022-09-21'),
       (3, 789, 2, '2023-02-03'),
       (4, 213, 5, '2022-10-17'),
       (5, 546, 3, '2023-03-20'),
       (6, 879, 4, '2022-12-09'),
       (7, 321, 3, '2023-04-25');




