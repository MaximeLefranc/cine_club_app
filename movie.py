from dataclasses import dataclass
import json
from pathlib import Path

MOVIES_DB = Path.cwd() / 'data' / 'movies.json'


@dataclass
class Movie:
    title: str

    def __post_init__(self):
        self.title = self.title.title()

    def __str__(self) -> str:
        return self.title

    def _get_movies(self) -> list:
        try:
            with open(MOVIES_DB, 'r') as f:
                content = json.load(f)
        except json.decoder.JSONDecodeError:
            print('Il n\'y a pas de films dans la base de donnée.')
        else:
            return content

        return []

    def _write_movies(self, movies):
        with open(MOVIES_DB, 'w') as f:
            json.dump(movies, f, indent=4)


if __name__ == '__main__':
    movie = Movie('harry potter')
    # print(movie.title)
    # print(movie)
    # print(MOVIES_DB)
    # print(movie._write_movies(["Harry Potter", "Barry Lyndon"]))
    print(movie._get_movies())
