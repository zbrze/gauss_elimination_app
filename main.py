from PyQt5.QtWidgets import (QWidget, QVBoxLayout)
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

    def initUI(self, rows, cols):
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 361))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QtWidgets.QGridLayout()
        """  
        for i in rows:
            for j in cols:
                #generujemy okienka

        
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.gridLayout.addWidget(self.plainTextEdit_8, 2, 1, 1, 1)
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.gridLayout.addWidget(self.plainTextEdit_5, 1, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 2, 1, 1)
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.gridLayout.addWidget(self.plainTextEdit_6, 1, 2, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 0, 1, 1, 1)
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.gridLayout.addWidget(self.plainTextEdit_7, 2, 0, 1, 1)
        self.plainTextEdit_10 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_10.setObjectName("plainTextEdit_10")
        self.gridLayout.addWidget(self.plainTextEdit_10, 0, 3, 1, 1)
        self.plainTextEdit_9 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_9.setObjectName("plainTextEdit_9")
        self.gridLayout.addWidget(self.plainTextEdit_9, 2, 2, 1, 1)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.gridLayout.addWidget(self.plainTextEdit_3, 0, 0, 1, 1)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.gridLayout.addWidget(self.plainTextEdit_4, 1, 0, 1, 1)
        self.plainTextEdit_12 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_12.setObjectName("plainTextEdit_12")
        self.gridLayout.addWidget(self.plainTextEdit_12, 2, 3, 1, 1)
        self.plainTextEdit_11 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_11.setObjectName("plainTextEdit_11")
        self.gridLayout.addWidget(self.plainTextEdit_11, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 2)
        """
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
