from PyQt5 import QtWidgets,QtCore, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("TITLE")
window.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
window.resize(1220, 500)
pixmap = QtGui.QPixmap("Circle_Blue.png")
pal = window.palette()
pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window,
             QtGui.QBrush(pixmap))
pal.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window,
             QtGui.QBrush(pixmap))


window.setPalette(pal)
button = QtWidgets.QPushButton("CLOSE WINDOW", window)
button.setFixedSize(1500,300)
button.move(75,135)
button.clicked.connect(QtWidgets.qApp.quit)

window.show()
sys.exit(app.exec_())
