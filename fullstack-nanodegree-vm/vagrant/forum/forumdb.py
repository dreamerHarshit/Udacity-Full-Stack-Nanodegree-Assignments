#
# Database access functions for the web forum.
# 
import psycopg2
import time

## Database connection
## Get posts from database.
def GetAllPosts():
    db=psycopg2.connect("dbname=forum")
    c=db.cursor()
    c.execute("Select time, content from posts order by time desc")
    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in c.fetchall()]
    db.close()
    return posts

## Add a post to the database.
def AddPost(content):
    db=psycopg2.connect("dbname=forum")
    c=db.cursor()
    c.execute("INSERT INTO posts (content) VALUES (%s)" , (content,))
    c.execute("update posts set content='cheese' where content like '%spam%'")
    #c.execute("select * from posts where content='cheese'")
    c.execute("DELETE from posts where content='cheese'")
    db.commit()
    db.close()
