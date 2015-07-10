-- Table definitions for the tournament project.

--Delete and recreate tournament database before connecting to it
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

--Create tables within database "tournament"
CREATE TABLE players (
	player_id serial PRIMARY KEY,
	name text
);

CREATE TABLE matches (
	match_id serial PRIMARY KEY,
	winner integer REFERENCES players(player_id),
	loser integer REFERENCES players(player_id)
);

--View: Shows number of *Wins* for each player
CREATE VIEW win_record AS
    SELECT
		players.player_id AS "Player ID",
		COUNT(matches.winner) AS "Wins"
    FROM players LEFT JOIN matches
        ON players.player_id = matches.winner
    GROUP BY players.player_id
    ORDER BY "Wins" DESC;

--View: Shows number of *Losses* for each player
CREATE VIEW loss_record AS
    SELECT
		players.player_id AS "Player ID",
		COUNT(matches.loser) AS "Losses"
    FROM players LEFT JOIN matches
        ON players.player_id = matches.loser
    GROUP BY players.player_id
    ORDER BY "Losses" DESC;

--View: Shows Player ID, Name, Wins, and Matches Played, sorted by Number of Wins
CREATE VIEW standings AS
    SELECT
		players.player_id AS "Player ID",
		players.name AS "Player Name",
		win_record."Wins" AS "Wins",
		win_record."Wins" + loss_record."Losses" AS "Matches Played"
    FROM
		players,
		win_record,
		loss_record
    WHERE players.player_id = win_record."Player ID" AND players.player_id = loss_record."Player ID"
	ORDER BY win_record."Wins" DESC;