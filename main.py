import sys

import json

import random

from conf import MODEL
model = MODEL
dict = {}

from faker import Faker
fake_ru = Faker('ru_RU')
dict_books = {}

book_file = "books.txt"
output_file = "output.json"


def year():
    ...
    return 'year'


def isbn13_():
    ...
    return 'isbn13_'


def pages():
    ...
    return "pages"


def rating():
    ...
    return 'rating'


def price():
    ...
    return 'price'


def author():
    ...
    return 'author'


def title():
    ...
    return 'title'


def main():
    for i in range(1, 101):
        year = random.randint(1800, 2022)
        pages = random.randint(50, 400)
        isbn13_ = fake_ru.isbn13()
        rating = random.uniform(0, 5)
        price = random.uniform(0, 10000)
        pk = 1 + i

        with open(book_file, "r", encoding="utf-8") as inp:
            lines = []
            lines = inp.readlines()
        title = random.choice(lines)[:-1]

        for k in range(1, 4):
            author = fake_ru.name()

        dict[i] = {"Author": author, "Title": title, "YeaR": year, "Pages": pages, "Isbn13": isbn13_, "Rating": rating, "Price": price, "pk": pk}
        #books_list = r"""####\s+\[(?P<author>+?)\]\.\s+\[?P<title>]"""
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dict, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
