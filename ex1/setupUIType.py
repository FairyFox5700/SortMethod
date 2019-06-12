from PyQt5 import QtWidgets, uic

class MYWINDOW(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        Form, BASE =uic.loadUiType("untitled.ui")
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(QtWidgets.qApp.quit)


if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MYWINDOW()
    window.show()
    sys.exit(app.exec_())
