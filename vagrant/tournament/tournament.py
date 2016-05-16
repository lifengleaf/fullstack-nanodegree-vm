#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connects to the PostgreSQL database.
    Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Removes all the match records from the database."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE game SET wins=0, matches=0;");
    conn.commit()
    conn.close()


def deletePlayers():
    """Removes all the player records from the database."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE from game;");
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) as num FROM game;")
    result = cursor.fetchone()[0]
    conn.close()
    return result


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO game (name) VALUES (%s);", (name,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches) of a player,
      ordered by wins descendingly
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM game ORDER BY wins DESC;")
    result = cursor.fetchall()
    conn.close()
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE game SET matches=matches+1, wins=wins+1 WHERE id = (%s);", (winner,)) 
    cursor.execute("UPDATE game SET matches=matches+1 WHERE id = (%s);", (loser,))
    conn.commit()
    conn.close()

 
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
    result = []
    players = playerStandings()
    for i in range(0, len(players), 2):
        result.append(
                (players[i][0], players[i][1], players[i+1][0], players[i+1][1])
            )
    return result

    
