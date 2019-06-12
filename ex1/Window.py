from PyQt5 import QtWidgets, QtCore, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("TITLE")
window.resize(300, 50)
window.setGeometry(QtCore.QRect(100,100,100,60))
rect = window.geometry()
print(rect.left(), rect.top(), rect.width(), rect.height())
window.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint | QtCore.Qt.WindowContextHelpButtonHint )
window.move(window.width() * -2, 0)
window.show()
desktop = QtWidgets.QDesktopWidget().screenGeometry(-1)
#center
x = (desktop.width()- window.width())//2
y =  (desktop.height()-window.height())//2
window.move(x,y)
#right top
x =  (desktop.width()-window.frameSize().width())
window.move(x,0)
sys.exit(app.exec_())
#right buttom
desktop = QtWidgets.QDesktopWidget()
taskBARHeight = (desktop.screenGeometry(-1).height()- desktop.availableGeometry().height())
