import pyxel

SCRNH=256
SCRNW=512

class App:

    def __init__(self):
        pyxel.init(SCRNW,SCRNH,'NDC')
        pyxel.load('assets.pyxres')
        self.en=Enemy(1,2)
        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        self.en.update()
        
    def mapinit(self):
        x=0
        y=0
        for _ in range(SCRNW//8):
            for _ in range(SCRNW//8):
                pyxel.blt(x,y,0,0,0,16,16)
                x+=8
            x=0
            y+=8
        x=0
        y=96
        for _ in range(24):
            pyxel.blt(x,y,0,16,0,16,16)
            x+=8
        for _ in range(8):
            pyxel.blt(x,y,0,16,0,16,16)
            y-=8
        for _ in range(8):
            pyxel.blt(x,y,0,16,0,16,16)
            x-=8
        for _ in range(20):
            pyxel.blt(x,y,0,16,0,16,16)
            y+=8
        for _ in range(8):
            pyxel.blt(x,y,0,16,0,16,16)
            x-=8
        for _ in range(8):
            pyxel.blt(x,y,0,16,0,16,16)
            y-=8
        for _ in range(24):
            pyxel.blt(x,y,0,16,0,16,16)
            x+=8
        for _ in range(8):
            pyxel.blt(x,y,0,16,0,16,16)
            y-=8
        for _ in range(8):
            pyxel.blt(x,y,0,16,0,16,16)
            x+=8
        for _ in range(14):
            pyxel.blt(x,y,0,16,0,16,16)
            y+=8
        for _ in range(16):
            pyxel.blt(x,y,0,16,0,16,16)
            x-=8
        for _ in range(10):
            pyxel.blt(x,y,0,16,0,16,16)
            y+=8

    def draw(self):
        self.mapinit()
        self.en.draw()

class Enemy:

    def __init__(self,health,speed):
        self.health=health
        self.speed=speed
        self.posx=0
        self.posy=96

    def update(self):
        if pyxel.frame_count % 1 == 0:
            self.posx+=self.speed

    def draw(self):
        pyxel.blt(self.posx,self.posy,1,0,0,16,16)


App()