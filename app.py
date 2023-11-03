from PySide6 import QtWidgets, QtCore

from movie import Movie


class App(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Ciné Club')
        self.setup_ui()
        self.setup_css()
        self.setup_connections()
        self.populate_movies()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)  # type: ignore
        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_add = QtWidgets.QPushButton('Ajouter un film')
        self.list_movies = QtWidgets.QListWidget()
        self.list_movies.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)  # type: ignore
        self.btn_remove = QtWidgets.QPushButton('Supprimer le(s) film(s)')

        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_add)
        self.main_layout.addWidget(self.list_movies)
        self.main_layout.addWidget(self.btn_remove)

    def setup_css(self):
        self.setStyleSheet("""
            width: 150;
        """)
        self.list_movies.setStyleSheet("""
            height: 100
        """)

    def populate_movies(self):
        self.list_movies.clear()
        movies = Movie.get_movies()
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.ItemDataRole.UserRole, movie)
            self.list_movies.addItem(lw_item)

    def setup_connections(self):
        self.le_movieTitle.returnPressed.connect(self.add_movie)
        self.btn_add.clicked.connect(self.add_movie)
        self.btn_remove.clicked.connect(self.remove_movie)

    def add_movie(self):
        title_movie = self.le_movieTitle.text()
        if not title_movie:
            return False
        new_movie = Movie(title_movie)
        if new_movie.add_to_movies():
            self.populate_movies()

        self.le_movieTitle.clear()

    def remove_movie(self):
        for selected_item in self.list_movies.selectedItems():
            movie: Movie = selected_item.data(QtCore.Qt.ItemDataRole.UserRole)
            movie.remove_from_movies()
            self.list_movies.takeItem(self.list_movies.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec()
