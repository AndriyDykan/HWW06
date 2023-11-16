-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    group_name VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tc_name VARCHAR(255) NOT NULL,
    subject_way VARCHAR(255) NOT NULL
);


-- Table: subjects
DROP TABLE IF EXISTS subjects ;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sb_name VARCHAR(255) NOT NULL,
    mark INTEGER,
    owner_id INTEGER,
    teacher INTEGER,
    time_of_mark DATE,
    FOREIGN KEY (teacher) REFERENCES teachers (id),
    FOREIGN KEY (owner_id) REFERENCES students (id)
    ON DELETE CASCADE
);