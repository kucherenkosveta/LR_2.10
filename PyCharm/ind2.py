#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_harry_potter(**kwargs):
    if kwargs:
        for movie_number, movie_title in kwargs.items():
            print(f'{movie_number}: {movie_title}')
    else:
        return None


if __name__ == "__main__":
    print_harry_potter(
        One="Harry Potter and the Philosopher's Stone",
        Two="Harry Potter And The Chamber of secrets",
        Three="Harry Potter and the prisoner of Azkaban",
        Four="Harry Potter and the Goblet of Fire",
        Five="Harry Potter and the Order of the Phoenix",
        Six="Harry Potter and the Half-Blood Prince",
        Seven="Harry Potter and the Deathly Hallows. Part 1",
        Eight="Harry Potter and the Deathly Hallows. Part 2"
    )

