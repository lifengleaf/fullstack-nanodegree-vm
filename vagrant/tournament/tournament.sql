-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create a table containing player information:
-- id: the player's unique id (assigned by the database)
-- name: the player's full name (as registered)
-- wins: the number of matches the player has won
-- matches: the number of matches the player has played

CREATE TABLE IF NOT EXISTS game(
	id SERIAL PRIMARY KEY,
	name TEXT,
	wins INTEGER DEFAULT 0,
	matches INTEGER DEFAULT 0
);
