from queries import *


def generate_normal_text():
    stars = get_stars()
    stars_news = []
    for s in stars:
        text = f"""{s[1]}

{s[2]}

{s[3]}
"""
        photo = s[4]
        stars_news.append((text, photo))

    return stars_news


def generate_normal_text_2():
    scandals = get_scandals()
    scandals_news = []
    for s in scandals:
        text = f"""{s[1]}

    {s[2]}

    {s[3]}
    """
        photo = s[4]
        scandals_news.append((text, photo))

    return scandals_news


def generate_normal_text_3():
    premieres = get_premieres()
    premieres_news = []
    for p in premieres:
        text = f"""{p[1]}

    {p[2]}

    {p[3]}
    """
        photo = p[4]
        premieres_news.append((text, photo))

    return premieres_news


def generate_normal_text_4():
    people = get_people()
    people_news = []
    for p in people:
        text = f"""{p[1]}

    {p[2]}

    {p[3]}
    """
        photo = p[4]
        people_news.append((text, photo))

    return people_news


def generate_normal_text_5():
    fashion = get_fashion()
    fashion_news = []
    for f in fashion:
        text = f"""{f[1]}

    {f[2]}

    {f[3]}
    """
        photo = f[4]
        fashion_news.append((text, photo))

    return fashion_news
