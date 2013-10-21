
class Drawable():
    def Draw(self):
        pass
    def Start(self):
        pass
    def Stop(self):
        pass
    def Update(self, name, item):
        pass

class Mesh(Drawable):
    def __init__(self, uniforms, buff):
        self.uniforms = uniforms
        self.buffer = buff

    def Start(self):
        self.uniforms.Start()
        self.buffer.Start()

    def Stop(self):
        self.buffer.Stop()
        self.uniforms.Stop()

    def Draw(self):
        self.uniforms.Start()
        self.buffer.Start()
        self.buffer.Stop()
        self.uniforms.Stop()

    def Update(self, name, item):
        self.uniforms.Update(name, item)

class CompositeMesh(Drawable):
    def __init__(self, meshes):
        self.meshes = meshes

    def Start(self):
        for mesh in self.meshes:
            mesh.Start()
            
    def Stop(self):
        for mesh in self.meshes:
            mesh.Stop()
            
    def Draw(self):
        for mesh in self.meshes:
            mesh.Draw()

    def Update(self, name, item):
        for mesh in self.meshes:
            mesh.Update(name, item)
            
