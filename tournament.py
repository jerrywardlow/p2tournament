#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the specified PostgreSQL database. Returns a database
    connection as well as a cursor with which to perform database operations.
    """
    db_con = psycopg2.connect("dbname=tournament")
    cursor = db_con.cursor()
    return db_con, cursor


def singleExecute(query):
    """A helper function to simplify connecting to a database, opening a
    cursor, and executing a simple query.
    """
    db_con, cursor = connect()
    cursor.execute(query)
    db_con.commit()
    db_con.close()


def deleteMatches():
    """Remove all match records from database."""
    query = ("DELETE FROM matches;")
    singleExecute(query)


def deletePlayers():
    """Remove all player records from database."""
    query = ("DELETE FROM players;")
    singleExecute(query)


def countPlayers():
    """Returns the number of players currently registered."""
    db_con, cursor = connect()
    query = ("SELECT COUNT(player_id) FROM players;")
    cursor.execute(query)
    count = cursor.fetchone()[0]
    db_con.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database. The player's name is sanitized
    before being passed to the SQL query.

    The database assigns a unique serial id number for the player.

    Args:
      name: the player's full name (need not be unique).
    """
    db_con, cursor = connect()
    safe_name = bleach.clean(name)
    query = ("INSERT INTO players(player_id, name) VALUES (default, %s);")
    cursor.execute(query, (safe_name,))
    db_con.commit()
    db_con.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    Returns:
      A list of tuples, each of which contains ("Player ID", "Player Name",
      "Wins", "Matches Played"):
        "Player ID": the player's unique id (assigned by the database)
        "Player Name": the player's full name (as registered)
        "Wins": the number of matches the player has won
        "Matches Played": the number of matches the player has played
    """
    db_con, cursor = connect()
    query = ("SELECT * FROM standings;")
    cursor.execute(query)
    results = cursor.fetchall()
    db_con.close()
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db_con, cursor = connect()
    query = ("INSERT INTO matches(match_id, winner, loser) \
             VALUES (default, %s, %s);")
    cursor.execute(query, (winner, loser,))
    db_con.commit()
    db_con.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    num_players = len(standings)
    pairings = []

    for player in range(0, num_players, 2):
        pair = ((standings[player][0], standings[player][1],
                standings[player + 1][0], standings[player + 1][1]))
        pairings.append(pair)

    return pairings
