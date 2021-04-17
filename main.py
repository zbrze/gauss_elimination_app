import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QDialog, QMainWindow, QFontDialog, \
    QColorDialog, QMessageBox
from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import QSize, QObject, pyqtSignal
import numpy as np
import random


class Main_window(QWidget):
    closed = pyqtSignal()
    matrix_created = pyqtSignal(int, int)
    error_occured = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("GAUSS ELIMINATION")                               #nadaje tytul okna

        self.setFixedHeight(350)                                               #nie mozna zmienic wlk okna
        self.setFixedWidth(300)

        self.setStyleSheet('background-color:#f7f1e3')                         #ustawiam kolor

        self.create_buttoms()


    def create_buttoms(self):

        self.columns = QLabel("COLUMNS", self)                                 #tworze etykiete kolumn
        self.columns.setGeometry(50, 50, 125, 25)                              #ustawiam ja w oknie

        self.num_columns = QLineEdit(self)                                     #tworze miejsce na wpisanie kolumn
        self.num_columns.setGeometry(125, 50, 125, 25)                         #ustawiam je w oknie
        self.num_columns.setStyleSheet('background-color:white')               #ustawiam kolor

        rows = QLabel("ROWS", self)                                            #tworze etykiete rzedow
        rows.setGeometry(50, 100, 125, 25)                                     #ustawiam polozenie w oknie

        self.num_rows = QLineEdit(self)                                        #tworze miejsce do wpisania rzedow
        self.num_rows.setGeometry(125, 100, 125, 25)                           #ustawiam polozenie w oknie
        self.num_rows.setStyleSheet('background-color:white')                  #ustawiam kolor

        self.submit = QPushButton("S U B M I T", self)                         #tworze przycisk submit
        self.submit.setGeometry(50, 150, 200, 50)                              #ustawiam polozenie w oknie
        self.submit.clicked.connect(self.open_matrix_window)                   #przypisuje do niego zadanie
        self.submit.setStyleSheet('background-color:#4a69bd;'                  #ustawiam kolor przycisku
                                  'color: white')                              #ustawiam kolor tekstu

        self.quit = QPushButton("Q U I T", self)                               #tworze przycisk quit
        self.quit.setGeometry(50, 225, 200, 50)                                #ustawiam jego polozenie w oknie
        self.quit.clicked.connect(self.open_exit_window)
        self.quit.setStyleSheet("color: white;"                                #ustawiam kolor tekstu
                        "background-color: #4a69bd;");                         #ustawiam kolor przycisku


    def open_matrix_window(self):
        cols = self.num_columns.text()                                  #pobieram wartosc wpisanych kolumn
        rows = self.num_rows.text()
        if((cols=='0' or rows=='0') or (not cols) or (not rows)):
            self.error_occured.emit()
        else:
            cols = int(cols)
            rows = int(rows)
            self.matrix_created.emit(rows, cols)                                   #wysylam sygnal(z wierszami i kolumnami)


    def open_exit_window(self):
        self.closed.emit()                                                     #wysylam sygnal



def make_board(parent, rows, cols):                                            #tworze funkcje, ktora tworzy siatke okienek
    board = []
    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            item = QLineEdit(parent)                                           #tworze i*j okienek
            item.setGeometry(20 + j*80, 20 + i*80, 80, 80)                     #ustawiam polozenie w oknie kazdego z [i][j] okienk
            row.append(item)                                                   #dodaje kazdy element do listy row
        board.append(row)                                                      #dodaje liste row do listy board
    return board

def fill_board(board, matrix):                                                 #tworze funkcje, ktora wypelnia board (siatke okienek), podana macierza
    rows = len(board)                                                          #wyliczam liczbe wierszy i kolumn
    cols = len(board[0])
    for row_index in range(rows):
        for col_index in range(cols):
            value = matrix[row_index, col_index]
            board[row_index][col_index].setText(str(value))                    #wypelniam kazde okienko elementem podanej macierza

class Error_window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wrong data")                                            #ustawiam tytul okna
        self.setFixedHeight(200)                                               #nie mozna zmienic rozmiaru okna
        self.setFixedWidth(380)
        self.setStyleSheet('background-color:#f7f1e3')                         #ustawiam kolor

        info = QLabel("You entered wrong number of rows or columns.\nDo you want to exit?", self)                  #tworze etykiete z pytaniem
        info.setGeometry(25, 20, 320, 50)                                      #ustawiam polozenie w oknie


        self.no = QPushButton("N O", self)                                     #tworze przycisk no
        self.no.setGeometry(90, 80, 200, 50)                                   #ustawiam polozenie w oknie
        self.no.setStyleSheet('background-color:#4a69bd;'                      #ustawiam kolor przycisku
                                  'color: white')                              #ustawiam kolor tekstu

        self.yes = QPushButton("Y E S", self)                                  #tworze przycisk yes
        self.yes.setGeometry(90, 135, 200, 50)                                 #ustawiam polozenie w oknie
        self.yes.setStyleSheet('background-color:#4a69bd;'                     #ustawiam kolor przycisku
                                  'color: white')                              #ustawiam kolor tekstu


class Matrix_window(QWidget):
    matrix_created = pyqtSignal(object)                                        #tworze sygnal

    def __init__(self, rows, cols):
        super().__init__()

        self.setWindowTitle("MATRIX")                                          #nadaje tytul okna

        self.setStyleSheet('background-color:#f7f1e3')                         #ustawiam kolor
        self.cols = cols
        self.rows = rows
        self.resize(40 + 80*self.cols, 140+80*self.rows)                        #ustawiam rozmiar okna

        self.board = make_board(parent=self, rows=rows, cols=cols)             #wywoluje funkcje, ktora tworzy siatke okienek

        self.submit = QPushButton("S U B M I T", self)                         #tworze przycisk submit
        self.submit.setGeometry(20, rows * 80 + 80, cols*80 , 50)              #uustawiam polozenie w oknie
        self.submit.clicked.connect(self._submit)                              #po kliknieciu submit wywoluje sie funkcja _submit
        self.submit.setStyleSheet('background-color:#4a69bd;'                  #ustawiam kolor przycisku
                                  'color: white')                              #ustawiam kolor tekstu

        self.randomize = QPushButton("R A N D O M I Z E", self)                #tworze przycisk randomize
        self.randomize.setGeometry(20, rows * 80 + 25, cols*80 , 50)           #ustawiam polozenie w oknie
        self.randomize.setStyleSheet('background-color:#4a69bd;'               #ustawiam kolor przycisku
                                  'color: white')
        self.randomize.clicked.connect(self.rand)                              #po kliknieciu randomize wywoluje sie funkcja rand


    def _submit(self):
        matrix = self.get_current_matrix()                                     #wywoluje funkcje get_current_matrix
        self.matrix_created.emit(matrix)                                       #wysyla sygnal


    def get_current_matrix(self):                                              #tworze funkcje, ktora pobiera wartosci podane przez uzytkownika do macierzy
        matrix = []
        for row_index in range(self.rows):
            row = []
            for col_index in range(self.cols):
                text = self.board[row_index][col_index].text()                 #pobieram wartosci z okienka
                number = float(text)                                           #zamianiam txt na floata
                row.append(number)                                             #dodaje wartosc do listy rows
            matrix.append(row)                                                 #dodaje liste row do listy matrix
        return np.array(matrix)                                                #zwraca pobrana macierz


    def rand(self):                                                            #tworze funkcje, ktora losuje liczby calkowite od 0 do 1000
        for row_index in range(self.rows):
            for col_index in range(self.cols):
                self.board[row_index][col_index].setText(str(random.randint(0, 1000)))



class Exit_window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EXIT")                                            #ustawiam tytul okna
        self.setFixedHeight(170)                                               #nie mozna zmienic rozmiaru okna
        self.setFixedWidth(300)
        self.setStyleSheet('background-color:#f7f1e3')                         #ustawiam kolor

        info = QLabel("Are you sure yoy want to exit?", self)                  #tworze etykiete z pytaniem
        info.setGeometry(75, 20, 150, 25)                                      #ustawiam polozenie w oknie


        self.no = QPushButton("N O", self)                                     #tworze przycisk no
        self.no.setGeometry(50, 50, 200, 50)                                   #ustawiam polozenie w oknie
        self.no.setStyleSheet('background-color:#4a69bd;'                      #ustawiam kolor przycisku
                                  'color: white')                              #ustawiam kolor tekstu

        self.yes = QPushButton("Y E S", self)                                  #tworze przycisk yes
        self.yes.setGeometry(50, 105, 200, 50)                                 #ustawiam polozenie w oknie
        self.yes.setStyleSheet('background-color:#4a69bd;'                     #ustawiam kolor przycisku
                                  'color: white')                              #ustawiam kolor tekstu



class Final_window(QWidget):
     def __init__(self, matrix):
        super().__init__()
        rows = len(matrix)
        cols = len(matrix[0])

        self.setWindowTitle("RESULT")                                          #nadaje tytul okna

        self.setStyleSheet('background-color:#f7f1e3')                         #ustawiam kolor

        self.resize(40 + 80*cols,90+80*rows)                                  #ustawiam rozmiar okna

        self.board = make_board(parent=self, rows=rows, cols=cols)             #tworze siatke okienek, wywoluje funkcje
        fill_board(self.board, matrix)                                         #wywoluje funkcje, ktora wypelnia okna wynikami

        self.quit = QPushButton("Q U I T", self)                               #tworze przycisk quit
        self.quit.setGeometry(20, rows * 80 + 30, cols*80 , 50)                #uustawiam polozenie w oknie
        self.quit.setStyleSheet('background-color:#4a69bd;'                    #ustawiam kolor przycisku
                                  'color: white')                              #ustawiam kolor tekstu
        self.quit.clicked.connect(QApplication.instance().quit)



class Program:

    def __init__(self):
        self.main_window = Main_window()
        self.main_window.matrix_created.connect(self._show_matrix_window)
        self.main_window.closed.connect(self._ask_quit)
        self.main_window.error_occured.connect(self.open_error_window)
        self.matrix_window = None

        self.exit_window = Exit_window()
        self.exit_window.no.clicked.connect(self._hide_exit_window)
        self.exit_window.yes.clicked.connect(QApplication.instance().quit)

        self.error_window = Error_window()
        self.error_window.no.clicked.connect(self._hide_error_window)
        self.error_window.yes.clicked.connect(QApplication.instance().quit)

        self.final_window = None


    def run(self):
        self.main_window.show()

    def _show_matrix_window(self, rows, cols):
        print('show matrix', rows, cols)
        self.matrix_window = Matrix_window(rows, cols)
        self.matrix_window.matrix_created.connect(self._process_matrix)

        self.main_window.hide()
        self.matrix_window.show()

    def _ask_quit(self):
        self.exit_window.show()

    def _hide_exit_window(self):
        self.exit_window.hide()

    def _hide_error_window(self):
        self.error_window.hide()

    def open_error_window(self):
        self.error_window.show()

    def _process_matrix(self, matrix):
        print('MATRIX', matrix)
        self.matrix_window.hide()
        try:
            print('calculate...')
            result = Gauss_pivoting(matrix)
            print('RESULT', result)
        except Exception as e:
            print(e)
        self.final_window = Final_window(result)
        self.final_window.show()


def Gauss_pivoting(matrixA):
    n = len(matrixA)
    for i in range(n):

        # partial pivoting
        max_row = i  # find row with the greatest number in column i
        counter = 1
        while i + counter < n:
            if abs(matrixA[i + counter, i]) > abs(matrixA[i, i]):
                max_row = i + counter
            counter += 1

        if i != max_row:  # swap rows if max_row is different than i
            matrixA[max_row], matrixA[i] = matrixA[i], matrixA[max_row].copy()
        for j in range(i + 1, n):
            quotient = float(matrixA[j][i]) / matrixA[i][i]
            for k in range(i, n):
                matrixA[j][k] -= float(matrixA[i][k]) * quotient
            matrixA[j][i] = 0
    for i in range(n):
        for j in range(n):
            matrixA[i, j] = round(matrixA[i, j], 3)

    return matrixA



if __name__ == '__main__':
    app = QApplication([])
    program = Program()
    program.run()
    sys.exit(app.exec_())
