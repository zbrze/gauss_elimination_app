from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPlainTextEdit)
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

class Matrix_window(QWidget):
    def __init__(self, cols, rows):
        super().__init__()
        print(cols, rows)
        layout = QVBoxLayout()
        self.label = QLabel("Matrix")
        layout.addWidget(self.label)
        self.initUI(rows, cols)

        self.resize(410+ 10*cols, 380+10*rows)

    def initUI(self, rows, cols, plain=None):
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 361))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QtWidgets.QGridLayout()
        for i in range (0,rows):
            for j in  range (0,cols):
                plain = QPlainTextEdit(self.verticalLayoutWidget)
                self.gridLayout.addWidget(plain, i, j)
                plain.setObjectName("plain"+ str(i) + str(j))
                print(plain.objectName())
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 2)

        self.submit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.submit_btn.setText("Submit")
        self.gridLayout.addWidget(self.submit_btn, 4, 1, 1, 2)
        self.randomize_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.randomize_btn.setText("Randomize")
        self.gridLayout.addWidget(self.randomize_btn, 6, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)


class Main_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Hello, world!'
        self.resize(410, 310)

        self.initUI()

    def initUI(self):
        #to setObjectName może się później przy wyszukiwaniu
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 20, 312, 251))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.label_rows = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_rows.setText("rows")
        self.gridLayout.addWidget(self.label_rows, 1, 1, 1, 1)

        self.rows_num = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.rows_num.setObjectName("rows_num")
        self.gridLayout.addWidget(self.rows_num, 1, 2, 1, 1)

        self.cols_num = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.cols_num.setObjectName("cols_num")
        self.gridLayout.addWidget(self.cols_num, 0, 2, 1, 1)

        self.submit_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.submit_btn.setObjectName("submit_btn")
        self.submit_btn.setText("Submit")
        self.gridLayout.addWidget(self.submit_btn, 3, 1, 1, 2)

        self.quit_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.quit_btn.setObjectName("quit_btn")
        self.gridLayout.addWidget(self.quit_btn, 4, 1, 1, 2)
        self.quit_btn.setText("Quit")
        self.quit_btn.clicked.connect(QApplication.instance().quit)

        self.label_cols = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_cols.setText("columns")
        self.gridLayout.addWidget(self.label_cols, 0, 1, 1, 1)

        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 1, 1, 2)
        self.checkBox.setText("calculate indeterminates")
        self.show()
        cols = self.cols_num.value()
        self.submit_btn.mousePressEvent = lambda event:self.setSize(self.cols_num.value(), self.rows_num.value())
        #self.setCentralWidget(self.submit_btn)

    def setSize(self, cols, rows):
        print(rows)
        if cols != 0 and rows != 0:
            self.w = Matrix_window(cols, rows)
            self.w.show()





def main():

    app = QApplication(sys.argv)
    ex = Main_Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
