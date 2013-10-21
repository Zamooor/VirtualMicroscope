import numpy
from ctypes import c_void_p

from OpenGL.GL import *
from transforms import *

class Uniforms():
    """Takes a shader and a list of uniforms, types and items
       and loads them into shader memory on Start."""
    def __init__(self, shader, unifs):
        self.shader = shader
        self.unifs = unifs
        self.locations = {}
        self.kinds = {}
        self.items = {}
        for unif in unifs:
            name, kind, item = unif
            self.items[name] = item
            self.kinds[name] = kind
            self.locations[name] = glGetUniformLocation(shader, name)

    def Update(self, name, item):
        self.items[name] = item
        
    def Start(self):
        glUseProgram(self.shader)
        for name in self.items:
            loc = self.locations[name]
            kind = self.kinds[name]
            item = self.items[name]

            if kind == 'vec4':
                glUniform4fv(loc, 1, item)
            elif kind == 'mat4':
                glUniformMatrix4fv(loc, 1, True, item)
            elif kind == 'int':
                glUniform1i(loc, item)
            elif kind == 'float':
                glUniform1f(loc, item)
                
    def Stop(self):
        glUseProgram(0)
