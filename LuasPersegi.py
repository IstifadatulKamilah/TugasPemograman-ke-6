import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class tugas2(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
        self.setGeometry(300,300, 300,250)
        self.setWindowTitle('Luas Persegi')
        self.show()
    def UI(self):
        lbljudul = QLabel('Menghitung Luas Persegi Panjang',self)
        lbljudul.setStyleSheet('font-size:20px;')
        lbljudul.setAlignment(Qt.AlignCenter)

        lblp = QLabel('Masukkan Panjang :',self)
        self.lep = QLineEdit(self)

        lbll = QLabel('Masukkan Lebar :',self)
        self.lel = QLineEdit(self)
        
        bhitung = QPushButton('Hitung',self)
        bhitung.clicked.connect(self.hitung)

        breset = QPushButton('Reset',self)
        breset.clicked.connect(self.reset)

        self.status = QLabel('Status',self)
        self.hasil = QLabel('Hasil : ',self)
        self.hasil.setAlignment(Qt.AlignCenter)
        self.hasil.setStyleSheet('font-size:16px;')
        
        layout = QGridLayout()
        layout.addWidget(lbljudul , 0,0,1,2)
        layout.addWidget(lblp, 1,0)
        layout.addWidget(self.lep, 1,1)
        layout.addWidget(lbll, 2,0)
        layout.addWidget(self.lel, 2,1)
        layout.addWidget(bhitung, 3,0,1,2)
        layout.addWidget(breset, 4,0,1,2)
        layout.addWidget(self.hasil,5,0,1,2)
        layout.addWidget(self.status,6,0,1,2)

        self.setLayout(layout)

    def hitung(self):
        if len(self.lel.text()) == 0 or len(self.lep.text()) == 0:
            self.status.setText('Harap Diisi')
        else :
            p = int(self.lep.text())
            l = int(self.lel.text())
            hasil = p * l
            self.hasil.setText('Hasil : '+str(hasil))
    def reset(self):
        self.lep.setText('')
        self.lel.setText('')
        self.hasil.setText('Hasil : ')
        self.status.setText('Data berhasil di reset')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = tugas2()
    sys.exit(app.exec_())
