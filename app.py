from PySide6 import QtWidgets

from movie import Movie


class App(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Ciné Club')
        self.setup_ui()
        self.setup_css()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)  # type: ignore
        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_add = QtWidgets.QPushButton('Ajouter un film')
        self.list_movies = QtWidgets.QListWidget()
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


app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec()
