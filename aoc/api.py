from bs4 import BeautifulSoup
import requests as rq
import requests_cache
import datetime


def input(day, year=None):

    if not year:
        year = datetime.datetime.now().year

    requests_cache.install_cache("/home/yelkhadi/.aoc/cache")

    session_cookie_location = "/home/yelkhadi/.aoc/secret"

    with open(session_cookie_location, "r") as session:
        headers = {"Cookie": session.readline()[:-1]}
    
    return rq.get(f"https://adventofcode.com/{year}/day/{day}/input", headers=headers).text


def submit(day, level, answer, year=None):

    if not year:
        year = datetime.datetime.now().year

    session_cookie_location = "/home/yelkhadi/.aoc/secret"

    with open(session_cookie_location, "r") as session:
        headers = {"Cookie": session.readline()[:-1]}

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    content = f"level={level}&answer={answer}"

    headers["Content-Length"] = str(len(content))

    res = rq.post(
        f"https://adventofcode.com/{year}/day/{day}/answer",
        data=content,
        headers=headers
        )

    soup = BeautifulSoup(res.text, features="lxml")

    print(soup.main.text)