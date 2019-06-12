from PyQt5 import QtCore, QtWidgets
class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.runing = False
        self.count =0
    def run(self):
        self.runing = True
        while self.runing:
            self.count+=1
            self.mysignal.emit("count = %s" % self.count)
            self.sleep(1)

class MYWINDOW(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Press for start")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button = QtWidgets.QPushButton('START PROCESS')
        self.button2 = QtWidgets.QPushButton('STOP PROCESS')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.button2)
        self.setLayout(self.vbox)
        self.mythread = MyThread()
        self.button.clicked.connect(self.on_started)
        self.button2.clicked.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
    def on_started(self):
        if not self.mythread.isRunning():
            self.mythread.start()
        self.label.setText("Method srart")
    def on_finished(self):
        self.mythread.runing = False
        self.label.setText("Method finish")
        self.button.setDisabled(False)
    def on_change(self,s):
        self.label.setText(s)
    def closeEvent(self, event):
        self.hide()
        self.mythread.runing = False
        self.mythread.wait(5000)
        event.accept()


if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MYWINDOW()
    window.setWindowTitle("Threads")
    window.resize(300,70)
    window.show()
    sys.exit(app.exec_())

