# Library Management System

Requirements: MySQL installed and configured, tkinter, python3, pymysql, pillow.

Create Database sql script needs to be run in MySQL workbench before any other file, it will create our database and tables
with the necessary relations between them. There are two tables, books and issued_books. The book_id attribute acts as the foreign key for books_issued 
and primary key for books. The database will be stored by the name of "library", if a pre-existing database by same name exists, the sql script will delete it.

Main Window is the first and main session of the system. Before starting it asks for password, this is the password foe your localhost connection of mysql thet
you filled while installing mysql. Then the gui window opens with various button, each of which will open the corresponding window on clicking.

lib.png is our background image. 
