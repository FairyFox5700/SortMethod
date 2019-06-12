from PyQt5 import QtWidgets,QtCore, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("TITLE")
window.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
window.resize(1220, 500)
button = QtWidgets.QPushButton("CLOSE WINDOW", window)
button.setFixedSize(1500,300)
button.move(75,135)
button.clicked.connect(window.close)

window.show()
sys.exit(app.exec_())
