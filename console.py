import sys

from PyQt5.QtGui import QTextCursor
from PyQt5.QtSerialPort import QSerialPortInfo

from PyQt5 import QtWidgets, QtSerialPort, QtCore
from ui import console_ui


class TerminalApp(QtWidgets.QMainWindow, console_ui.Ui_ConsoleWindow):
    def __init__(self, port):
        super().__init__()
        self.setupUi(self)

        self.line_end = ''

        self.baudRateComboBox.addItems(map(str, QSerialPortInfo.standardBaudRates()))

        self.sendButton.clicked.connect(self.send)
        self.downbutton.clicked.connect(self.to_end)
        self.baudRateComboBox.currentIndexChanged.connect(self.change_baudrate)
        self.lineEndComboBox.currentIndexChanged.connect(self.change_line_end)

        self.serial = QtSerialPort.QSerialPort(
            port,
            baudRate=QtSerialPort.QSerialPort.Baud9600,
            readyRead=self.receive
        )
        self.serial.open(QtCore.QIODevice.ReadWrite)

    def send(self):
        print('\'', self.lineEdit.text() + self.line_end, '\'')
        self.serial.writeData((self.lineEdit.text() + self.line_end).encode())
        cursor = self.textEdit.textCursor()
        self.textEdit.moveCursor(QTextCursor.End)
        self.textEdit.insertHtml('<br><font color=\"red\">>' + self.lineEdit.text() + '</font><br>')
        self.textEdit.setTextCursor(cursor)

    def to_end(self, state):
        self.textEdit.moveCursor(QTextCursor.End)

    def change_baudrate(self, state):
        print(state)
        self.serial.setBaudRate(QSerialPortInfo.standardBaudRates()[state])

    def change_line_end(self, state):
        if state == 0:
            self.line_end = ''
        elif state == 1:
            self.line_end = '\n'
        elif state == 2:
            self.line_end = '\r'
        elif state == 3:
            self.line_end = '\r\n'

    def closeEvent(self, event):
        self.serial.close()
        event.accept()

    def receive(self):
        incoming_text = self.serial.readAll().data().decode(errors='backslashreplace')
        if len(incoming_text) > 100: #критически важно для сохранения быстродействия при некоректной скорости порта
            return
        cursor = self.textEdit.textCursor()
        self.textEdit.moveCursor(QTextCursor.End)
        self.textEdit.insertPlainText(incoming_text)
        self.textEdit.setTextCursor(cursor)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TerminalApp('COM3')
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
