import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLineEdit,
                               QRadioButton, QPushButton, QMessageBox,
                               QSpinBox, QLabel)
from PySide2.QtGui import Qt, QIcon
from PySide2.QtCore import Slot
from ui_form import Ui_RC5


class RC5(QWidget):
    def __init__(self):
        super(RC5, self).__init__()
        self.ui = Ui_RC5()
        self.ui.setupUi(self)
        self.setFixedHeight(395)

        self.encrypt = True

        self.lineEdit = self.findChild(QLineEdit, "lineEdit")
        self.lineEdit2 = self.findChild(QLineEdit, "lineEdit_2")
        self.lineEdit3 = self.findChild(QLineEdit, "lineEdit_3")
        self.label = self.findChild(QLabel, "label")
        self.label3 = self.findChild(QLabel, "label_3")
        self.spinBox = self.findChild(QSpinBox, "spinBox")
        self.radioButton = self.findChild(QRadioButton, "radioButton")
        self.radioButton2 = self.findChild(QRadioButton, "radioButton_2")
        self.radioButton3 = self.findChild(QRadioButton, "radioButton_3")
        self.button = self.findChild(QPushButton, "pushButton")
        self.button2 = self.findChild(QPushButton, "pushButton_2")

        self.lineEdit.setFocus()

        self.button.clicked.connect(self.button_clicked)
        self.button2.clicked.connect(self.button2_clicked)

    # Обработка нажатия ESC и ENTER
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Return:
            self.button.click()

    # Обработка нажатия кнопки Зашифровать / Расшифровать
    @Slot()
    def button_clicked(self):
        if self.encrypt:  # Шифрование
            if len(self.lineEdit.text()) == 0:
                QMessageBox.critical(
                    self, "Ошибка", "Отсутствует открытый текст!")
                return

            if self.radioButton.isChecked():
                if len(self.lineEdit.text()) > 4:
                    QMessageBox.critical(
                        self, "Ошибка", "Текст содержит больше 4 символов!")
                    return
                w = 16
            elif self.radioButton2.isChecked():
                if len(self.lineEdit.text()) > 8:
                    QMessageBox.critical(
                        self, "Ошибка", "Текст содержит больше 8 символов!")
                    return
                w = 32
            elif self.radioButton3.isChecked():
                if len(self.lineEdit.text()) > 16:
                    QMessageBox.critical(
                        self, "Ошибка", "Текст содержит больше 16 символов!")
                    return
                w = 64

            if len(self.lineEdit2.text()) > 255:
                QMessageBox.critical(
                    self, "Ошибка", "Ключ содержит больше 255 символов!")
                return

            r = self.spinBox.value()
            text = self.lineEdit.text().encode()
            key = self.lineEdit2.text().encode()

            with open("source.txt", 'wb') as inp:
                inp.write(text)
            with open("encrypted.txt", 'wb') as out:
                out.close()

            inp = "source.txt"
            out = "encrypted.txt"

            self.setValues(w, r, key)
            self.encryptFile(inp, out)

            self.lineEdit3.setText((self.encryptBytes(text)).hex().upper())
        else:  # Расшифрование
            if len(self.lineEdit.text()) == 0:
                QMessageBox.critical(
                    self, "Ошибка", "Отсутствует зашифрованный текст!")
                return

            try:
                text = bytearray.fromhex(self.lineEdit.text())
            except ValueError as e:
                QMessageBox.critical(
                    self, "Ошибка", "Зашифрованный текст не в 16 сс!")
                return

            if len(self.lineEdit2.text()) > 255:
                QMessageBox.critical(
                    self, "Ошибка", "Ключ содержит больше 255 символов!")
                return

            if self.radioButton.isChecked():
                w = 16
            elif self.radioButton2.isChecked():
                w = 32
            elif self.radioButton3.isChecked():
                w = 64

            r = self.spinBox.value()
            key = self.lineEdit2.text().encode()

            with open("source.txt", 'wb') as inp:
                inp.write(text)
            with open("encrypted.txt", 'wb') as out:
                out.close()

            inp = "source.txt"
            out = "decrypted.txt"

            self.setValues(w, r, key)
            self.decryptFile(inp, out)

            self.lineEdit3.setText((self.decryptBytes(text)).hex().upper())

    # Обработка нажатия кнопки с замком
    @Slot()
    def button2_clicked(self):
        if self.encrypt:
            self.encrypt = False
            self.button2.setIcon(QIcon(":/images/dec.png"))
            self.button.setText("Расшифровать")
            self.label.setText("Зашифрованный текст (16 сс):")
            self.label3.setText("Расшифрованный текст (16 сс):")
        else:
            self.encrypt = True
            self.button2.setIcon(QIcon(":/images/enc.png"))
            self.button.setText("Зашифровать")
            self.label.setText("Открытый текст:")
            self.label3.setText("Зашифрованный текст (16 сс):")

    # Установка значений RC5-w/r/b и запуск процедуры расширения ключа
    def setValues(self, w, r, key):
        self.w = w  # Половина длины блока (16, 32, 64 бит)
        self.r = r  # Число раундов (1-255)
        self.K = key  # Ключ
        self.b = len(self.K)  # Длина ключа (0-2040 бит)
        self.mod = 2 ** self.w
        self.t = 2 * (r + 1)
        self.u = w // 8
        self.w4 = w // 4
        self.mask = self.mod - 1

        self.__keyAlign()
        self.__keyExtend()
        self.__shuffle()

    # Битовый сдвиг влево
    def __lshift(self, val, n):
        n %= self.w
        return ((val << n) & self.mask) | ((val & self.mask) >> (self.w - n))

    # Битовый сдвиг вправо
    def __rshift(self, val, n):
        n %= self.w
        return ((val & self.mask) >> n) | (val << (self.w - n) & self.mask)

    # Генерация констант P и Q
    def __const(self):
        if self.w == 16:
            return 0xB7E1, 0x9E37
        elif self.w == 32:
            return 0xB7E15163, 0x9E3779B9
        elif self.w == 64:
            return 0xB7E151628AED2A6B, 0x9E3779B97F4A7C15

    # Выравнивание ключа
    def __keyAlign(self):
        if self.b == 0:  # Пустой ключ
            self.c = 1
        elif self.b % self.u:  # Ключ не кратен w / 8
            # Дополнение ключа нулевыми байтами
            self.K += b'\x00' * (self.u - self.b % self.u)
            self.b = len(self.K)
            self.c = self.b // self.u
        else:
            self.c = self.b // self.u
        L = [0] * self.c
        for i in range(self.b - 1, -1, -1):  # Заполнение массива L
            L[i // self.u] = (L[i // self.u] << 8) + self.K[i]
        self.L = L

    # Инициализация массива расширенных ключей S
    def __keyExtend(self):
        P, Q = self.__const()
        self.S = [(P + i * Q) % self.mod for i in range(self.t)]

    # Перемешивание
    def __shuffle(self):
        i, j, G, H = 0, 0, 0, 0
        for k in range(3 * max(self.c, self.t)):
            G = self.S[i] = self.__lshift((self.S[i] + G + H), 3)
            H = self.L[j] = self.__lshift((self.L[j] + G + H), G + H)
            i = (i + 1) % self.t
            j = (j + 1) % self.c

    # Шифрование блока
    def encryptBlock(self, data):
        A = int.from_bytes(data[:self.u], byteorder='little')
        B = int.from_bytes(data[self.u:], byteorder='little')
        A = (A + self.S[0]) % self.mod
        B = (B + self.S[1]) % self.mod
        for i in range(1, self.r + 1):
            A = (self.__lshift((A ^ B), B) + self.S[2 * i]) % self.mod
            B = (self.__lshift((A ^ B), A) + self.S[2 * i + 1]) % self.mod
        return (A.to_bytes(self.u, byteorder='little')
                + B.to_bytes(self.u, byteorder='little'))

    # Расшифрование блока
    def decryptBlock(self, data):
        A = int.from_bytes(data[:self.u], byteorder='little')
        B = int.from_bytes(data[self.u:], byteorder='little')
        for i in range(self.r, 0, -1):
            B = self.__rshift(B - self.S[2 * i + 1], A) ^ A
            A = self.__rshift(A - self.S[2 * i], B) ^ B
        B = (B - self.S[1]) % self.mod
        A = (A - self.S[0]) % self.mod
        return (A.to_bytes(self.u, byteorder='little')
                + B.to_bytes(self.u, byteorder='little'))

    # Шифрование файла
    def encryptFile(self, inpFileName, outFileName):
        with open(inpFileName, 'rb') as inp, open(outFileName, 'wb') as out:
            run = True
            while run:
                text = inp.read(self.w4)
                if not text:
                    break
                if len(text) != self.w4:
                    text = text.ljust(self.w4, b'\x00')
                    run = False
                text = self.encryptBlock(text)
                out.write(text)

    # Расшифрование файла
    def decryptFile(self, inpFileName, outFileName):
        with open(inpFileName, 'rb') as inp, open(outFileName, 'wb') as out:
            run = True
            while run:
                text = inp.read(self.w4)
                if not text:
                    break
                if len(text) != self.w4:
                    run = False
                text = self.decryptBlock(text)
                if not run:
                    text = text.rstrip(b'\x00')
                out.write(text)

    # Шифрование массива байт
    def encryptBytes(self, data):
        res, run = b'', True
        while run:
            temp = data[:self.w4]
            if len(temp) != self.w4:
                data = data.ljust(self.w4, b'\x00')
                run = False
            res += self.encryptBlock(temp)
            data = data[self.w4:]
            if not data:
                break
        return res

    # Расшифрование массива байт
    def decryptBytes(self, data):
        res, run = b'', True
        while run:
            temp = data[:self.w4]
            if len(temp) != self.w4:
                run = False
            res += self.decryptBlock(temp)
            data = data[self.w4:]
            if not data:
                break
        return res.rstrip(b'\x00')


if __name__ == "__main__":
    app = QApplication([])
    widget = RC5()
    widget.show()
    sys.exit(app.exec_())
