from PySide2 import QtWidgets
import MainForm


class MyFirstWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyFirstWindow, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()
        button = QtWidgets.QPushButton('Button')

        layout.addWidget(button)

        self.setLayout(layout)

        self.ui = MainForm.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_open.clicked.connect(self.on_push_button_open_clicked)
        self.ui.pushButton_Accept.clicked.connect(self.on_push_button_accept_clicked)

    def on_push_button_open_clicked(self):
        filepath, ok = QtWidgets.QFileDialog.getOpenFileName(self, 'File selection', ".")
        if not ok:
            return
        print('Open button was pressed')
        print(filepath)

    def on_push_button_accept_clicked(self):
        print(self.ui.lineEdit_5.text())
        print(self.ui.lineEdit_6.text())
        print(self.ui.lineEdit_7.text())
        print(self.ui.lineEdit_8.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    my_form = MyFirstWindow()
    my_form.show()
    app.exec_()
