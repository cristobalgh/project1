import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    # Create table to import data into
    db.execute("DROP TABLE IF EXISTS books CASCADE")
    db.execute("CREATE TABLE books (id SERIAL, isbn VARCHAR, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year VARCHAR NOT NULL)")
    db.execute("DROP TABLE IF EXISTS reviews CASCADE")
    #db.execute("CREATE TABLE reviews (id SERIAL, user_id VARCHAR NOT NULL, book_id VARCHAR NOT NULL, comment VARCHAR NOT NULL, rating VARCHAR NOT NULL)")
    db.execute("CREATE TABLE reviews (id serial NOT NULL, user_id int4 NOT NULL, book_id int4 NOT NULL, comment text NOT NULL, rating int4 NOT NULL, time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)")
    db.execute("DROP TABLE IF EXISTS users CASCADE")
    db.execute("CREATE TABLE users (id SERIAL, username TEXT NOT NULL, hash TEXT NOT NULL)")
    db.commit()
if __name__ == "__main__":
    main()
