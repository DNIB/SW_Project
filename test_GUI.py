from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog, QFontDialog, QTextEdit, QFileDialog
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Learn PyQt5')


        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)

        self.bt1 = QPushButton('Open File',self)
        self.bt1.move(350,20)
        self.bt2 = QPushButton('Choose Font',self)
        self.bt2.move(350,70)
        self.bt3 = QPushButton('Choose Color',self)
        self.bt3.move(350,120)

        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.choicefont)
        self.bt3.clicked.connect(self.choicecolor)

        self.show()
    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File','./')
        if fname[0]:
            with open(fname[0], 'r',errors='ignore') as f:
                self.tx.setText(f.read()) 
    def choicefont(self):
        font, ok = QFontDialog.getFont() 
        if ok:
            self.tx.setCurrentFont(font)
    def choicecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.tx.setTextColor(col)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
