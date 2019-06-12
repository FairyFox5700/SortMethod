from PyQt5 import QtWidgets,QtCore, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("TITLE")
window.resize(300, 50)
pal = window.palette()
pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window,
             QtGui.QBrush(QtGui.QPixmap("detective.png")))

window.setPalette(pal)
label = QtWidgets.QLabel("TEXT")
label.setAlignment(QtCore.Qt.AlignCenter)
label.setAutoFillBackground(True)
vbp=ox = QtWidgets.QVBoxLayout()
vbp.addWidget(label)
window.setLayout(vbp)
window.show()
sys.exit(app.exec_())
