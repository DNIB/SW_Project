from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog, QFontDialog, QTextEdit, QFileDialog, QMessageBox
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
                self.dis = self.dt
                counter += self.dis
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

        self.setGeometry(300, 300, 400, 70)
        self.setWindowTitle('Arranger GUI')


        self.bt1 = QPushButton('打開檔案',self)
        self.bt1.move(50,20)
        self.bt2 = QPushButton('輸出檔案',self)
        self.bt2.move(250,20)

        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.choicefont)

        self.show()
        
    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File','./')
        if fname[0]:
            self.da.inputFile(fname[0])
                
    def choicefont(self):
        self.da.printer(4)
        QMessageBox.about(self, '提示','輸出完成!')
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
