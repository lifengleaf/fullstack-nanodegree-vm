#
# Database access functions for the web forum.
# 
import psycopg2

## Database connection
DB = []

## Get posts from database.
def GetAllPosts():
    db = psycopg2.connect('dbname = forum')
    c = db.cursor()
    c.execute('SELECT time, content FROM posts ORDER BY time DESC')
    posts = ({'content': str(row[1]),
              'time': str(row[0])}
              for row in c.fetchall())
    db.close()
    return posts

## Add a post to the database.
def AddPost(content):
    db = psycopg2.connect('dbname = forum')
    c = db.cursor()
    c.execute("INSERT INTO posts (content) VALUES (%s)", 
              (content,))
    db.commit()
    db.close() 
