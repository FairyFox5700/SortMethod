from PyQt5 import QtWidgets,QtCore
import sys

def show_modal_window():
    global modal_window
    modal_window = QtWidgets.QWidget(window1, QtCore.Qt.Window)
    modal_window.setWindowTitle("MODAL")
    modal_window.resize(200,120)
    modal_window.setWindowModality(QtCore.Qt.WindowModal)
    modal_window.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
    modal_window.move(window1.geometry().center() - modal_window.rect().center() -
                      QtCore.QPoint(4,30))
    modal_window.show()

app = QtWidgets.QApplication(sys.argv)
window1 = QtWidgets.QWidget()
window1.setWindowTitle("TITLE")
window1.resize(300, 50)
button = QtWidgets.QPushButton("OPEN MODAL WINDOW")
button.clicked.connect(show_modal_window)
vbp=ox = QtWidgets.QVBoxLayout()
vbp.addWidget(button)
window1.setLayout(vbp)
window1.show()

window2 = QtWidgets.QWidget()
window2.setWindowTitle("TITLE2")
window2.resize(300, 50)
window2.show()

sys.exit(app.exec_())

