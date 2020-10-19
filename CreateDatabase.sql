DROP DATABASE IF EXISTS library;

CREATE DATABASE library;
USE library;

CREATE TABLE books(
    book_id VARCHAR(6) PRIMARY KEY,
    title VARCHAR(20),
    author VARCHAR(20),
    status VARCHAR(2)
);

CREATE TABLE issued_books(
    book_id VARCHAR(6) PRIMARY KEY,
    issued_to VARCHAR(20),
    FOREIGN KEY(book_id) REFERENCES books
);