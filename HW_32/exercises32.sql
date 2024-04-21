-- Active: 1712672983994@@127.0.0.1@3306@it_step_db

-- 1. დაწერეთ SQL რომელიც შექმნის Author ცხრილს, რომელსაც ექნება პირველადი გასაღები
CREATE TABLE AUTHOR (
    AuthorID INT PRIMARY KEY,
    AuthorName VARCHAR(100)
);

-- 2. დაწერეთ SQL რომელიც შექმნის Books ცხრილს, სადაც გექნებათ მეორადი გასაღები AuthorID 
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(200),
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES AUTHOR(AuthorID)
);

-- 3. დაწერეთ SQL Author და Books ცხრილებისთვის სადაც შექმნით მინიმუმ 5 ჩანაწერს

INSERT INTO AUTHOR (AuthorID, AuthorName) 
VALUES (1, 'Ilia Chavchavadze');

INSERT INTO AUTHOR (AuthorID, AuthorName) 
VALUES (2, 'Akaki Tsereteli');

INSERT INTO AUTHOR (AuthorID, AuthorName) 
VALUES (3, 'Vazha-Pshavela');

INSERT INTO AUTHOR (AuthorID, AuthorName) 
VALUES (4, 'Galaktion Tabidze');

INSERT INTO AUTHOR (AuthorID, AuthorName) 
VALUES (5, 'Nikoloz Baratashvili');


-- 4. დაწერეთ SQL Books ცხრილისთვის სადაც გამოიყენებთ update ბრძანებას და გაანახლებთ კონკრეტულ ჩანაწერის ერთ-ერთ ველის მნიშვნელობას
UPDATE Books SET Title = 'New Title' WHERE BookID = 1;

-- 5. წაშალეთ ყველა ჩანაწერი Author და Books ცხრილიდან

DELETE FROM AUTHOR;
DELETE FROM Books;

-- 6. წაშალეთ Author და Books ცხრილები
DROP TABLE AUTHOR;
DROP TABLE Books;
