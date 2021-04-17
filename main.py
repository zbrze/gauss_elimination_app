from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QDialog, QMainWindow, QFontDialog, \
    QColorDialog, QMessageBox
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

        self.setWindowTitle("GAUSS ELIMINATION")

        self.setFixedHeight(350)
        self.setFixedWidth(300)

        self.setStyleSheet('background-color:#f7f1e3')

        self.create_buttoms()


    def create_buttoms(self):

        self.columns = QLabel("COLUMNS", self)
        self.columns.setGeometry(50, 50, 125, 25)

        self.num_columns = QLineEdit(self)
        self.num_columns.setGeometry(125, 50, 125, 25)
        self.num_columns.setStyleSheet('background-color:white')

        rows = QLabel("ROWS", self)
        rows.setGeometry(50, 100, 125, 25)

        self.num_rows = QLineEdit(self)
        self.num_rows.setGeometry(125, 100, 125, 25)
        self.num_rows.setStyleSheet('background-color:white')

        self.submit = QPushButton("S U B M I T", self)
        self.submit.setGeometry(50, 150, 200, 50)
        self.submit.clicked.connect(self.open_matrix_window)
        self.submit.setStyleSheet('background-color:#4a69bd;'              
                                  'color: white')

        self.quit = QPushButton("Q U I T", self)
        self.quit.setGeometry(50, 225, 200, 50)
        self.quit.clicked.connect(self.open_exit_window)
        self.quit.setStyleSheet("color: white;"                             
                        "background-color: #4a69bd;");

    def open_matrix_window(self):
        cols = self.num_columns.text()
        rows = self.num_rows.text()
        if((cols=='0' or rows=='0') or (not cols) or (not rows)):
            self.error_occured.emit()
        else:
            cols = int(cols)
            rows = int(rows)
            if (rows > cols + 1):
                self.error_occured.emit()
            else:
                self.matrix_created.emit(rows, cols)


    def open_exit_window(self):
        self.closed.emit()



def make_board(parent, rows, cols):
    board = []
    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            item = QLineEdit(parent)
            item.setGeometry(20 + j*80, 20 + i*80, 80, 80)
            row.append(item)
        board.append(row)
    return board

def fill_board(board, matrix):
    rows = len(board)
    cols = len(board[0])
    for row_index in range(rows):
        for col_index in range(cols):
            value = matrix[row_index, col_index]
            board[row_index][col_index].setText(str(value))

class Error_window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wrong data")
        self.setFixedHeight(200)
        self.setFixedWidth(240)
        self.setStyleSheet('background-color:#f7f1e3')

        info = QLabel("You entered wrong data.\nDo you want to exit?", self)
        info.setGeometry(30, 20, 220, 50)


        self.no = QPushButton("N O", self)
        self.no.setGeometry(20, 80, 200, 50)
        self.no.setStyleSheet('background-color:#4a69bd;'                     
                                  'color: white')

        self.yes = QPushButton("Y E S", self)
        self.yes.setGeometry(20, 135, 200, 50)
        self.yes.setStyleSheet('background-color:#4a69bd;'                     
                                  'color: white')


class Matrix_window(QWidget):
    matrix_created = pyqtSignal(object)

    error_occured = pyqtSignal()
    def __init__(self, rows, cols):
        super().__init__()

        self.setWindowTitle("MATRIX")

        self.setStyleSheet('background-color:#f7f1e3')
        self.cols = cols
        self.rows = rows
        self.resize(40 + 80*self.cols, 140+80*self.rows)

        self.board = make_board(parent=self, rows=rows, cols=cols)

        self.submit = QPushButton("S U B M I T", self)
        self.submit.setGeometry(20, rows * 80 + 80, cols*80 , 50)
        self.submit.clicked.connect(self._submit)
        self.submit.setStyleSheet('background-color:#4a69bd;'              
                                  'color: white')

        self.randomize = QPushButton("R A N D O M I Z E", self)
        self.randomize.setGeometry(20, rows * 80 + 25, cols*80 , 50)
        self.randomize.setStyleSheet('background-color:#4a69bd;'             
                                  'color: white')
        self.randomize.clicked.connect(self.rand)

        self.error_window = Error_window()
        self.error_window.no.clicked.connect(self._hide_error_window)
        self.error_window.yes.clicked.connect(QApplication.instance().quit)

    def _hide_error_window(self):
        self.error_window.hide()

    def open_error_window(self):
        self.error_window.show()

    def _submit(self):
        try:
            matrix = self.get_current_matrix()
            self.matrix_created.emit(matrix)
        except:
            self.error_occured.emit()

    def get_current_matrix(self):
        matrix = []
        for row_index in range(self.rows):
            row = []
            for col_index in range(self.cols):
                text = self.board[row_index][col_index].text()
                number = float(text)
                row.append(number)
            matrix.append(row)
        return np.array(matrix)

    def rand(self):
        for row_index in range(self.rows):
            for col_index in range(self.cols):
                self.board[row_index][col_index].setText(str(random.randint(0, 1000)))



class Exit_window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EXIT")
        self.setFixedHeight(170)
        self.setFixedWidth(300)
        self.setStyleSheet('background-color:#f7f1e3')

        info = QLabel("Are you sure yoy want to exit?", self)
        info.setGeometry(75, 20, 150, 25)


        self.no = QPushButton("N O", self)
        self.no.setGeometry(50, 50, 200, 50)
        self.no.setStyleSheet('background-color:#4a69bd;'             
                                  'color: white')

        self.yes = QPushButton("Y E S", self)
        self.yes.setGeometry(50, 105, 200, 50)
        self.yes.setStyleSheet('background-color:#4a69bd;'                   
                                  'color: white')



class Final_window(QWidget):
     def __init__(self, matrix):
        super().__init__()
        rows = len(matrix)
        cols = len(matrix[0])

        self.setWindowTitle("RESULT")

        self.setStyleSheet('background-color:#f7f1e3')

        self.resize(40 + 80*cols,90+80*rows)

        self.board = make_board(parent=self, rows=rows, cols=cols)
        fill_board(self.board, matrix)

        self.quit = QPushButton("Q U I T", self)
        self.quit.setGeometry(20, rows * 80 + 30, cols*80 , 50)
        self.quit.setStyleSheet('background-color:#4a69bd;'                
                                  'color: white')
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
    m = len(matrixA[0])
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
            for k in range(i, m):
                matrixA[j][k] -= float(matrixA[i][k]) * quotient
            matrixA[j][i] = 0
    for i in range(n):
        for j in range(m):
            matrixA[i, j] = round(matrixA[i, j], 3)

    return matrixA



if __name__ == '__main__':
    app = QApplication([])
    program = Program()
    program.run()
    sys.exit(app.exec_())
