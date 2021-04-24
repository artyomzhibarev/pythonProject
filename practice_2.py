import PySide2
from PySide2 import QtWidgets, QtCore


class MyFirstWindowSplitter(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyFirstWindowSplitter, self).__init__(parent)

        self.init_ui()

    def init_ui(self):
        central_widget = QtWidgets.QWidget()

        layoutV = QtWidgets.QVBoxLayout()
        splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)

        self.text_edit_1 = QtWidgets.QTextEdit()
        self.text_edit_1.append('text_edit_1')

        text_edit_2 = QtWidgets.QTextEdit()
        text_edit_2.append('text_edit_2')

        text_edit_3 = QtWidgets.QTextEdit()
        text_edit_3.append('text_edit_3')

        splitter.addWidget(self.text_edit_1)
        splitter.addWidget(text_edit_2)
        splitter.addWidget(text_edit_3)
        layoutV.addWidget(splitter)

        central_widget.setLayout(layoutV)
        self.setCentralWidget(central_widget)

        self.text_edit_1.installEventFilter(self)

    def eventFilter(self, watched: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent) -> bool:
        if watched == self.text_edit_1 and event.type() == QtCore.QEvent.Resize:
            print(self.text_edit_1.size().height())


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    my_form = MyFirstWindowSplitter()
    my_form.show()
    app.exec_()
