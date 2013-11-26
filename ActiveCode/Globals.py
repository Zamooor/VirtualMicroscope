"""==========================================================================

All GLobal Variables

=========================================================================="""
from PyQt4 import QtCore, QtGui,QtOpenGL
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from algaeTable import *
algaeTable=AlgaeTable()
#algaeTable=None 

class Pixmap(QtCore.QObject):
    def __init__(self, pix):
        super(Pixmap, self).__init__()

        self.pixmap_item = QtGui.QGraphicsPixmapItem(pix)
        self.pixmap_item.setCacheMode(QtGui.QGraphicsItem.DeviceCoordinateCache)
        self.pixmap_item.setScale(.03)
    def _set_pos(self, pos):
        self.pixmap_item.setPos(pos)

    def setRot(self, angle):
        self.pixmap_item.setRotation(angle)

    def setScaleVariance(self, var):
        self.pixmap_item.setScale(self.pixmap_item.scale() + var)

    pos = QtCore.pyqtProperty(QtCore.QPointF, fset=_set_pos)

def New_Session():
    global algaeTable
    algaeTable = AlgaeTable()
