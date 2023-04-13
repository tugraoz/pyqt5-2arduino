import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import serial

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
class ArduinoController(QMainWindow):
    def __init__(self):
        super().__init__()

        # Birinci Arduino Butonları
        self.stepper_motor_saat_yonu_buton = QPushButton('Stepper Motoru Saat Yönünde Döndür', self)
        self.stepper_motor_saat_yonu_buton.move(20, 50)
        self.stepper_motor_saat_yonu_buton.clicked.connect(self.stepper_motor_saat_yonu)

        self.stepper_motor_ters_yonu_buton = QPushButton('Stepper Motoru Ters Yönde Döndür', self)
        self.stepper_motor_ters_yonu_buton.move(220, 50)
        self.stepper_motor_ters_yonu_buton.clicked.connect(self.stepper_motor_ters_yonu)

        # İkinci Arduino Butonları
        self.stepper_motor_saat_yonu_buton_2 = QPushButton('Stepper Motoru Saat Yönünde Döndür (Arduino 2)', self)
        self.stepper_motor_saat_yonu_buton_2.move(20, 150)
        self.stepper_motor_saat_yonu_buton_2.clicked.connect(self.stepper_motor_saat_yonu_2)

        self.stepper_motor_ters_yonu_buton_2 = QPushButton('Stepper Motoru Ters Yönde Döndür (Arduino 2)', self)
        self.stepper_motor_ters_yonu_buton_2.move(220, 150)
        self.stepper_motor_ters_yonu_buton_2.clicked.connect(self.stepper_motor_ters_yonu_2)

        # Dönüş Sayısı Girişi
        self.donus_sayisi_label = QLabel('Dönüş Sayısı:', self)
        self.donus_sayisi_label.move(20, 250)
        self.donus_sayisi_girisi = QLineEdit(self)
        self.donus_sayisi_girisi.move(120, 250)

        # Arduino Bağlantısı
        self.serial_port = serial.Serial('COM3', 9600)
        self.serial_port_2 = serial.Serial('COM4', 9600) # İkinci Arduino'nun bağlantı noktası
        self.setWindowTitle('Arduino Control Program')
        self.setGeometry(100, 100, 400, 400)
        self.show()

    @pyqtSlot()
    def stepper_motor_saat_yonu(self):
        donus_sayisi = self.donus_sayisi_girisi.text()
        if donus_sayisi:
             donus_sayisi = int(donus_sayisi)
             for i in range(donus_sayisi):
                  self.serial_port.write(b'1')
    @pyqtSlot()
    def stepper_motor_ters_yonu(self):
        donus_sayisi = self.donus_sayisi_girisi.text()
        if donus_sayisi:
             donus_sayisi = int(donus_sayisi)
             for i in range(donus_sayisi):
                  self.serial_port.write(b'2')
 
    def stepper_motor_saat_yonu_2(self):
                donus_sayisi = self.donus_sayisi_girisi.text()
                if donus_sayisi:
                     donus_sayisi = int(donus_sayisi)
                     for i in range(donus_sayisi):
                          self.serial_port_2.write(b'3')

    def stepper_motor_ters_yonu_2(self):
        donus_sayisi = self.donus_sayisi_girisi.text()
        if donus_sayisi:
             donus_sayisi = int(donus_sayisi)
             for i in range(donus_sayisi):
                self.serial_port_2.write(b'4')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ArduinoController()
    ex.stepper_motor_saat_yonu_2()
    ex.stepper_motor_ters_yonu_2()
    sys.exit(app.exec_())
