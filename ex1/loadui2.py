from PyQt5 import QtWidgets, uic

class MYWINDOW(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi("untitled.ui",self)
        self.pushButton.clicked.connect(QtWidgets.qApp.quit)

if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MYWINDOW()
    window.show()
    sys.exit(app.exec_())
