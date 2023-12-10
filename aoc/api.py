import datetime
from pathlib import Path

from bs4 import BeautifulSoup
import requests as rq
import requests_cache

from . import configd


def login(session_secret):
    session_cookie_location = Path(configd) / "secret"
    with open(session_cookie_location, "w") as session:
        session.write(f"session={session_secret}")


def input(day, year=None):

    if not year:
        year = datetime.datetime.now().year

    requests_cache.install_cache(Path(configd) / "cache")

    session_cookie_location = Path(configd) / "secret"

    with open(session_cookie_location, "r") as session:
        headers = {"Cookie": session.read().rsplit()[0]}

    return rq.get(f"https://adventofcode.com/{year}/day/{day}/input",
                  headers=headers).text


def submit(day, level, answer, year=None):

    if not year:
        year = datetime.datetime.now().year

    session_cookie_location = Path(configd) / "secret"

    with open(session_cookie_location, "r") as session:
        headers = {"Cookie": session.read().rsplit()[0]}

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
