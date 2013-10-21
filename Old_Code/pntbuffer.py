import numpy
from ctypes import c_void_p

from OpenGL.GL import *

class PNTBuffer():
    """Loads a vetex attribute array in init, enables it in Start
       and disables it in Stop"""
    def __init__(self, shader, data, elements, numInstances=1):
        self.numInstances=numInstances
        self.data = numpy.array(data, dtype=numpy.float32)
        self.elements = numpy.array(elements, dtype=numpy.uint16)
        self.shader = shader
        self.position = glGetAttribLocation(shader, 'position')
        self.normal = glGetAttribLocation(shader, 'normal')
        self.texCoord = glGetAttribLocation(shader, 'texCoord')
        self.n = len(elements)
        self.bufferObject = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferObject)
        glBufferData(GL_ARRAY_BUFFER, self.data, GL_STATIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

        self.elementsBufferObject = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.elementsBufferObject)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.elements, GL_STATIC_DRAW)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def Start(self):
        # do this with a vao next time?
        bytesPerFloat = 4
        bytesPerShort = 2
        
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferObject)
        glEnableVertexAttribArray(self.position)
        glEnableVertexAttribArray(self.normal)
        glEnableVertexAttribArray(self.texCoord)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.elementsBufferObject)

        # Stride is start to start:
        glVertexAttribPointer(self.position, 4,
                              GL_FLOAT, False,
                              10*bytesPerFloat,
                              c_void_p(0))
        glVertexAttribPointer(self.normal, 4,
                              GL_FLOAT, False,
                              10*bytesPerFloat,
                              c_void_p(4*bytesPerFloat))
        glVertexAttribPointer(self.texCoord, 2,
                              GL_FLOAT, False,
                              10*bytesPerFloat,
                              c_void_p(8*bytesPerFloat))
        glDrawElementsInstanced(GL_TRIANGLES,
                                self.n*bytesPerShort,
                                GL_UNSIGNED_SHORT,
                                c_void_p(0),
                                self.numInstances)

    def Stop(self):
        glDisableVertexAttribArray(self.position)
        glDisableVertexAttribArray(self.normal)
        glDisableVertexAttribArray(self.texCoord)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
