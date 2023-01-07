import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget

from mainUI import Ui_MainWindow
from addEditCoffeeFormUI import Ui_Form


class CoffeMachine(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = sqlite3.connect('coffee.sqlite')
        self.setWindowTitle('Добавление кофе')
        self.cur = self.db.cursor()
        self.pushButton.clicked.connect(self.createNewCoffe)

    def createNewCoffe(self):
        try:
            req = f'''INSERT INTO coffes(название_сорта, степень_обжарки, вид, описание_вкуса, цена, объем_упаковки) VALUES('{
            self.lineEdit.text()}', '{self.lineEdit_2.text()}', '{self.lineEdit_3.text()}', '{self.lineEdit_4.text()}', '{
            self.lineEdit_5.text()}', '{self.lineEdit_6.text()}')'''
            print(req)
            self.cur.execute(req)
            self.db.commit()
            ex.loadTable()
        except:
            self.label_7.setText('Неверно заполнена форма')


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = sqlite3.connect('coffee.sqlite')
        self.setWindowTitle('Кофе')
        self.cursor = self.db.cursor()
        self.pushButton.clicked.connect(self.newCoffe)
        self.loadTable()

    def loadTable(self):
        res = self.cursor.execute('SELECT * FROM coffes').fetchall()
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setHorizontalHeaderLabels([i[0] for i in self.cursor.description])
        for i, u in enumerate(res):
            for j, k in enumerate(u):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(k)))

    def newCoffe(self):
        self.ext = CoffeMachine()
        self.ext.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())