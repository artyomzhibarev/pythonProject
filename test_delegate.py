import sys
import os
import random
import time

from PySide2 import QtWidgets, QtGui, QtCore


class CustomTableView(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        super(CustomTableView, self).__init__(parent)

    def data(self, item, role):
        if role == QtCore.Qt.DisplayRole:
            if item.column() == 2:
                try:
                    size = QtGui.QStandardItemModel.data(self, item, QtCore.Qt.DisplayRole)
                    return int(size) / 1024
                except Exception as e:
                    print(e)
        return QtGui.QStandardItemModel.data(self, item, role)


class DoubleDelegate(QtWidgets.QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        editor = QtWidgets.QDoubleSpinBox(parent, decimals=2)
        editor.setFrame(False)
        editor.setMaximum(40)
        editor.setMinimum(-40)

        editor.valueChanged.connect(lambda: print(editor.value()))
        return editor

    def updateEditorGeometry(self, editor, option, index) -> None:
        editor.setGeometry(option.rect)


class TestDelegate(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(TestDelegate, self).__init__(parent)

        self.initUi()
        self.loadTable()

    def initUi(self):
        self.tableView = QtWidgets.QTableView()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.tableView)

        self.setLayout(layout)

        self.doubleDelegate = DoubleDelegate()

    def loadTable(self):
        headers = ["Путь", "Число", 'Размер', "Время"]

        stm = CustomTableView()
        stm.setHorizontalHeaderLabels(headers)

        data = [x for x in os.listdir()]

        stm.setRowCount(len(data))

        for row in range(len(data)):
            stm.setItem(row, 0, QtGui.QStandardItem(data[row]))
            stm.setItem(row, 1, QtGui.QStandardItem(str(random.randint(-30, 30))))
            stm.setItem(row, 2, QtGui.QStandardItem(str(os.path.getsize(data[row]))))
            stm.setItem(row, 3, QtGui.QStandardItem(str(time.time() + random.randint(0, 400))))

        self.tableView.setModel(stm)
        self.tableView.setItemDelegateForColumn(1, self.doubleDelegate)
        # self.tableView.horizontalHeader().setStretchLastSection(QtWidgets.QHeaderView.Stretch)
        self.tableView.resizeColumnsToContents()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = TestDelegate()
    win.show()
    sys.exit(app.exec_())
