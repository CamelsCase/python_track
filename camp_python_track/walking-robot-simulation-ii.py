class Robot:
    def __init__(self, width: int, height: int):
        self.ps = {0:"East",1:"North",2:"West",3:"South"}
        self.face = 0
        self.pos = [0,0]
        self.width = width
        self.height = height

    def step(self, num: int) -> None:
        rc = num%(2*self.width+2*self.height-4)
        if rc==0 and num>0:
            if (self.pos==[0,0] and self.face ==0) or (self.pos==[0,self.height] and  self.face ==3) or (self.pos==[self.width,0] and  self.face ==1) or (self.pos==[self.width,self.height] and  self.face ==2):
                    self.face = (self.face+3)%4

        for i in range(rc):
            found = False
            while not found:
                if self.face==0:
                    if self.pos[0]<self.width-1:
                        self.pos[0]+=1
                        found=True
                    else:
                        self.face = (self.face+1)%4
                if self.face==1:
                    if self.pos[1]<self.height-1:
                        self.pos[1]+=1
                        found=True
                    else:
                        self.face = (self.face+1)%4
                if self.face==2:
                    if self.pos[0]>0:
                        self.pos[0]-=1
                        found=True
                    else:
                        self.face = (self.face+1)%4
                if self.face==3:
                    if self.pos[1]>0:
                        self.pos[1]-=1
                        found=True
                    else:
                        self.face = (self.face+1)%4

    def getPos(self) -> list[int]:
        return self.pos

    def getDir(self) -> str:
        return self.ps[self.face]