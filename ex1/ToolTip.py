from PyQt5 import QtWidgets,QtCore, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget(flags=QtCore.Qt.Dialog)
window.setWindowTitle("TITLE")
window.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
window.resize(1220, 500)
button = QtWidgets.QPushButton("CLOSE WINDOW", window)
button.setFixedSize(100,300)
button.move(75,135)
button.setToolTip("TOOOLTIP")
button.setToolTipDuration(3000)
window.setToolTip("TOOLWINDOW")
window.setToolTipDuration(5000)
button.setWhatsThis("HELP FOR BUTTOn")
button.clicked.connect(QtWidgets.qApp.quit)

window.show()
sys.exit(app.exec_())
