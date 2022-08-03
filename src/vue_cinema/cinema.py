from typing import List

import requests


class Cinema:
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get("name")
        self.search_term = kwargs.get("search_term")
        self.id = int(kwargs.get("id", 0))

    def __str__(self) -> str:
        return self.name

def get_cinemas() -> List[Cinema]:
    url = "https://www.myvue.com/data/locations"
    headers = {"x-requested-with": "XMLHttpRequest"}

    response = requests.request("GET", url, headers=headers).json()

    cinemas = []
    for alpha in response.get("venues"):
        for cinema in alpha.get("cinemas"):
            cinemas.append(Cinema(**cinema))

    return cinemas

def search_cinemas(search_term: str) -> List[Cinema]:
    cinemas = get_cinemas()
    return [cinema for cinema in cinemas if search_term.lower() in cinema.search_term.lower()]
