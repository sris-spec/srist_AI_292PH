import random
from time import sleep

class player:

    def _init_(self):
        self.step = 0

    def closest_empty(self,B,N,cur_x,cur_y):
        dis = 2*N+1
        best = {"x":cur_x,"y":cur_y}
        for i in range(N):
            for j in range(N):
                if B[i][j] == 0:
                    dx = min ( abs(cur_x - i) , N - abs(cur_x - i) )
                    dy = min ( abs(cur_y - j) , N - abs(cur_y - j) )
                    cur_dis = dx+dy
                    if cur_dis < dis:
                        dis = cur_dis
                        best["x"] = i 
                        best["y"] = j 

        if best["y"] > cur_y:
            if best["y"]-cur_y < N/2:
                return (0,1)
            else:
                return (0,-1)


        if best["y"] < cur_y:
            if cur_y-best["y"] < N/2:
                return (0,-1)
            else:
                return (0,1)


        if best["x"] > cur_x:
            if best["x"]-cur_x < N/2:
                return (1,0)
            else:
                return (-1,0)

        if best["x"] < cur_x:
            if cur_x-best["x"] < N/2:
                return (-1,0)
            else:
                return (1,0)
        return (0,0)

    def checkNbr(self,B,N,cur_x,cur_y):
        left = B[(cur_x-1)%(N)][cur_y%(N)] == 0
        right = B[(cur_x+1)%(N)][cur_y%(N)] == 0
        up = B[cur_x%(N)][(cur_y-1)%(N)] == 0
        down = B[cur_x%(N)][(cur_y+1)%(N)] == 0

        if left == True:
            left = (-1,0)
        if right == True:
            right = (1,0)
        if up == True:
            up = (0,-1)
        if down == True:
            down = (0,1)

        return left, right, up, down

    def move(self,B,N,cur_x,cur_y):
        self.step+=1

        nbrs = self.checkNbr(B,N,cur_x,cur_y)
        rdm = random.choice(nbrs)

        if rdm != False:
            return rdm

        return self.closest_empty(B,N,cur_x,cur_y)




        


        # if B[cur_x][(cur_y+1)%N]==0:
        #     return (0,1)

        # if B[cur_x][(cur_y+N-1)%N]==0:
        #     return (0,-1)
        
        # if B[(cur_x+1)%N][cur_y]==0:
        #     return (1,0)

        # if B[(cur_x+N-1)%N][cur_y]==0:
        #     return (-1,0)