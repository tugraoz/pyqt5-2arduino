import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QComboBox
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import serial
from serial import SerialException
import serial.tools.list_ports as list_ports
from PyQt5.QtGui import QDoubleValidator

class ArduinoController(QMainWindow):
    def __init__(self):
        super().__init__()
     

    
        # First Stepper Motor Buttons
        self.stepper_motor_clockwise_button = QPushButton('clockwise ', self)
        self.stepper_motor_clockwise_button.move(20, 200)
        self.stepper_motor_clockwise_button.clicked.connect(self.stepper_motor_clockwise)
        self.stepper_motor_anticlockwise_button = QPushButton('Anticlockwise ', self)
        self.stepper_motor_anticlockwise_button.move(200, 200)
        self.stepper_motor_anticlockwise_button.clicked.connect(self.stepper_motor_anticlockwise)
        
        self.returns_count_label = QLabel('Returns Count:', self)
        self.returns_count_label.move(20, 50)
        self.returns_count = QLineEdit(self)
        self.returns_count.move(120, 50)
 

        self.returns_count_2_label = QLabel('Returns Count_2:', self)
        self.returns_count_2_label.move(120, 50)
        self.returns_count_2 = QLineEdit(self)
        self.returns_count_2.move(120, 50)

         # COM Port Selection for Stepper Motor 1
        self.com_port_label1 = QLabel('Motor 2', self)
        self.com_port_label1.move(20, 240)
        self.com_port_combo1 = QComboBox(self)
        self.com_port_combo1.move(330, 200)
        self.refresh_com_ports(self.com_port_combo1)

        self.connect_button = QPushButton('Connect', self)
        self.connect_button.move(450, 200)
        self.connect_button.clicked.connect(self.connect_arduino)
        self.serial_port = None
    
        # Second Stepper Motor Buttons
        self.stepper_motor_clockwise_2button = QPushButton('Clockwise ', self)
        self.stepper_motor_clockwise_2button.move(20, 270)
        self.stepper_motor_clockwise_2button.clicked.connect(self.stepper_motor_clockwise_2)
        self.stepper_motor_anticlockwise_2button = QPushButton('antiClockwise ', self)
        self.stepper_motor_anticlockwise_2button.move(200, 270)
        self.stepper_motor_anticlockwise_2button.clicked.connect(self.stepper_motor_counterclockwise_2)
         # COM Port Selection for Stepper Motor 2
         
        self.com_port_label2 = QLabel('Motor 1', self)
        self.com_port_label2.move(20, 170)
        self.com_port_combo2 = QComboBox(self)
        self.com_port_combo2.move(330, 270)
        self.refresh_com_ports(self.com_port_combo2)

        self.connect_button = QPushButton('Connect', self)
        self.connect_button.move(450, 270)
        self.connect_button.clicked.connect(self.connect_arduino_2)
        self.serial_port_2 = None

         # Input Number of Returns
        self.returns_count_label = QLabel('Returns Count:', self)
        self.returns_count_label.move(20, 50)
        self.returns_count = QLineEdit(self)
        self.returns_count.move(120, 50)
        self.returns_count.setValidator(QDoubleValidator())  # Allow decimal input

        self.returns_count_label = QLabel('Returns Count_2', self)
        self.returns_count_label.move(20, 50)
        self.returns_count = QLineEdit(self)
        self.returns_count.move(120, 50)
        self.returns_count.setValidator(QDoubleValidator())  # Allow decimal input


        self.setWindowTitle('Arduino Control Program')
        self.setGeometry(200, 200, 650, 450)
        self.show()

    def refresh_com_ports(self, combo):
        combo.clear()
        ports = list_ports.comports()
        for port in ports:
            combo.addItem(port.device)

    def connect_arduino(self, com_port):
        com_port = self.com_port_combo1.currentText()
        try:
            self.serial_port = serial.Serial(com_port, 9600)
        except SerialException:
            QMessageBox.critical(self, "Serial Port Error", "{} port is not available!".format(com_port))

    def connect_arduino_2(self):
        com_port = self.com_port_combo2.currentText()
        try:
            self.serial_port_2 = serial.Serial(com_port, 9600)
        except SerialException:
            QMessageBox.critical(self, "Serial Port Error", "{} port is not available!".format(com_port))

    @pyqtSlot()
    def stepper_motor_clockwise(self):
       port = self.com_port_combo1.currentText()
       if port:
            returns_count = self.returns_count.text()
            if returns_count:
                returns_count = (returns_count).encode()
            self.serial_port.write(returns_count)
       else:
            QMessageBox.critical(self, "Serial Port Error", "Serial port is not available!")


    @pyqtSlot()
    def stepper_motor_anticlockwise(self):
        port = self.com_port_combo1.currentText()
        if port:
            returns_count = -1 * float(self.returns_count.text())
            if returns_count:
                returns_count = (str(returns_count)).encode()
            self.serial_port.write(returns_count)
        else:
            QMessageBox.critical(self, "Serial Port Error", "Serial port is not available!")



    @pyqtSlot()
    def stepper_motor_clockwise_2(self):
        port = self.com_port_combo2.currentText()
        if port:
            returns_count = self.returns_count.text()
            if returns_count:
                returns_count = (returns_count).encode()      
            self.serial_port_2.write(returns_count)
        else:
            QMessageBox.critical(self, "Serial Port Error", "Serial port is not available!")
    
    @pyqtSlot()
    def stepper_motor_counterclockwise_2(self):
        port = self.com_port_combo2.currentText()
        if port:
            returns_count = -1 * float(self.returns_count.text())
            if returns_count:
                returns_count = (str(returns_count)).encode()
                self.serial_port_2.write(returns_count)
        else:
            QMessageBox.critical(self, "Serial Port Error", "Serial port is not available!")
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ArduinoController()
    sys.exit(app.exec_())               