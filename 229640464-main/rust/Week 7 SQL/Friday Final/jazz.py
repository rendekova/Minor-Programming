import sqlite3
import sys
import os

def get_sql():
	# output the 5 artist with the most tracks in the tracks table of the Jazz genre,
	# highest amount of tracks first.
	# Output shows artists name and his/her amount of tracks. See example.
	sql = """

	SELECT
	    artists.Name AS Name,
		COUNT(tracks.TrackId) AS amount
	FROM artists
	JOIN albums ON artists.ArtistId = albums.ArtistId
	JOIN tracks ON albums.AlbumId = tracks.AlbumId
	JOIN genres ON tracks.GenreId = genres.GenreId
	WHERE genres.Name = 'Jazz'
	GROUP BY artists.ArtistId
	ORDER BY amount DESC
	LIMIT 5;
	"""
	return sql

def row_factory(cursor, row):
	# do not change below code
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def get_results(sql):
	# do not change below code
	dbname = "dbhunt.db"
	connection = sqlite3.connect(dbname)
	connection.row_factory = row_factory
	# make cursor
	cursor = connection.cursor()
	# get results from database
	return cursor.execute(sql)

if __name__ == "__main__":
	# do not change below code
	sql = get_sql()
	results = list(get_results(sql))
	os.system('cls' if os.name == 'nt' else 'clear')
	print()
	for r in results:
		print(r)
	print(f"Rows: {len(results)}")
	print()
