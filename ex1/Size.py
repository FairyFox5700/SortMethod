from PyQt5 import QtCore
s1 = QtCore.QSize()
s2 =  QtCore.QSize(10,33)
s3 =  QtCore.QSize(s2)
print(s1, s2, s3)
s1.setHeight(124)
s =  QtCore.QSize(10,33)
# нарушение пропорций
s.scale(70,60,QtCore.Qt.IgnoreAspectRatio)
# без нарушение пропорцийб старая область
s.scale(70,60,QtCore.Qt.KeepAspectRatio)
# без нарушение пропорцийб новая область
s.scale(70,60,QtCore.Qt.KeepAspectRatioByExpanding)
#min size
print(s.boundedTo(QtCore.QSize(23414,1232)))
#max.size
print(s.expandedTo(QtCore.QSize(23414,1232)))
s.transpose()
print(s)
