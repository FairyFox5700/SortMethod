from PyQt5 import QtCore, QtWidgets
class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(int)
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.count =0
    def run(self):
        self.exec_()
    def on_started(self):
        self.count+=1
        self.mysignal.emit(self.count)

class THREAD2(QtCore.QThread):
    s2 = QtCore.pyqtSignal(str)
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
    def run(self):
        self.exec_()
    def on_change(self,i):
        i +=10
        self.s2.emit("%d"%i)



class MYWINDOW(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Press for start")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button = QtWidgets.QPushButton('START PROCESS')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.mythread = MyThread()
        self.mythread2 = THREAD2()
        self.mythread.start()
        self.mythread2.start()
        self.button.clicked.connect(self.mythread.on_started)
        self.mythread.mysignal.connect(self.mythread2.on_change)
        self.mythread2.s2.connect(self.on_thear2_s2)

    def on_thear2_s2(self,s):
        self.label.setText(s)


if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MYWINDOW()
    window.setWindowTitle("Threads")
    window.resize(300,70)
    window.show()
    sys.exit(app.exec_())

