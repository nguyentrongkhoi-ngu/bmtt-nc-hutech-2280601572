import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vegenere import Ui_MainWindow
import requests

class VigenereApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        payload = {
            "plain_text": self.ui.plainTextEdit.toPlainText(),
            "key": self.ui.plainTextEdit_2.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit_3.setPlainText(data.get("encrypted_text", ""))

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                self.ui.plainTextEdit_3.setPlainText("Error while calling API")
        except Exception as e:
            self.ui.plainTextEdit_3.setPlainText(f"Error: {str(e)}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        payload = {
            "cipher_text": self.ui.plainTextEdit_3.toPlainText(),
            "key": self.ui.plainTextEdit_2.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit.setPlainText(data.get("decrypted_text", ""))

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                self.ui.plainTextEdit.setPlainText("Error while calling API")
        except Exception as e:
            self.ui.plainTextEdit.setPlainText(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VigenereApp()
    window.show()
    sys.exit(app.exec_())
