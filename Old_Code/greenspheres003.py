import os

# Real time microscope depth of field.
# use arrow keys and pgup/pgdown

from OpenGL.GL import *

import pygame
from pygame.locals import *

import numpy 
from ctypes import c_void_p

from shader import getShader
from transforms import *
from parametricsurface import ParametricSurface
from pntbuffer import PNTBuffer
from uniforms import Uniforms
from drawable import Mesh
from frame import Frame

shaderfiles = ['shader003.vert', 'shader003.frag']

# stuff for generating a sphere:
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
    global theWorld
    # Normal OpenGL initializations
    glClearColor(0.5,0.5,0.5,1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    #glBlendFunc(GL_ONE, GL_ONE)
    glEnable(GL_CULL_FACE)

    #glEnable(GL_ALPHA_TEST)
    #glAlphaFunc(GL_GREATER, 0.001)
    
    # Create the buffer and uniform objects for our sphere surface
    theShader = getShader(shaderfiles[0], shaderfiles[1])
    theSurface = ParametricSurface(point = spherePoint, norm = sphereNorm,
                                   sRange = sRange, tRange = tRange)
    theBuffer = PNTBuffer(theShader,
                          theSurface.vertices,
                          theSurface.indices,
                          20)
    pMatrix = projectionMatrix(1.0, 100.0, 1.0, 1.0)
    pMatrix = orthographicMatrix(1.0, 100.0, 10.0, 10.0)
    # only used if no joystick:
    tMatrix = translationMatrix(0.0, 0.0, -20.0)
    rMatrix = numpy.eye(4, dtype=numpy.float32)
    theUniforms = Uniforms(theShader,
                           [('focalDistance', 'float',
                             20.0),
                            ('light', 'vec4',
                             numpy.array((10,10,10,1), dtype=numpy.float32)),
                            ('color', 'vec4',
                             numpy.array((0,.5,0), dtype=numpy.float32)),
                            ('modelMatrix', 'mat4',
                             numpy.eye(4, dtype=numpy.float32)),
                            ('translationMatrix', 'mat4',
                             tMatrix),
                            ('preRotationMatrix', 'mat4',
                             rMatrix),
                            ('postRotationMatrix', 'mat4',
                             numpy.eye(4, dtype=numpy.float32)),
                            ('projectionMatrix', 'mat4',
                             pMatrix),
                            ('showLines', 'int',
                             0)])
    theWorld = Mesh(theUniforms, theBuffer)

def display():
    global theWorld
    # OpenGL necessities first:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Draw our objects:
    theWorld.Draw()

factor = 0.1
def joy(joystick, axis):
    val = joystick.get_axis(axis)
    return round(factor*val, 1)
                           
def main():
    global theWorld
    pygame.init()
    screen = pygame.display.set_mode((800,800), OPENGL|DOUBLEBUF)
    
    frame = Frame()
    have_joystick = False
    if pygame.joystick.get_count() > 0:
        have_joystick = True
        autoRotation = False
        joystick = pygame.joystick.Joystick(0)
        joystick.init()       
        rot = 0
        fwd = 1
        stf = 2
        tlt = 3

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

            if have_joystick:
                if event.type == pygame.JOYBUTTONUP:
                    autoRotation = not(autoRotation)

        # Joystick polling:
        if have_joystick:
            factor = 1.0/30.0
            frame.move(-joy(joystick, fwd))
            frame.rotate(numpy.pi * -joy(joystick, rot))
            frame.strafe(joy(joystick, stf))
            frame.tilt(numpy.pi * joy(joystick, tlt))
            theWorld.Update('translationMatrix',
                             frame.translation)
            theWorld.Update('postRotationMatrix',
                             frame.rotation)
            if autoRotation:
                rotX += 0.005
                rotY += 0.005
                rotZ += 0.005

        # Keyboard polling:
        pressed = pygame.key.get_pressed()

        # observer movement:
        if pressed[K_DOWN]:
            frame.elevate(0.1)
        if pressed[K_UP]:
            frame.elevate(-0.1)
        if pressed[K_LEFT]:
            frame.strafe(-0.1)
        if pressed[K_RIGHT]:
            frame.strafe(0.1)
        if pressed[K_PAGEUP]:
            frame.move(0.1)
        if pressed[K_PAGEDOWN]:
            frame.move(-0.1)
            
        theWorld.Update('translationMatrix', frame.translation)
        theWorld.Update('postRotationMatrix', frame.rotation)

        # world rotation:
        if pressed[K_q]:
            rotZ -= 0.02
        if pressed[K_e]:
            rotZ += 0.02
            
        setRotationZ(rotZmatrix, rotZ)
        mat = numpy.dot(rotYmatrix, rotZmatrix)
        mat = numpy.dot(rotXmatrix, mat)
                            
        theWorld.Update('preRotationMatrix', mat)

        # near/far manipulation:
        amt = 0.1
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

        near = max(near, 0.001)
        #theWorld.Update('projectionMatrix',
         #                projectionMatrix(near, far, near, near))
                            
        display()
        pygame.display.flip()

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
        
