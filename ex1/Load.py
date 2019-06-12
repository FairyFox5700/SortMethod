from PyQt5 import QtCore, QtWidgets, QtGui
import  time

class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText("CLOSE WINDOW")
        self.clicked.connect(QtWidgets.qApp.quit)
    def load_data(self, sp):
        for i in range(1,11):
            time.sleep(2)
            sp.showMessage("LOADING...{0}%".format(i*10), QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom, QtCore.Qt.black)
            QtWidgets.qApp.processEvents()

if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("detective.png"))
    splash.showMessage("LOADING...{0}%", QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom, QtCore.Qt.black)
    splash.show()
    QtWidgets.qApp.processEvents()
    window = MyWindow()
    window.setWindowTitle("Threads")
    window.resize(300,30)
    window.show()
    sys.exit(app.exec_())
