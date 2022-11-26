import sqlite3
from pprint import pprint
import json


def get_title(title):
    with sqlite3.connect('netflix.db') as con:
        cursor = con.cursor()
        query = f"""
                SELECT title, country, release_year, listed_in, description
                FROM netflix
                WHERE title LIKE "%{title}%"
                ORDER BY release_year DESC 
        """
        cursor.execute(query)
        date = cursor.fetchone()
        movie = {
            'title': date[0],
            'country': date[1],
            'release_year': date[2],
            'genre': date[3],
            'description': date[4],
        }
        return movie

def get_release_year(year_one:int, year_two:int):
    with sqlite3.connect('netflix.db') as con:
        cursor = con.cursor()
        query = f"""
                SELECT title, release_year
                FROM netflix
                WHERE release_year BETWEEN {year_one} AND {year_two}
                ORDER BY release_year DESC
                LIMIT 100 
        """
        cursor.execute(query)
        data = []
        for i in cursor.fetchall():
            film = {
                'title': i[0],
                'release_year': i[1]
            }
            data.append(film)
        return data

def get_rating_family():
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        query = '''
            SELECT title, rating, description
            FROM netflix
            WHERE rating LIKE 'G' OR 'PG' OR 'PG-13'
        '''
        cur.execute(query)
        data = []
        for i in cur.fetchall():
            film = {
                'title':i[0],
                'rating': i[1],
                'description':i[2],
            }
            data.append(film)
        return data


def get_rating_children():
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        query = '''
            SELECT title, rating, description
            FROM netflix
            WHERE rating LIKE 'G'
        '''
        cur.execute(query)
        data = []
        for i in cur.fetchall():
            film = {
                'title':i[0],
                'rating': i[1],
                'description':i[2],
            }
            data.append(film)
        return data


def get_rating_adult():
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        query = '''
            SELECT title, rating, description
            FROM netflix
            WHERE rating LIKE 'R' OR 'NC-17'
        '''
        cur.execute(query)
        data = []
        for i in cur.fetchall():
            film = {
                'title':i[0],
                'rating': i[1],
                'description':i[2],
            }
            data.append(film)
        return data


def get_genre(genre):
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        query = f'''
                SELECT title, description
                FROM netflix
                WHERE listed_in LIKE '%{genre}%'
                ORDER BY release_year DESC 
                LIMIT 10
        '''
        cur.execute(query)
        data = []
        for i in cur.fetchall():
            film = {
                'title': i[0],
                'description': i[1],
            }
            data.append(film)
        return data


def get_cast(name1, name2):
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        query = f'''
                SELECT COUNT("cast"), "cast"
                FROM netflix
                WHERE "cast" LIKE '%{name1}%' 
                AND "cast" LIKE '%{name2}%'
                GROUP BY "cast"
                
        '''
        cur.execute(query)
        return cur.fetchall()

def get_type(type_, release_year, listed_in):
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        query = f'''
            SELECT title, description
            FROM netflix
            WHERE "type" LIKE '%{type_}%'
            AND release_year LIKE '%{release_year}%'
            AND listed_in LIKE '%{listed_in}%'
            ORDER BY title
        
        '''
        cur.execute(query)
        data = []
        for i in cur.fetchall():
            film = {
                'title': i[0],
                'description':i[1]
            }
            data.append(film)
        with open('one.json', 'w', encoding='UTF=8') as file:
            return json.dump(data, file)

pprint(get_genre("Dramas"))
