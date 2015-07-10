# Project 2 - Swiss Tournament Database
Udacity - Full Stack - Project 2 - Tournament Database

By Jerry Wardlow for the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

### About

This project implements a PostgreSQL database to keep track of players and matches during a [Swiss Tournament](https://en.wikipedia.org/wiki/Swiss-system_tournament). Interaction with the PostgreSQL database is done via a simple Python module.

### In This Repository

The project consists of two files, a Python module (`tournament.py`) and a PostgreSQL database file (`tournament.sql`). In addition, there is a Python module which can be used to test the functionality of this project (`tournament_test.py`).

### Using This Project

**Prerequisites in a Linux Environment:**

* Python 2.7.x
* Psycopg2 (Python Library)
* Bleach (Python Library)
* PostgreSQL 9.x
* The files contained in this repository

**Running and Testing This Project**

From a command line, first change into the directory where the project files are stored. (For this example, we will assume they are in `/home/user/Tournament`)

- `cd /home/user/Tournament`

Now that we are in the correct directory, we can open PostgreSQL and load the `tournament.sql` file, which will automatically create the database (after dropping if it already exists) and generate the tables necessary for the project to run before connecting to the newly created database:

- `psql`
- `\i tournament.sql`

Upon succesful initialization and connection, we can exit PostgreSQL

- `\q`

Now that we have generated our `tournament` PostgreSQL database, we can test the functionality of our `tournament.py` module using `tournament_test.py`. From the command line, we will run the `tournament_test.py` module which will start an automated process that checks the functionality of `tournament.py` against our `tournament` database.

- `python tournament_test.py`

This will produce a wonderful success message letting us know that we actually understand what we are doing.

`1. Old matches can be deleted.`
`2. Player records can be deleted.`
`3. After deleting, countPlayers() returns zero.`
`4. After registering a player, countPlayers() returns 1.`
`5. Players can be registered and deleted.`
`6. Newly registered players appear in the standings with no matches.`
`7. After a match, players have updated standings.`
`8. After one match, players with one win are paired.`
`Success!  All tests pass!`