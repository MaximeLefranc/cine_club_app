from __future__ import annotations
from dataclasses import dataclass
import json
from pathlib import Path
import logging

logging.basicConfig(
    filename=Path.cwd() / 'movies.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

MOVIES_DB = Path.cwd() / 'data' / 'movies.json'


@dataclass
class Movie:
    title: str

    def __post_init__(self):
        self.title = self.title.title()

    def __str__(self) -> str:
        return self.title

    @staticmethod
    def get_movies() -> list[Movie] | list:
        try:
            with open(MOVIES_DB, 'r') as f:
                content = json.load(f)
        except json.decoder.JSONDecodeError:
            logging.info('La base de donnée ne contient pas de film.')
        else:
            return [Movie(title) for title in content]

        return []

    def _get_movies(self) -> list:
        try:
            with open(MOVIES_DB, 'r') as f:
                content = json.load(f)
        except json.decoder.JSONDecodeError:
            logging.info('La base de donnée ne contient pas de film.')
        else:
            return content

        return []

    def _write_movies(self, movies):
        with open(MOVIES_DB, 'w') as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self) -> bool:
        movies = self._get_movies()
        if self.title in movies:
            logging.warning(f'Le film {self.title} est déjà présent dans la base de données')
            return False

        movies.append(self.title)
        self._write_movies(movies)
        return True

    def remove_from_movies(self) -> bool:
        movies = self._get_movies()
        if self.title not in movies:
            logging.warning(f'Le film {self.title} n\'est pas présent dans la base de données -> suppression annulé')
            return False

        movies.remove(self.title)
        self._write_movies(movies)
        return True


if __name__ == '__main__':
    # print(movie.title)
    # print(movie)
    # print(MOVIES_DB)
    # print(movie._write_movies(["Harry Potter", "Barry Lyndon"]))
    movies = Movie.get_movies()
    print(movies)
