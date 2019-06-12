from PyQt5 import QtCore
r = QtCore.QRect()
print(r.left(),r.right(), r.top(), r.bottom(),r.width(),r.height())
r = QtCore.QRect(10,15,20,23)
print(r.left(),r.right(), r.top(), r.bottom(),r.width(),r.height())
r = QtCore.QRect(QtCore.QPoint(10,15),QtCore.QSize(400,300))
print(r.left(),r.right(), r.top(), r.bottom(),r.width(),r.height())
r = QtCore.QRect(QtCore.QPoint(10,15),QtCore.QPoint(110,115))
print(r.left(),r.right(), r.top(), r.bottom(),r.width(),r.height())
r.setCoords(12,212,13,11)
# уменьщение границ
m = QtCore.QMargins(2,10,2,10)
r2 = r.marginsRemoved(m)
print(r2)
# увелечение границ
m = QtCore.QMargins(2,10,2,10)
r2 = r.marginsAdded(m)
print(r2)
r2.moveTo(0,0)
print(r)
#перемещение по координатам верх и низ
r.translate(20,15)
print(r)
#перемещение по координатам левого верххнего и правого нижнего
r.adjust(10,4,3,1)
print(r)
print(r.getCoords(), r.getRect())
#лыво быльше права ы верх быльше низу
r = QtCore.QRect(QtCore.QPoint(409,315),QtCore.QPoint(10,15))
print(r)
print(r.normalized())
print(r.contains(409,315))
print(r.intersects(QtCore.QRect(10,15,20,20)))
print(r.united(QtCore.QRect(120,125,202,220)))

