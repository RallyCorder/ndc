import pyxel

SCRNH=256
SCRNW=256

class App:

    def __init__(self):
        pyxel.init(SCRNW,SCRNH,'NDC')
        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        pyxel.cls(pyxel.COLOR_WHITE)

App()