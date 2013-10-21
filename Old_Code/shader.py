import os
from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram
    
def loadFile(filename):
    with open(os.path.join(os.getcwd(), filename)) as fp:
        return fp.read()

def compileShaderProgram(vertexShader, fragmentShader):
    myProgram = compileProgram(
        compileShader(vertexShader, GL_VERTEX_SHADER),
        compileShader(fragmentShader, GL_FRAGMENT_SHADER)
    )
    return myProgram

def getShader(vertexShader, fragmentShader):
    vert = loadFile(vertexShader)
    frag = loadFile(fragmentShader)
    return compileShaderProgram(vert, frag)
