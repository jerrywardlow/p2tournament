# Project 2 - Swiss Tournament Database
Udacity - Full Stack - Project 2 - Tournament Database

By Jerry Wardlow for the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

### About

This project implements a PostgreSQL database to keep track of players and matches during a [Swiss Tournament](https://en.wikipedia.org/wiki/Swiss-system_tournament). Interaction with the PostgreSQL database is done via a simple Python module.

### In This Repository

The project consists of two files, a Python module (tournament.py) and a PostgreSQL database file (tournament.sql). In addition, there is a Python module which can be used to test the functionality of this project (tournament_test.py).

### Using This Project

**Prerequisites in a Linux Environment:**

* Python 2.7.x
* Psycopg2 (Python Library)
* Bleach (Python Library)
* Installation and configuration of PostgreSQL 9.x

**Running and Testing This Project**

Loading the tournament.sql file into your PostgreSQL database server will initialize the necessary database and tables for the Swiss Tournament. After the database has been initialized, the functionality of the tournament.py module can be tested by running the tournament_test.py module in Python 2.7.x. 