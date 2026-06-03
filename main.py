import pyxel

SCRNH=256
SCRNW=512

class App:

    def __init__(self):
        pyxel.init(SCRNW,SCRNH,'NDC')
        pyxel.load('assets.pyxres')
        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        pyxel.cls(pyxel.COLOR_GRAY)
        

App()