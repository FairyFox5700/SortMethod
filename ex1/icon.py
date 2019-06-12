from PyQt5 import QtWidgets,QtCore, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("TITLE")
window.resize(300, 50)
ico = QtGui.QIcon("icon.png")
window.setWindowIcon(ico)
app.setWindowIcon(ico)
window.show()
sys.exit(app.exec_())
