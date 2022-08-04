"""Main file for Showing class and showing related functions."""
from datetime import datetime
from typing import List

import requests

from .cinema import Cinema
from .movie import Movie


class Showing:
    """Main class for showings that includes information about them."""

    def __init__(self, **kwargs) -> None:
        """Initialize a Showing object."""
        self.date_prefix = kwargs.get("date_prefix") if\
            kwargs.get("date_prefix") != "" else None
        self.day = kwargs.get("date_day")
        date = datetime.strptime(kwargs.get("date_time"), "%Y-%m-%d").date()
        time = datetime.strptime(kwargs.get("time"), "%I:%M %p").time()
        self.datetime = datetime.combine(date, time)
        self.cinema = Cinema(cinema_id=kwargs.get("cinema"))
        self.movie = Movie(movie_id=kwargs.get("movie"))

    def __repr__(self) -> str:
        """Return a string representation of the Showing object."""
        return str(self.datetime)

    def __str__(self) -> str:
        """Return a string representation of the Showing object."""
        return str(self.datetime)


def get_showings(cinema: Cinema, movie: Movie) -> List[Showing]:
    """Return a list of Showing objects."""
    url = "https://www.myvue.com/data/showings/{}/{}"\
        .format(movie.id, cinema.id)

    headers = {"x-requested-with": "XMLHttpRequest"}

    try:
        response = requests.request("GET", url, headers=headers).json()
    except Exception as e:
        print(e)
        return []

    showings = []
    for day in response.get("showings", {}):
        for time in day.get("times", {}):
            day_without_showings = day.copy()
            day_without_showings.pop("times")
            day_without_showings.pop("is_dp2_2")

            showings.append(Showing(**time, **day_without_showings))

    return showings
