#Chạy lệnh pip install PyQt5 để cài đặt thư viện
import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from test import Ui_Form

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.uic = Ui_Form()
        self.uic.setupUi(self)
        
                 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Main()
    main_win.show()
    sys.exit(app.exec())

#install
pip install PyMySQL
