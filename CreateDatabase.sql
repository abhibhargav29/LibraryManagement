DROP DATABASE IF EXISTS library;

CREATE DATABASE library;
USE library;

CREATE TABLE books(
    book_id VARCHAR(6) PRIMARY KEY,
    title VARCHAR(30),
    author VARCHAR(50),
    status VARCHAR(2)
);

CREATE TABLE issued_books(
    book_id VARCHAR(6) PRIMARY KEY,
    issued_to VARCHAR(8) NOT NULL,
    issue_date VARCHAR(10) NOT NULL,
    FOREIGN KEY(book_id) REFERENCES books(book_id)
);
