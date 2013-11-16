import os,sys,random
from PyQt4 import QtGui
from PyQt4 import QtCore

# Display random algae images in a view using QPixmaps
# Code modelled on animatedtiles PyQt demo
# Geoffrey Matthews
# 2013

### Class borrowed from animatedtiles demo:
# PyQt doesn't support deriving from more than one wrapped class so we use
# composition and delegate the property.
class Pixmap(QtCore.QObject):
    def __init__(self, pix):
        super(Pixmap, self).__init__()

        self.pixmap_item = QtGui.QGraphicsPixmapItem(pix)
        self.pixmap_item.setCacheMode(QtGui.QGraphicsItem.DeviceCoordinateCache)

    def _set_pos(self, pos):
        self.pixmap_item.setPos(pos)

    pos = QtCore.pyqtProperty(QtCore.QPointF, fset=_set_pos)
    
width,height = 800,800
app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
window.setGeometry(0, 0, width, height)
scene = QtGui.QGraphicsScene(-400,-400,800,800)
view = QtGui.QGraphicsView(scene)

pics = []
for i in range(32):
    item = (Pixmap(QtGui.QPixmap("images/"+["a101.png","a102.png","a103.png"][i%3])))
    item.pos = QtCore.QPointF(random.randint(-300,300), random.randint(-300,300))
    pics.append(item)
    scene.addItem(item.pixmap_item)

view.show()
sys.exit(app.exec_())
