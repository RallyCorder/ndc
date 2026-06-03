import pyxel

SCRNH=256
SCRNW=512

class App:

    def __init__(self):
        pyxel.init(SCRNW,SCRNH,'BudgetVSMachine')
        pyxel.load('assets.pyxres')
        pyxel.mouse(True)
        self.en=Enemy(1,8)
        self.sentry=Turret(1,-16,-16)
        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        self.en.update()
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.sentry.posx=pyxel.mouse_x-16
            self.sentry.posy=pyxel.mouse_y-16
        
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
        if self.en.lose==True:
            pyxel.text(0,0,'LOST LOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOL',pyxel.frame_count % 16)
        self.sentry.draw()

class Enemy:

    def __init__(self,health,speed):
        self.health=health
        self.speed=speed
        self.lose=False
        self.posx=0
        self.posy=96
        self.step0=True
        self.step1=True
        self.step2=True
        self.step3=False
        self.step4=True
        self.step5=False
        self.step6=False
        self.step7=False
        self.step8=False
        self.step9=False
        self.step10=False
        self.step11=False

    def update(self):
        if pyxel.frame_count % 1 == 0:
            if not self.posx==192 and self.posy==96 and self.step0==True:
                self.posx+=self.speed
            if not self.posy==32 and self.posx==192 and self.step1==True:
                self.step0=False
                self.posy-=self.speed
            if not self.posx==128 and self.posy==32 and self.step2==True:
                self.step1=False
                self.step3=True
                self.posx-=self.speed
            if not self.posy==192 and self.posx==128 and self.step3==True:
                self.step2=False
                self.posy+=self.speed
            if not self.posx==64 and self.posy==192 and self.step4==True:
                self.step3=False
                self.step6=True
                self.step5=True
                self.posx-=self.speed
            if not self.posy==128 and self.posx==64 and self.step5==True:
                self.step4=False
                self.posy-=self.speed
            if not self.posx==256 and self.posy==128 and self.step6==True:
                self.step5=False
                self.step7=True
                self.posx+=self.speed
            if not self.posy==64 and self.posx==256 and self.step7==True:
                self.step6=False
                self.step8=True
                self.posy-=self.speed
            if not self.posx==320 and self.posy==64 and self.step8==True:
                self.step7=False
                self.step9=True
                self.posx+=self.speed
            if not self.posy==176 and self.posx==320 and self.step9==True:
                self.step8=False
                self.step10=True
                self.posy+=self.speed
            if not self.posx==192 and self.posy==176 and self.step10==True:
                self.step9=False
                self.step11=True
                self.posx-=self.speed
            if not self.posy==SCRNH and self.posx==192 and self.step11==True:
                self.step10=False
                self.posy+=self.speed
            if self.posy==SCRNH:
                self.lose=True                


    def draw(self):
        pyxel.blt(self.posx,self.posy,1,0,0,16,16,pyxel.COLOR_BLACK)

class Turret:

    def __init__(self,lvl,posx,posy):
        self.lvl=lvl
        self.posx=posx
        self.posy=posy

    def draw(self):
        pyxel.blt(self.posx,self.posy,2,0,0,-16,16,pyxel.COLOR_WHITE,0,2)

App()