import sys

from PyQt5 import QtWidgets
from PyQt5.QtSerialPort import QSerialPortInfo

from console import TerminalApp
from ui import uartsearch_ui


class PortChooseApp(QtWidgets.QMainWindow, uartsearch_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.terminal = []
        self.port = ''

        self.scan()
        self.change_port()
        self.scanButton.clicked.connect(self.scan)
        self.connectButton.clicked.connect(self.con)
        self.comboBox.currentIndexChanged.connect(self.change_port)

    def change_port(self):
        self.port = self.comboBox.currentText()
        print(self.port)

    def scan(self):
        self.comboBox.clear()
        self.comboBox.addItems(map(lambda port: port.portName(), QSerialPortInfo.availablePorts()))

    def con(self):
        if self.port == '':
            return
        terminal = TerminalApp(self.port)
        terminal.show()
        self.terminal.append(terminal)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = PortChooseApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
