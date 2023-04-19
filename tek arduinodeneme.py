import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import serial
from serial import SerialException

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

class ArduinoController(QMainWindow):
    def __init__(self):
        super().__init__()
        # First Arduino Buttons
        self.stepper_motor_clock_side_button = QPushButton('Rotate Magnet Height Rotater In The  Clockwise', self)
        self.stepper_motor_clock_side_button.move(20, 50)
        self.stepper_motor_clock_side_button.clicked.connect(self.stepper_motor_clock_side)

        self.stepper_motor_reverse_side_button = QPushButton('Rotate Magnet Height Rotater In The Anti-Clockwise', self)
        self.stepper_motor_reverse_side_button.move(220, 50)
        self.stepper_motor_reverse_side_button.clicked.connect(self.stepper_motor_reverse_side_)
        # Second Arduino Buttons
        self.stepper_motor_clock_side_button_2 = QPushButton('Rotate Magnet In The Clockwise ', self)
        self.stepper_motor_clock_side_button_2.move(20, 150)
        self.stepper_motor_clock_side_button_2.clicked.connect(self.stepper_motor_clock_side_2)

        self.stepper_motor_reverse_side_button2 = QPushButton('Rotate Magnet In The Anti-Clockwise ', self)
        self.stepper_motor_reverse_side_button2.move(220, 150)
        self.stepper_motor_reverse_side_button2.clicked.connect(self.stepper_motor_reverse_side2)

        # Input Number of Returns
        self.returns_count_label = QLabel('returns_count:', self)
        self.returns_count_label.move(20, 250)
        self.returns_count = QLineEdit(self)
        self.returns_count.move(120, 250)

        # Arduino Connection
        try:
            self.serial_port = serial.Serial('COM5', 9600)
        except SerialException:
            QMessageBox.critical(self, "Serial Port Error", "COM3 port is not available!")

        try:
            self.serial_port_2 = serial.Serial('COM4', 9600) # Port of the second Arduino
        except SerialException:
            QMessageBox.critical(self, "Serial Port Error", "COM4 port is not available!")

        self.setWindowTitle('Arduino Control Program')
        self.setGeometry(100, 100, 400, 400)
        self.show()

    @pyqtSlot()
    def stepper_motor_clock_side(self):
        returns_count = self.returns_count.text()
        if returns_count:
            return_count = int(returns_count)
            for i in range(return_count):
                self.serial_port.write(b'1')

    @pyqtSlot()
    def stepper_motor_reverse_side_(self):
        returns_count = self.returns_count.text()
        if returns_count:
            return_count = int(returns_count)
            for i in range(return_count):
                self.serial_port.write(b'2')

    def stepper_motor_clock_side_2(self):
        returns_count = self.returns_count.text()
        if returns_count:
             return_count = int(returns_count)
             for i in range(return_count):
                self.serial_port_2.write(b'1')

    def stepper_motor_reverse_side2(self):
        returns_count = self.returns_count.text()
        if returns_count:
             return_count = int(returns_count)
             for i in range(return_count):
                self.serial_port_2.write(b'2')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ArduinoController()
    ex.stepper_motor_clock_side_2()
    ex.stepper_motor_reverse_side2()
    sys.exit(app.exec_())

    
