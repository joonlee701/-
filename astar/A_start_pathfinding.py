from time import time

class Node:
    def __init__(self, coordi, state):
        self.coordi = coordi
        self.g_val = 0
        self.parent = None
        self.h_val = 0
        self.state = state
        self.f_val = 0
    
    def getHval(self, goal):
        if self.h_val != 0:
            return
        x_differ = abs(self.coordi[1] - goal[1])
        y_differ = abs(self.coordi[0] - goal[0])
        
        self.h_val += min([x_differ, y_differ]) * 14
        self.h_val += abs(x_differ - y_differ) * 10
        
        
    
class searchNode:
    def __init__(self, start, goal):
        self.map = []
        self.openList = []
        self.start = start
        self.goal = goal
        self.success = False
        
    def doMove(self):
        while not self.success:
            coordi = self.openList.pop(0)
            cur_node = self.map[coordi[0]][coordi[1]]
            
            if coordi[0] != 0 and self.checkState([coordi[0] - 1, coordi[1]], cur_node.g_val):
                x = coordi[1]
                y = coordi[0] - 1
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 10
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].h_val + self.map[y][x].g_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            
            if coordi[0] != 0 and coordi[1] != 199 and self.checkState([coordi[0] - 1, coordi[1] + 1], cur_node.g_val):
                x = coordi[1] + 1
                y = coordi[0] - 1
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 14
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].g_val + self.map[y][x].h_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            if coordi[1] != 199 and self.checkState([coordi[0], coordi[1] + 1], cur_node.g_val):
                x = coordi[1] + 1
                y = coordi[0]
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 10
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].g_val + self.map[y][x].h_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            if coordi[0] != 199 and coordi[1] != 199 and self.checkState([coordi[0] + 1, coordi[1] + 1], cur_node.g_val):
                x = coordi[1] + 1
                y = coordi[0] + 1
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 14
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].g_val + self.map[y][x].h_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            if coordi[0] != 199 and self.checkState([coordi[0] + 1, coordi[1]], cur_node.g_val):
                x = coordi[1]
                y = coordi[0] +1
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 10
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].h_val + self.map[y][x].g_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            if coordi[0] != 199 and coordi[1] != 0 and self.checkState([coordi[0] + 1, coordi[1] - 1], cur_node.g_val):
                x = coordi[1] - 1
                y = coordi[0] + 1
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 14
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].h_val + self.map[y][x].g_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            if coordi[1] != 0 and self.checkState([coordi[0], coordi[1] - 1], cur_node.g_val):
                x = coordi[1] - 1
                y = coordi[0]
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 10
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].h_val + self.map[y][x].g_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            if coordi[0] != 0 and coordi[1] != 0 and self.checkState([coordi[0] - 1, coordi[1] - 1], cur_node.g_val):
                x = coordi[1] - 1
                y - coordi[0] - 1
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 14
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].h_val + self.map[y][x].g_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
        self.printMap()
            
                
                
            
    def  checkState(self, coordi, value):
        if coordi[0] in range(200) and coordi[1] in range(200):
            if self.map[coordi[0]][coordi[1]].state == '1':
                return False
        
            elif self.map[coordi[0]][coordi[1]].state == '2':
                if value + 14 > self.map[coordi[0]][coordi[1]].g_val:
                    return False
                
        if coordi in self.openList:
            self.openList.remove(coordi)
        return True 
            
    
    
    def getMap(self, filename):
        j = 0
        state = []
        row = []
        
        f = open(filename)
        lines = f.readlines()
        for line in lines:
            state.append(line.split(','))
            for i in range(len(state[j])):
                if i < 199:
                    row.append(Node([j, i], state[j][i]))
                else:
                    a = state[j][i].split('\n')
                    row.append(Node([j, i], a[0]))
            self.map.append(row)
            row = []
            j += 1
                           
                
    def insert(self, coordi):
        if len(self.openList) == 0:
            self.openList.append(coordi)
        else:
            self.openList.append(coordi)
            m = len(self.openList) - 1
            while m != 0:
                if self.map[coordi[0]][coordi[1]].f_val <= self.map[self.openList[int(m/2)][0]][self.openList[int(m/2)][1]].f_val: 
                    temp = self.openList[int(m/2)]
                    self.openList[int(m/2)] = self.openList[m]
                    self.openList[m] = temp
                    m = int(m/2)
                else:
                    break
        
        
    def makeRoot(self):
        root = self.map[0][0]
        root.getHval(self.goal)
        root.f_val = root.h_val
        self.insert(root.coordi)
        self.map[0][0].state = '2'
        
    
    def search(self):
        self.makeRoot()
        self.doMove()
        
        
    def printMap(self):
        node = self.map[self.goal[0]][self.goal[1]]        
        while node != None:
            node.state = '9'
            node = node.parent
            
        row = ""
        f = open("result.txt", 'w')
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                row += str(self.map[i][j].state)
            f.write(row)
            f.write('\n')
            row = ""
        


if __name__ == "__main__":
    start = [0,0]
    goal = [199,199]
    
    t = time()
    astar = searchNode(start, goal)
    astar.getMap("Map.txt")
    astar.search()
    
    print str(time() - t) + " secs"