from PyQt5 import QtCore, QtWidgets
import  queue
class MyThread(QtCore.QThread):
    task_dohe = QtCore.pyqtSignal(int,int, name = "taskDone")
    def __init__(self, id, queue, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.id = id
        self.queue = queue
    def run(self):
        while True:
            task = self.queue.get()
            self.sleep(5)
            self.task_dohe.emit(task, self.id)
            self.queue.task_done()

class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText("Give tasks")
        self.queue = queue.Queue()
        self.threads = []
        for i in range(1,3):
            thread = MyThread(i,self.queue)
            self.threads.append(thread)
            thread.task_dohe.connect(self.on_task_done, QtCore.Qt.QueuedConnection)
            thread.start()
        self.clicked.connect(self.on_add_task)

    def on_add_task(self):
        for i in range(0,11):
            self.queue.put(i)
    def on_task_done(self, data, id):
        print(data, "- id =", id)
if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Threads")
    window.resize(300,70)
    window.show()
    sys.exit(app.exec_())
