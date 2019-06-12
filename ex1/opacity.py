from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("TITLE")
window.resize(300, 50)
window.setWindowOpacity(0.6)
window.show()
print(window.windowOpacity())
sys.exit(app.exec_())
