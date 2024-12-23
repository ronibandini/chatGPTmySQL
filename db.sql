-- Creating the main students table with camelCase
CREATE TABLE students (
    idStudent INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    country VARCHAR(100),
    age INT,
    lead TEXT,
    skills TEXT,
    confirmed BOOLEAN
);

-- Creating the nested course table with camelCase
CREATE TABLE course (
    idCourse INT AUTO_INCREMENT PRIMARY KEY,
    idStudent INT,
    courseName VARCHAR(100),
    courseDate DATE,
    courseAmount DECIMAL(10, 2),
    coursePaymentMethod VARCHAR(50),
    FOREIGN KEY (idStudent) REFERENCES students(idStudent)
);