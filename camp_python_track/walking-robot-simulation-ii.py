class Robot:

    def __init__(self, width: int, height: int):
        self.ps = {0:"East",1:"North",2:"West",3:"South"}
        self.face = 0
        self.pos = [0,0]
        self.width = width
        self.height = height
        
    def step(self, num: int) -> None:
        """
        here whene rc==0 and num>0 this means that the robot will come around and be in the previous positions it was.
        but the catch is if that it may be facing other direction depending on what rout it took if the robot was on the corners the facing will change
        not finished it also depend on ehich direction the robot is facing right now to
        east[0,0] the botton left corner ===> south[0,0]
        norht[x,y] the top right corner  ===> 
        """
        rc = num%(2*self.width+2*self.height-4)
        if rc==0 and num>0:
            # print("face before ",self.face,self.ps[self.face])
            if self.pos==[0,0]:
                if self.face ==0:
                    self.face = 3
            elif  self.pos==[0,self.height]:
                if self.face ==3:
                    self.face = 2
            elif self.pos==[self.width,0]:
                if self.face ==1:
                    self.face = 0
            elif self.pos==[self.width,self.height]:
                if self.face ==2:
                    self.face = 1
            # print("face after ",self.face,self.ps[self.face])
        for i in range(rc):
            # print(i,self.pos,self.ps[self.face])
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
                # print(self.pos)
    def getPos(self) -> list[int]:
        return self.pos
        

    def getDir(self) -> str:
        return self.ps[self.face]