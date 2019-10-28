from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog, QFontDialog, QTextEdit, QFileDialog
import sys


class dataArranger():
    def __init__(self):
        self.dis = 0.02


    def inputFile(self, file_name):
        self.fn = file_name.split('.')[0]
        f = open(file_name, 'r')
        self.s = f.readlines()
        f.close()

    def printer(self, start_line):
        sender = open(self.fn + '_result.txt', 'w')
        i = 0
        counter = 0.
        for string in self.s:
            if i == 3:
                self.dt = float(string.split()[3])
                self.dis= self.dt
                #print(self.dt)

            if i >= start_line:
                for word in string.split():
                    #print('%.2f  %s' % (counter, word))
                    sender.write('%.2f  %s\n' % (counter, word))
                    counter += self.dis
            i += 1
        sender.close()

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.da = dataArranger()

        self.initUI()
    def initUI(self):

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Arranger GUI')


        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)

        self.bt1 = QPushButton('Open File',self)
        self.bt1.move(350,20)
        self.bt2 = QPushButton('Export File',self)
        self.bt2.move(350,70)

        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.choicefont)

        self.show()
        
    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File','./')
        if fname[0]:
            self.da.inputFile(fname[0])
                
    def choicefont(self):
        self.da.printer(0)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
