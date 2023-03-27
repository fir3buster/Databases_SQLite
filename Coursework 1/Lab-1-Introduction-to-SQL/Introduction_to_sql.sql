?

DELETE FROM pet;
INSERT INTO pet (name,owner,species,sex,checkups,birth,death)
VALUES
('Fluffy','Harold','cat','f',5,'2001-02-04',NULL),
('Claws','Gwen','cat','m',2,'2000-03-17',NULL),
('Buffy','Harold','dog','f',7,'1999-05-13',NULL),
('Fang','Benny','dog','m',4,'2000-08-27',NULL),
('Bowser','Diane','dog','m',8,'1998-08-31','2001-07-29'),
('Chirpy','Gwen','bird','f',0,'2002-09-11',NULL),
('Whistler','Gwen','bird','',1,'2001-12-09',NULL),
('Slim','Benny','snake','m',5,'2001-04-29',NULL);

.mode column
.headers on
.separator ROW "\n"
.nullvalue NULL

-- running the whole table to make sure that it is working
.print "Table"
.print
SELECT * FROM pet;

-- Q1-1. Query the names of owners and thier pet's name for all pets who are female.
.print 
.print "Q1-1. Query The names of owners and their pet's name for all pets who are female"
.print
SELECT owner, name 
FROM pet 
WHERE sex = "f";

-- Q1-2. Query the names and birth dates of pets which are dogs.
.print 
.print "Q1-2. Query the names and birth dates of pets which are dogs"
.print
SELECT name, birth 
FROM pet 
WHERE species = "dog";

-- Q1-3. Query the names of the owners of birds.
.print
.print "Q1-3. Query the names of the owners of birds"
.print
SELECT owner 
FROM pet 
WHERE species = "bird";

-- Q1-4. Query the species of pets who are female.
.print
.print "Q1-4. Query the species of pets who are female"
.print
SELECT species 
FROM pet 
WHERE sex = "f";

-- Q1-5. Query the names and birth dates of pets which are cats or birds.
.print
.print "Q1-5. Query the names and birth dates of pets which are cats or birds"
.print
SELECT name, birth 
FROM pet 
WHERE species = "cat" OR species = "bird";

-- Q1-6. Query the names and species of pets which are cats or birds and which are female
.print
.print "Q1-6. Query the names and species of pets which are cats or birds and which are female"
.print
SELECT name, species 
FROM pet 
WHERE species IN ("cat", "bird") and sex = "f";


-- Q2-1. Query the names of owners and their pets where the pet's name ends with "er" or "all"
.print
.print "Q2-1. Query the names of owners and their pets where the pet's name ends with 'er' or 'all'"
.print
SELECT owner, name 
FROM pet 
WHERE (name LIKE "%er" OR "%all");

-- Q2-2. Query the the names of any pets whose owner's name contains an "e"
.print
.print "Q2-2. Query the the names of any pets whose owner's name contains an 'e'"
.print
SELECT name 
FROM pet 
WHERE owner LIKE "%e%";

-- Q2-3. Query the names of all pets whose name does not end with "fy"
.print
.print "Q2-3. Query the names of all pets whose name does not end with 'fy'"
.print
SELECT name 
FROM pet 
WHERE name NOT LIKE "%fy";

-- Q2-4. Query all pet names whose owners name is only four characters long
.print
.print "Q2-4. Query all pet names whose owners name is only four characters long"
.print
SELECT name 
FROM pet 
WHERE LENGTH(owner) = 4;

-- Q2-5. Query all owners whose names begin and end with one of the first five letters of the alphabet
.print
.print "Q2-5. Query all owners whose names begin and end with one of the first five letters of the alphabet"
.print
SELECT owner 
FROM pet 
WHERE SUBSTR(owner,1,1) IN ("A", "B", "C", "D", "E")AND SUBSTR(owner,-1,1) IN ("a", "b", "c", "d", "e");

-- Q2-6. Repeat previous query sensitive to the case letters of the alphabet the characters in the name
.print
.print "Q2-6. Repeat previous query sensitive to the case letters of the alphabet the characters in the name"
.print
SELECT owner
FROM pet
WHERE LOWER(SUBSTR(owner,1,1)) IN ("a", "b", "c", "d", "e")
AND UPPER(SUBSTR(owner,-1,1)) IN ("A", "B", "C", "D", "E");

-- Q3-1. Query the average number of check-ups that each owner has made with their pets
.print
.print "Q3-1. Query the average number of check-ups that each owner has made with their pets"
.print
SELECT owner, avg(checkups) AS avg_checkups
FROM pet
GROUP BY owner;

-- Q3-2. Query the number of pets of each species in ascending order
.print
.print "Q3-2. Query the number of pets of each species in ascending order"
.print
SELECT species, COUNT(species) AS number_of_species
FROM pet
GROUP BY species
ORDER BY number_of_species;

-- Q3-3. Query the number of pets of each species that each owner has
.print
.print "Q3-3. Query the number of pets of each species that each owner has"
.print
SELECT owner, species, COUNT(species) AS number_of_species
FROM pet
GROUP BY owner, species;

-- Q3-4. Query the number of distinct species of pet each owner has
.print
.print "Q3-4. Query the number of distinct species of pet each owner has"
.print
SELECT owner, COUNT(distinct(species)) AS number_of_distinct_species
FROM pet
GROUP BY owner;

-- Q3-5. Query the number of pets of each gender there are in database, where the gender is known
.print
.print "Q3-5. Query the number of pets of each gender there are in database, where the gender is known"
.print
SELECT sex, COUNT(sex) AS number_of_pets_gender
FROM pet
WHERE sex <> ""
GROUP BY sex;

-- Q3-6. Query the number of birds each owner has
.print
.print "Q3-6. Query the number of birds each owner has"
.print
SELECT owner, count(species) AS number_of_bird
FROM pet
WHERE species == "bird"
GROUP BY owner;

-- Q3-7. Query the total number of check-ups each owner has made with all their pets
.print
.print "Q3-7. Query the total number of check-ups each owner has made with all their pets"
.print
SELECT owner, sum(checkups) AS total_checkups
FROM pet
GROUP BY owner;