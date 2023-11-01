from dataclasses import dataclass


@dataclass
class Movie:
    title: str

    def __post_init__(self):
        self.title = self.title.title()

    def __str__(self) -> str:
        return self.title


if __name__ == '__main__':
    movie = Movie('harry potter')
    print(movie.title)
    print(movie)
