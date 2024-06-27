import sqlite3


def get_stars():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM news
    WHERE category_id = 1 
    ORDER BY news_id ASC 
    LIMIT 5
    """)

    stars = cursor.fetchall()

    conn.close()

    return stars


def get_scandals():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM news
    WHERE category_id = 2 
    ORDER BY news_id ASC 
    LIMIT 5
    """)

    scandals = cursor.fetchall()

    conn.close()

    return scandals


def get_premieres():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM news
    WHERE category_id = 3 
    ORDER BY news_id ASC 
    LIMIT 5
    """)

    premieres = cursor.fetchall()

    conn.close()

    return premieres


def get_people():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM news
    WHERE category_id = 4 
    ORDER BY news_id ASC 
    LIMIT 5
    """)

    people = cursor.fetchall()

    conn.close()

    return people


def get_fashion():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM news
    WHERE category_id = 5 
    ORDER BY news_id ASC 
    LIMIT 5
    """)

    fashion = cursor.fetchall()

    conn.close()

    return fashion
