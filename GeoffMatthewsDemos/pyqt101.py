import os,sys,random
from PyQt4 import QtGui
from PyQt4 import QtCore

# Display random algae images in a view using QLabels
# Geoffrey Matthews
# 2013

width,height = 800,800
app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
window.setGeometry(0, 0, width, height)

pics = []
for i in range(32):
    pic = QtGui.QLabel(window)
    pic.setGeometry(random.randint(0,width-100),random.randint(0,height-100),100,100)
    pic.setPixmap(QtGui.QPixmap("images/"+["a101.png","a102.png","a103.png"][i%3]))

window.show()
sys.exit(app.exec_())
