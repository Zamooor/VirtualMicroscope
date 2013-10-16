import os

from OpenGL.GL import *

import pygame
from pygame.locals import *

import numpy 
from ctypes import c_void_p

#from shader import getShader
#from transforms import *
from parametricsurface import ParametricSurface
#from pntbuffer import PNTBuffer
#from uniforms import Uniforms
#from drawable import Mesh
from frame import Frame



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

def init():
    # Normal OpenGL initializations
    glClearColor(0.5,0.5,0.5,1.0)
    glEnable(GL_DEPTH_TEST)

def display():
    # OpenGL necessities first:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,800), OPENGL|DOUBLEBUF)
    frame = Frame()
    rotX, rotY, rotZ = 0.0,0.0,0.0
    rotXmatrix = numpy.eye(4, dtype=numpy.float32)
    rotYmatrix = numpy.eye(4, dtype=numpy.float32)
    rotZmatrix = numpy.eye(4, dtype=numpy.float32)
    clock = pygame.time.Clock()

    init()
    near = 1.0 
    far = 50.0 
    depth = 2.0

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYUP and event.key == K_ESCAPE:
                return
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    n = theUniforms.items['showLines']
                    theUniforms.items['showLines'] = (n+1)%2
                if event.key == K_l:
                    if near < 2.0:
                        near = 19.0
                        far = 21.0
                    else:
                        near = 1.0
                        far = 50.0

        # Keyboard polling:
        pressed = pygame.key.get_pressed()

        # observer movement:
        amt = 0.2
        if pressed[K_DOWN]:
            frame.elevate(amt)
        if pressed[K_UP]:
            frame.elevate(-amt)
        if pressed[K_LEFT]:
            frame.strafe(-amt)
        if pressed[K_RIGHT]:
            frame.strafe(amt)
        if pressed[K_PAGEUP]:
            frame.move(amt)
        if pressed[K_PAGEDOWN]:
            frame.move(-amt)
        
        # world rotation:
        if pressed[K_w]:
            rotX -= 0.02
        if pressed[K_s]:
            rotX += 0.02
        if pressed[K_a]:
            rotY += 0.02
        if pressed[K_d]:
            rotY -= 0.02
        if pressed[K_q]:
            rotZ -= 0.02
        if pressed[K_e]:
            rotZ += 0.02

        #setRotationX(rotXmatrix, rotX)
        #setRotationY(rotYmatrix, rotY)
        #setRotationZ(rotZmatrix, rotZ)

        mat = numpy.dot(rotYmatrix, rotZmatrix)
        mat = numpy.dot(rotXmatrix, mat)

        # near/far manipulation:
        if pressed[K_j]:
            near += amt
        if pressed[K_k]:
            near -= amt
        if pressed[K_u]:
            far += amt
        if pressed[K_i]:
            far -= amt

        if pressed[K_o]:
            near += amt
            far += amt
        if pressed[K_p]:
            near -= amt
            far -= amt

                            
        display()
        pygame.display.flip()

    

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
