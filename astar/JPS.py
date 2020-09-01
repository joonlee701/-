'''
Created on 2016. 3. 29.

@author: 389
'''
from time import time


class Node:
    def __init__(self, coordi, state, g_val = 0, parent = None):
        self.coordi = coordi
        self.state = state
        self.g_val = g_val
        self.h_val = 0
        self.f_val = 0
        self.parent = parent
        
    def getDist(self, goal):
        dist = 0
        x_differ = abs(goal[1] - self.coordi[1])
        y_differ = abs(goal[0] - self.coordi[0])
        
        dist += min([x_differ, y_differ]) * 14
        dist += abs(x_differ - y_differ) * 10
        
        return dist
        
    
class searchNode:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.map = []
        self.openList = []
        self.success = False
        
        
    def readFile(self, filename):
        j = 0
        state = []
        row = []
        
        file = open(filename)
        lines = file.readlines()
        
        for line in lines:
            state.append(line.split(','))
            for i in range(len(state[j])):
                if i < 199:
                    row.append(Node([j, i], state[j][i]))
                else:
                    row.append(Node([j, i], state[j][i].split('\n')[0]))
            self.map.append(row)        
            j += 1
            row = []
    
    
    def doMove(self):

        while not self.success:
            coordi = self.openList.pop(0)
            print coordi
            node = self.map[coordi[0]][coordi[1]]
            self.look_R(node, node.g_val)
            self.look_D(node, node.g_val)
            self.look_L(node, node.g_val)
            self.look_U(node, node.g_val)
            self.look_RD(node)
            self.look_RU(node)
            self.look_LD(node)
            self.look_LU(node)
            
        self.printResult()
            
        
    def look_RD(self, node):
        x_coordi = node.coordi[1] + 1 
        y_coordi = node.coordi[0] + 1
        
        while x_coordi in range(200) and y_coordi in range(200) and self.map[y_coordi][x_coordi].state == '0':
            cur_node = self.map[y_coordi][x_coordi]
            val = cur_node.getDist(node.coordi) + node.g_val
            if self.look_R(cur_node, val) or self.look_D(cur_node, val):      
                if self.map[y_coordi][x_coordi].state != '2' or cur_node.parent == None:
                        cur_node.parent = node
                        cur_node.g_val = cur_node.getDist(node.coordi) + node.g_val
                cur_node.h_val = cur_node.getDist(self.goal)
                cur_node.f_val = cur_node.g_val + cur_node.h_val
                self.insert([y_coordi, x_coordi])
                
                self.map[y_coordi][x_coordi].state = '2'
                
            elif x_coordi != 199 and y_coordi != 199:    
                if self.map[y_coordi + 1][x_coordi + 1].state == '1':
                    if self.map[y_coordi][x_coordi].state != '2':
                        cur_node.parent = node
                        cur_node.g_val = cur_node.getDist(node.coordi) + node.g_val
                        cur_node.h_val = cur_node.getDist(self.goal)
                        cur_node.f_val = cur_node.h_val + cur_node.g_val
                        self.insert([y_coordi, x_coordi])
                    self.map[y_coordi][x_coordi].state = '2'
                    break
                
            self.map[y_coordi][x_coordi].state = '2'
            x_coordi += 1
            y_coordi += 1
                        
            
            
    def look_RU(self, node):
        x_coordi = node.coordi[1] + 1
        y_coordi = node.coordi[0] - 1
        
        while x_coordi in range(200) and y_coordi in range(200) and self.map[y_coordi][x_coordi].state == '0':
            cur_node = self.map[y_coordi][x_coordi]
            val = cur_node.getDist(node.coordi) + node.g_val
            if self.look_R(cur_node, val) or self.look_U(cur_node, val):
                if self.map[y_coordi][x_coordi].state != '2' or cur_node.parent == None:
                        cur_node.parent = node
                        cur_node.g_val = cur_node.getDist(node.coordi) + node.g_val
                cur_node.h_val = cur_node.getDist(self.goal)
                cur_node.f_val = cur_node.h_val + cur_node.g_val
                self.insert([y_coordi, x_coordi])
                self.map[y_coordi][x_coordi].state = '2'
        
            elif y_coordi != 0 and x_coordi != 199:
                if self.map[y_coordi - 1][x_coordi + 1].state == '1':
                    cur_node.g_val = cur_node.getDist(node.coordi) + node.g_val
                    cur_node.h_val = cur_node.getDist(self.goal)
                    cur_node.f_val = cur_node.h_val + cur_node.g_val
                    if self.map[y_coordi][x_coordi].state != '2':
                        cur_node.parent = node
                        self.insert([y_coordi, x_coordi])
                    self.map[y_coordi][x_coordi].state = '2'
                    break
            
            self.map[y_coordi][x_coordi].state = '2'
            x_coordi += 1
            y_coordi -= 1
            
            
    def look_LD(self, node):
        x_coordi = node.coordi[1] - 1
        y_coordi = node.coordi[0] + 1
        
        while x_coordi in range(200) and y_coordi in range(200) and self.map[y_coordi][x_coordi].state ==  '0':
            cur_node = self.map[y_coordi][x_coordi]
            val = cur_node.getDist(node.coordi) + node.g_val
            if self.look_L(cur_node, val) or self.look_D(cur_node, val):
                if self.map[y_coordi][x_coordi].state != '2' or cur_node.parent == None:
                        cur_node.parent = node
                        cur_node.g_val = cur_node.getDist(node.coordi) + node.g_val
                cur_node.h_val = cur_node.getDist(self.goal)
                cur_node.f_val = cur_node.h_val + cur_node.g_val
                self.insert([y_coordi, x_coordi])
                self.map[y_coordi][x_coordi].state = '2'
       
            elif y_coordi != 199 and x_coordi != 0:
                if self.map[y_coordi + 1][x_coordi - 1].state == '1':
                    if self.map[y_coordi][x_coordi].state != '2':
                        cur_node.parent = node
                        cur_node.g_val = cur_node.getDist(node.coordi) + node.g_val
                        cur_node.h_val = cur_node.getDist(self.goal)
                        cur_node.f_val = cur_node.h_val + cur_node.g_val
                        self.insert([y_coordi, x_coordi])
                    self.map[y_coordi][x_coordi].state = '2'
                    break
                
            self.map[y_coordi][x_coordi].state = '2'
            x_coordi -= 1
            y_coordi += 1 
    
    
    def look_LU(self, node):
        x_coordi = node.coordi[1] - 1
        y_coordi = node.coordi[0] - 1
        
        while x_coordi in range(200) and self.map[y_coordi][x_coordi].state == '0':
            cur_node = self.map[y_coordi][x_coordi]
            val = cur_node.getDist(node.coordi) + node.g_val
            if self.look_L(cur_node, val) or self.look_U(cur_node, val):
                if self.map[y_coordi][x_coordi].state != '2' or cur_node.parent == None:
                        cur_node.parent = node
                        cur_node.g_val = cur_node.getDist(node.coordi) + node.g_val
                cur_node.h_val = cur_node.getDist(self.goal)
                cur_node.f_val = cur_node.h_val + cur_node.g_val
                self.insert([y_coordi, x_coordi])
                self.map[y_coordi][x_coordi].state = '2'
      
            elif y_coordi != 0 and x_coordi != 0:
                if self.map[y_coordi - 1][x_coordi - 1].state == '1':
                    if self.map[y_coordi][x_coordi].state != '2':
                        cur_node.parent = node
                        cur_node.g_val = cur_node.getDist(node.coordi) + node.g_val
                        cur_node.h_val = cur_node.getDist(self.goal)
                        cur_node.f_val = cur_node.h_val + cur_node.g_val
                        self.insert([y_coordi, x_coordi])
                    self.map[y_coordi][x_coordi].state = '2'
                    break
                
            self.map[y_coordi][x_coordi].state = '2'
            x_coordi -= 1
            y_coordi -= 1
             
        
    def look_R(self, node, val):
        x_coordi = node.coordi[1] + 1
        y_coordi = node.coordi[0]
        
        while x_coordi in range(200) and self.map[y_coordi][x_coordi].state == '0':
            cur_node = self.map[y_coordi][x_coordi]
            if y_coordi != 0 and x_coordi != 199:
                if self.map[y_coordi - 1][x_coordi].state == '1' and self.map[y_coordi - 1][x_coordi + 1].state == '0':
                    cur_node.parent = node
                    cur_node.g_val = cur_node.getDist(node.coordi) + val
                    cur_node.h_val = cur_node.getDist(self.goal)
                    cur_node.f_val = cur_node.h_val + cur_node.g_val   
                    self.insert([y_coordi, x_coordi])
                    self.map[y_coordi][x_coordi].state = '2'
                    return True
            if y_coordi != 199 and x_coordi != 199:
                if self.map[y_coordi + 1][x_coordi].state == '1' and self.map[y_coordi + 1][x_coordi + 1].state == '0':
                    cur_node.parent = node
                    cur_node.g_val = cur_node.getDist(node.coordi) + val
                    cur_node.h_val = cur_node.getDist(self.goal)
                    cur_node.f_val = cur_node.h_val + cur_node.g_val   
                    self.insert([y_coordi, x_coordi])
                    self.map[y_coordi][x_coordi].state = '2'
                    return True
                
            if [y_coordi, x_coordi] == self.goal:
                cur_node.parent = node
                cur_node.g_val = cur_node.getDist(node.coordi) + val
                cur_node.h_val = cur_node.getDist(self.goal)
                cur_node.f_val = cur_node.h_val + cur_node.g_val   
                self.insert([y_coordi, x_coordi])
                self.map[y_coordi][x_coordi].state = '2'
                self.success = True    
                return True
            self.map[y_coordi][x_coordi].state = '2'
            x_coordi += 1
            
        return False
            
    
    def look_L(self, node, val):
        x_coordi = node.coordi[1] - 1
        y_coordi = node.coordi[0]
        
        while x_coordi in range(200) and self.map[y_coordi][x_coordi].state == '0':
            cur_node = self.map[y_coordi][x_coordi]
            if y_coordi != 0 and x_coordi != 0:
                if self.map[y_coordi - 1][x_coordi].state == '1' and self.map[y_coordi - 1][x_coordi - 1].state == '0':
                    cur_node.parent = node
                    cur_node.g_val = cur_node.getDist(node.coordi) + val
                    cur_node.h_val = cur_node.getDist(self.goal)
                    cur_node.f_val = cur_node.h_val + cur_node.g_val      
                    self.insert([y_coordi, x_coordi])
                    self.map[y_coordi][x_coordi].state = '2'
                    return True
                
            if  y_coordi != 199 and x_coordi != 0:
                if self.map[y_coordi + 1][x_coordi].state == '1' and self.map[y_coordi + 1][x_coordi - 1].state == '0':
                    cur_node.parent = node
                    cur_node.g_val = cur_node.getDist(node.coordi) + val
                    cur_node.h_val = cur_node.getDist(self.goal)
                    cur_node.f_val = cur_node.h_val + cur_node.g_val   
                    self.insert([y_coordi, x_coordi])
                    self.map[y_coordi][x_coordi].state = '2'
                    return True
            
            if [y_coordi, x_coordi] == self.goal:
                cur_node.parent = node
                cur_node.g_val = cur_node.getDist(node.coordi) + val
                cur_node.h_val = cur_node.getDist(self.goal)
                cur_node.f_val = cur_node.h_val + cur_node.g_val   
                self.insert([y_coordi, x_coordi])
                self.map[y_coordi][x_coordi].state = '2'
                self.success = True    
                return True
                
            self.map[y_coordi][x_coordi].state = '2'    
            x_coordi -= 1
            
        return False
            
                
    def look_U(self, node, val):  
        x_coordi = node.coordi[1]
        y_coordi = node.coordi[0] - 1
        
        while y_coordi in range(200) and self.map[y_coordi][x_coordi].state == '0':
            cur_node = self.map[y_coordi][x_coordi]
            if x_coordi != 199 and y_coordi != 0:
                if self.map[y_coordi][x_coordi + 1].state == '1' and self.map[y_coordi - 1][x_coordi + 1].state == '0':
                    cur_node.parent = node
                    cur_node.g_val = cur_node.getDist(node.coordi) + val
                    cur_node.h_val = cur_node.getDist(self.goal)
                    cur_node.f_val = cur_node.h_val + cur_node.g_val      
                    self.insert([y_coordi, x_coordi])
                    self.map[y_coordi][x_coordi].state = '2'
                    return True
                
            if x_coordi != 0 and y_coordi != 0:    
                if self.map[y_coordi][x_coordi - 1].state == '1' and self.map[y_coordi - 1][x_coordi - 1].state == '0':
                    cur_node.parent = node
                    cur_node.g_val = cur_node.getDist(node.coordi) + val
                    cur_node.h_val = cur_node.getDist(self.goal)
                    cur_node.f_val = cur_node.h_val + cur_node.g_val   
                    self.insert([y_coordi, x_coordi])
                    self.map[y_coordi][x_coordi].state = '2'
                    return True
            if [y_coordi, x_coordi] == self.goal:
                cur_node.parent = node
                cur_node.g_val = cur_node.getDist(node.coordi) + val
                cur_node.h_val = cur_node.getDist(self.goal)
                cur_node.f_val = cur_node.h_val + cur_node.g_val   
                self.insert([y_coordi, x_coordi])
                self.map[y_coordi][x_coordi].state = '2'
                self.success = True    
                return True
            
            self.map[y_coordi][x_coordi].state = '2'
            y_coordi -= 1
        
        return False
        
    
    def look_D(self, node, val):
        x_coordi = node.coordi[1]
        y_coordi = node.coordi[0] + 1
        
        while y_coordi in range(200) and self.map[y_coordi][x_coordi].state == '0':
            cur_node = self.map[y_coordi][x_coordi]
            if x_coordi != 199 and y_coordi != 199:
                if self.map[y_coordi][x_coordi + 1].state == '1' and self.map[y_coordi + 1][x_coordi + 1].state == '0':
                    cur_node.parent = node
                    cur_node.g_val = cur_node.getDist(node.coordi) + val
                    cur_node.h_val = cur_node.getDist(self.goal)
                    cur_node.f_val = cur_node.h_val + cur_node.g_val   
                    self.insert([y_coordi, x_coordi])
                    self.map[y_coordi][x_coordi].state = '2'
                    return True
            if x_coordi != 0 and y_coordi != 199:        
                if self.map[y_coordi][x_coordi - 1].state == '1' and self.map[y_coordi + 1][x_coordi - 1].state == '0':
                    cur_node.parent = node
                    cur_node.g_val = cur_node.getDist(node.coordi) + val
                    cur_node.h_val = cur_node.getDist(self.goal)
                    cur_node.f_val = cur_node.h_val + cur_node.g_val      
                    self.insert([y_coordi, x_coordi])
                    self.map[y_coordi][x_coordi].state = '2'
                    return True
                
            if [y_coordi, x_coordi] == self.goal:
                cur_node.parent = node
                cur_node.g_val = cur_node.getDist(node.coordi) + val
                cur_node.h_val = cur_node.getDist(self.goal)
                cur_node.f_val = cur_node.h_val + cur_node.g_val   
                self.insert([y_coordi, x_coordi])
                self.map[y_coordi][x_coordi].state = '2'
                self.success = True    
                return True
           
            self.map[y_coordi][x_coordi].state = '2'    
            y_coordi += 1
    
        return False   
        
            
    def makeRoot(self):
        coordi = self.start
        root = self.map[coordi[0]][coordi[1]]
        root.h_val = root.getDist(self.goal)
        root.f_val = root.h_val
        self.insert(self.start)
        
        
    def insert(self, coordi):
        if len(self.openList) == 0:
            self.openList.append(coordi)
        else:
            self.openList.append(coordi)
            m = len(self.openList) - 1 
            while m != 0:
                if self.map[self.openList[m][0]][self.openList[m][1]].f_val <= self.map[self.openList[int(m/2)][0]][self.openList[int(m/2)][1]].f_val:
                    temp = self.openList[int(m/2)]
                    self.openList[int(m/2)] = self.openList[m]
                    self.openList[m] = temp
                    m = int(m/2)
                else:
                    break
                
                
    def printResult(self):
        node = self.map[self.goal[0]][self.goal[1]]
        f = open("JPS.txt", 'w')
        
        while node != None:
            node.state = '9'
            parent = node.parent
            print node.g_val
            if parent == None:
                break
            
            x_differ = parent.coordi[1] - node.coordi[1]
            y_differ = parent.coordi[0] - node.coordi[0]
            
            if x_differ == 0:
                if y_differ == 0:
                    continue
                diff = y_differ / abs(y_differ)
                for i in range(abs(y_differ)):
                    self.map[node.coordi[0] + diff*i][node.coordi[1]].state ='9'
            
            elif y_differ == 0:
                diff = x_differ / abs(x_differ)
                for i in range(abs(x_differ)):
                    self.map[node.coordi[0]][node.coordi[1] + diff*i].state = '9'
            
            else:
                x_diff = x_differ / abs(x_differ)
                y_diff = y_differ / abs(y_differ)
                for i in range(abs(x_differ)):
                    self.map[node.coordi[0] + y_diff*i][node.coordi[1] + x_diff*i].state = '9'
            
            node = parent
            
            
        for i in range(200):
            for j in range(200):
                f.write(self.map[i][j].state)
                if j == 199:
                    f.write('\n')
        
if __name__ == "__main__":
    start = [0, 0]
    goal = [199, 199]
    
    t = time()
    
    a = searchNode(start, goal)
    a.readFile("Map.txt")
    a.makeRoot()
    a.doMove()
    
    print str(time() - t) + " secs"
    
            