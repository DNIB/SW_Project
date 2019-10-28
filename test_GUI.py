import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self): # open a window
        
        self.setGeometry(300, 300, 300, 220) # specify the sindow size
        self.setWindowTitle('Icon') # specify the window title
        self.setWindowIcon(QIcon('horse.png')) # specify the window icon           
        self.show() # show the window
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv) # construct an application
    ex = Example() # create a wndow
    sys.exit(app.exec_()) # enters the main loop to catch events and exits until closing window