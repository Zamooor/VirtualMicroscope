import os

from OpenGL.GL import *

import pygame
from pygame.locals import *

import numpy 
from ctypes import c_void_p

#from shader import getShader
#from transforms import *
#from parametricsurface import ParametricSurface
#from pntbuffer import PNTBuffer
#from uniforms import Uniforms
#from drawable import Mesh
#from frame import Frame

class ParametricSurface():
    def __init__(self, point, norm = None, tex = None,
                 sRange = None, tRange = None):
        self.point = point
        if norm != None:
            self.norm = norm
        if tex != None:
            self.tex = tex
        if sRange != None:
            self.sRange = sRange
        else:
            self.sRange = numpy.arange(0.0, 1.1, 0.1)
        if tRange != None:
            self.tRange = tRange
        else:
            self.tRange = numpy.arange(0.0, 1.1, 0.1)
        self.createBuffer()
        
    def norm(self, s, t):
        a = numpy.array(self.point(s, t), dtype=numpy.float32)[0:3]
        b = numpy.array(self.point(s+0.001, t), dtype=numpy.float32)[0:3]
        c = numpy.array(self.point(s, t+0.001), dtype=numpy.float32)[0:3]
        v1 = c-a
        v2 = b-a
        n = numpy.cross(v1, v2)
        denom = numpy.sqrt(numpy.dot(n,n))
        if denom > 0.0:
            n /= numpy.sqrt(numpy.dot(n,n))
        n = list(n)
        n.append(0.0)
        return n

    def tex(self, s, t):
        return [s,t]

    def createBuffer(self):
        # TODO: convert these to strips (natural for param surfaces)
        vertices = []
        for s in self.sRange:
            for t in self.tRange:
                p00 = self.point(s,t)
                n00 = self.norm(s,t)
                t00 = self.tex(s,t)
                vertices.extend(p00+n00+t00)
        self.vertices = numpy.array(vertices, dtype=numpy.float32)

        numS = len(self.sRange)
        numT = len(self.tRange)
        indices = []
        for s in range(numS-1):
            for t in range(numT-1):
                i00 = s*numT + t
                i01 = s*numT + (t+1)
                i10 = (s+1)*numT + t
                i11 = (s+1)*numT + (t+1)
                indices.extend([i00,i01,i10, i01,i11,i10])
        self.indices = numpy.array(indices, dtype=numpy.uint16)

radius = 1.0
def spherePoint(s,t):
    cosS = numpy.cos(s)
    sinS = numpy.sin(s)
    cosT = numpy.cos(t)
    sinT = numpy.sin(t)
    return [radius*cosS*sinT,
            radius*sinS*sinT,
            radius*cosT,
            1.0]

def sphereNorm(s,t):
    x,y,z,w = spherePoint(s,t)
    mag = numpy.sqrt(x*x+y*y+z*z)
    return [x/mag, y/mag, z/mag, 0.0]

inc = numpy.pi*0.125
sRange = numpy.arange(0.0, 2*numpy.pi+inc, inc)
tRange = numpy.arange(0.0, numpy.pi+inc, inc)

def main():
    pygame.init()


    theSurface = ParametricSurface(point = spherePoint, norm = sphereNorm,
                                   sRange = sRange, tRange = tRange)

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
