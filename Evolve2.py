# Assignment 2 evolve a species Vicente Montero III

from Tkinter import *

import random

class Evolve:
        

              
        """
        make random numbers according to size of world
        """                  
        def randy(self):
            x = random.randrange(0,self.randsize-10,10)
            return x
            
            
        """
        make strawbs and mushrooms
        """
        def ins_strawb(self,x,y,tag):
            self.x = x
            self.y = y
            self.canvas.create_oval(x,y,x+10,y+10, fill = "red", tags="strawb"+str(tag)+"")
            
        """
        mushrm insert
        """
        
        def ins_mushrm(self,x,y,tag):
            self.x = x
            self.y = y
            self.canvas.create_oval(x,y,x+10,y+10, fill = "brown", tags="mushrm"+str(tag)+"")            

        """
        creature insert
        """
        
        def ins_creature(self,x,y,tag):
            self.x = x
            self.y = y
            self.canvas.create_rectangle(x,y,x+10,y+10, fill = "yellow", tags="creature"+str(tag)+"")
        """
        monster insert
        """
        
        def ins_monster(self,x,y,tag):
            self.x = x
            self.y = y
            self.canvas.create_rectangle(x,y,x+10,y+10, fill = "black", tags="monster"+str(tag)+"")
            
            
        """
        Sensors------------------------------------------------------------------------------------------------------O
        """
        def strawb_present(self,xcoord,ycoord):
            #print "coords "+str(xcoord) + " " +str(ycoord)            
            i =0
            while i < len(self.strawb_array): 
                x = self.strawb_array[i][0]
                y = self.strawb_array[i][1]
                #print "strawb" + str(i) + " "+str(x) + " " +str(y)
                

                if x == xcoord: 
                    if y == ycoord:
                        if self.strawb[i] != 0:
                        #print 'hi'
                        #print str(self.strawb[i])
                            return 1
                i += 1
            
            return 0
        
        def mushrm_present(self,xcoord,ycoord):
            
            
            i =0
            while i < len(self.mushrm_array): 
                x = self.mushrm_array[i][0]
                y = self.mushrm_array[i][1]
                #print "strawb" + str(i) + " "+str(x) + " " +str(y)
                

                if x == xcoord: 
                    if y == ycoord:
                        if self.mushrm[i] != 0:
                            
                        #print str(self.strawb[i])
                            return 1
                i += 1
            
            return 0
                            
        def nearest_strawb(self,xcoord,ycoord):
#n = [xcoord-30,ycoord-30,xcoord+40,ycoord+40]
            nx = xcoord - 40
            ny = ycoord - 40
            nu = xcoord +50
            nv = ycoord +50
           # print str(nx) + " " +str(ny)+ " " + str(nu) + " " + str(nv)
           #print str(xcoord) + ' ' + str(ycoord)
            
            c =0
            d =0 
            
            thing = []
            nearest4 ='null'
            i=0
            while i < len(self.strawb_array):#find out nearest
                
                j = 0
                while j < len(self.strawb_array):
                    if self.strawb[j] != 0:
                        thing.append([self.strawb_array[j][0],self.strawb_array[j][1]])                              
                    j+=1
                       
                #x = u
                #y = v
                a = 0 #the difference in the x axis
                b = 0
                
                for t in thing:
                    x = t[0]
                    y = t[1]
                    #print str(x) + " " + str(y)
                    if nu >= x:
                        if y <= nv:
                            if nx <= x:
                                if y >= ny:
                                
                                    if nearest4 == 'null':
                                        nearest4 = [x,y]
                                    if nearest4 != 'null':
                                        if xcoord < x:  
                                            a = x-xcoord
                                        if xcoord > x:
                                            a = xcoord-x
                    
                                        if ycoord < y:
                                            b = y-ycoord
                                        if ycoord > y:
                                            b = ycoord-y
                                    
                                        if xcoord <= nearest4[0]:
                                            c = nearest4[0]-xcoord
                                        if xcoord >= nearest4[0]:
                                            c = xcoord-nearest4[0]
            
                                        if ycoord <= nearest4[1]:
                                            d = nearest4[1]-ycoord
                                
                                        if ycoord >= y:
                                            d = ycoord-nearest4[1]
                                        
                                        if a <= c & b <= d:
                                            #print 'got here'
                                            nearest4 = [x,y]
                i +=1
                    
                                           
                #if nx <= x & ny <= y & nu >= x & nv >= y & self.creature[i][1] != 1:
                #    print str(i)
                    
                                                                                            
            
            if nearest4 == 'null':
                
                return 'random'
            else:
            #find out which direction the nearest is at from coords
                nearx = nearest4[0]
                neary = nearest4[1]
                if nearx == xcoord:
                    if neary == ycoord:
                        nearest4 = 'null'
                        return 0
                if nearx == xcoord:
                    if neary > ycoord:
                        return 'south'
                    if neary < ycoord:
                        return 'north'
                    
                if neary == ycoord:
                    if nearx > xcoord:
                        return 'east'
                    if nearx < xcoord:
                        return 'west'
                        
                if nearx > xcoord:
                    if neary > ycoord:
                        return 'south'
                    if neary < ycoord:
                        return 'north'
                
                if neary > ycoord:
                    if nearx > xcoord:
                        return 'south'
                    if nearx < xcoord:
                        return 'south'
                
                if nearx < xcoord:
                    if neary > ycoord:
                        return 'south'
                    if neary < ycoord:
                        return 'north'
                if neary < xcoord:
                    if nearx > xcoord:
                        return 'north'
                    if nearx < xcoord:
                        return 'north'
                   
        def nearest_mushrm(self,xcoord,ycoord):
#n = [xcoord-30,ycoord-30,xcoord+40,ycoord+40]
            nx = xcoord - 40
            ny = ycoord - 40
            nu = xcoord +50
            nv = ycoord +50
           # print str(nx) + " " +str(ny)+ " " + str(nu) + " " + str(nv)
           #print str(xcoord) + ' ' + str(ycoord)
            
            c =0
            d =0 
            
            thing = []
            nearest3 = 'null'
            i=0
            while i < len(self.mushrm_array):#find out nearest
                
                j = 0
                while j < len(self.mushrm_array):
                    if self.mushrm[j] !=0:
                        thing.append([self.mushrm_array[j][0],self.mushrm_array[j][1]])                               
                    j+=1
                       
                #x = u
                #y = v
                a = 0 #the difference in the x axis
                b = 0
                
                for t in thing:
                    x = t[0]
                    y = t[1]
                   # print str(x) + " " + str(y)
                    if nu >= x:
                        if y <= nv:
                            if nx <= x:
                                if y >= ny:
                                
                                    if nearest3 == 'null':
                                        nearest3 = [x,y]
                                    if nearest3 != 'null':
                                        if xcoord < x:  
                                            a = x-xcoord
                                        if xcoord > x:
                                            a = xcoord-x
                    
                                        if ycoord < y:
                                            b = y-ycoord
                                        if ycoord > y:
                                            b = ycoord-y
                                    
                                        if xcoord <= nearest3[0]:
                                            c = nearest3[0]-xcoord
                                        if xcoord >= nearest3[0]:
                                            c = xcoord-nearest3[0]
            
                                        if ycoord <= nearest3[1]:
                                            d = nearest3[1]-ycoord
                                
                                        if ycoord >= y:
                                            d = ycoord-nearest3[1]
                                        
                                        if a <= c & b <= d:
                                          #  print 'got here'
                                            nearest3 = [x,y]
                i +=1
                    
                                           
                #if nx <= x & ny <= y & nu >= x & nv >= y & self.creature[i][1] != 1:
                #    print str(i)
                    
                                                                                            
            
            if nearest3 == 'null':
                #print 'lol'
                return 'random'
            else:
            #find out which direction the nearest is at from coords
                nearx = nearest3[0]
                neary = nearest3[1]
                if nearx == xcoord:
                    if neary == ycoord:
                        nearest3 = 'null'
                        return 0
                if nearx == xcoord:
                    if neary > ycoord:
                        return 'south'
                    if neary < ycoord:
                        return 'north'
                    
                if neary == ycoord:
                    if nearx > xcoord:
                        return 'east'
                    if nearx < xcoord:
                        return 'west'
                        
                if nearx > xcoord:
                    if neary > ycoord:
                        return 'south'
                    if neary < ycoord:
                        return 'north'
                
                if neary > ycoord:
                    if nearx > xcoord:
                        return 'south'
                    if nearx < xcoord:
                        return 'south'
                
                if nearx < xcoord:
                    if neary > ycoord:
                        return 'south'
                    if neary < ycoord:
                        return 'north'
                if neary < xcoord:
                    if nearx > xcoord:
                        return 'north'
                    if nearx < xcoord:
                        return 'north'
                                                                    

        def nearest_monster(self,xcoord,ycoord):
            #n = [xcoord-30,ycoord-30,xcoord+40,ycoord+40]
            nx = xcoord - 40
            ny = ycoord - 40
            nu = xcoord +50
            nv = ycoord +50
           # print str(nx) + " " +str(ny)+ " " + str(nu) + " " + str(nv)
           #print str(xcoord) + ' ' + str(ycoord)
            
            c =0
            d =0 
            
            thing = []
            nearest2 = 'null'
            i=0
            while i < len(self.monster_array):#find out nearest
                
                j = 0
                while j < len(self.monster_array):
                    thing.append([self.monster_array[j][0],self.monster_array[j][1]])                               
                    j+=1
                       
                #x = u
                #y = v
                a = 0 #the difference in the x axis
                b = 0
                
                for t in thing:
                    x = t[0]
                    y = t[1]
                   # print str(x) + " " + str(y)
                    if nu >= x:
                        if y <= nv:
                            if nx <= x:
                                if y >= ny:
                                
                                    if nearest2 == 'null':
                                        nearest2 = [x,y]
                                    if nearest2 != 'null':
                                        if xcoord < x:  
                                            a = x-xcoord
                                        if xcoord > x:
                                            a = xcoord-x
                    
                                        if ycoord < y:
                                            b = y-ycoord
                                        if ycoord > y:
                                            b = ycoord-y
                                    
                                        if xcoord <= nearest2[0]:
                                            c = nearest2[0]-xcoord
                                        if xcoord >= nearest2[0]:
                                            c = xcoord-nearest2[0]
            
                                        if ycoord <= nearest2[1]:
                                            d = nearest2[1]-ycoord
                                
                                        if ycoord >= y:
                                            d = ycoord-nearest2[1]
                                        
                                        if a <= c & b <= d:
                                            #print 'got here'
                                            self.nearest2 = [x,y]
                i +=1
                    
                                           
                #if nx <= x & ny <= y & nu >= x & nv >= y & self.creature[i][1] != 1:
                #    print str(i)
                    
                                                                                            
            
            if nearest2 == 'null':
                #print 'lol'
                return 'random'
            else:
            #find out which direction the nearest is at from coords
                nearx = nearest2[0]
                neary = nearest2[1]
                if nearx == xcoord:
                    if neary == ycoord:
                        nearest2 = 'null'
                        return 0
                if nearx == xcoord:
                    if neary > ycoord:
                        return 'south'
                    if neary < ycoord:
                        return 'north'
                    
                if neary == ycoord:
                    if nearx > xcoord:
                        return 'east'
                    if nearx < xcoord:
                        return 'west'
                        
                if nearx > xcoord:
                    if neary > ycoord:
                        return 'south'
                    if neary < ycoord:
                        return 'north'
                
                if neary > ycoord:
                    if nearx > xcoord:
                        return 'south'
                    if nearx < xcoord:
                        return 'south'
                
                if nearx < xcoord:
                    if neary > ycoord:
                        return 'south'
                    if neary < ycoord:
                        return 'north'
                if neary < xcoord:
                    if nearx > xcoord:
                        return 'north'
                    if nearx < xcoord:
                        return 'north'
            


        def nearest_creature(self,xcoord,ycoord):
            #n = [xcoord-30,ycoord-30,xcoord+40,ycoord+40]
            nx = xcoord - 40
            ny = ycoord - 40
            nu = xcoord +50
            nv = ycoord +50
           #print str(nx) + " " +str(ny)+ " " + str(nu) + " " + str(nv)
           #print str(xcoord) + ' ' + str(ycoord)
            
            c =0
            d =0 
            
            thing = []
            nearest1 = 'null'
            i=0
            while i < len(self.creature_array):#find out nearest
                
                j = 0
                while j < len(self.creature_array):
                    if self.creature[j][1] != 1:
                                                
                        thing.append([self.creature_array[j][0],self.creature_array[j][1]])
                                                                     
                    j+=1                      
                #x = u
                #y = v
                a = 0 #the difference in the x axis
                b = 0               
                for t in thing:
                    x = t[0]
                    y = t[1]
                    #print str(x) + " " + str(y)
                    if nu >= x:
                        if y <= nv:
                            if nx <= x:
                                if y >= ny:
                                    #print str(t)
                                    if nearest1 == 'null':
                                        nearest1 = [x,y]
                                    if nearest1 != 'null':
                                        if xcoord < x:  
                                            a = x-xcoord
                                        if xcoord > x:
                                            a = xcoord-x
                    
                                        if ycoord < y:
                                            b = y-ycoord
                                        if ycoord > y:
                                            b = ycoord-y
                                    
                                        if xcoord <= nearest1[0]:
                                            c = nearest1[0]-xcoord
                                        if xcoord >= nearest1[0]:
                                            c = xcoord-nearest1[0]
            
                                        if ycoord <= nearest1[1]:
                                            d = nearest1[1]-ycoord
                                
                                        if ycoord >= y:
                                            d = ycoord-nearest1[1]
                                        
                                        if a <= c & b <= d:
                                            #print 'got here'
                                            nearest1 = [x,y]
                i +=1
                
                                           
                #if nx <= x & ny <= y & nu >= x & nv >= y & self.creature[i][1] != 1:
                #    print str(i)
                    
                                                                                            
            
            if nearest1 == 'null':
                #print 'lol'
                return 'random'
            else:
            #find out which direction the nearest is at from coords
                nearx = nearest1[0]
                neary = nearest1[1]
                if nearx == xcoord:
                    if neary == ycoord:
                        nearest1 = 'null'
                        return 0
                if nearx == xcoord:
                    if neary > ycoord:
                        return 'south'
                    if neary < ycoord:
                        return 'north'
                    
                if neary == ycoord:
                    if nearx > xcoord:
                        return 'east'
                    if nearx < xcoord:
                        return 'west'
                        
                if nearx > xcoord:
                    if neary > ycoord:
                        return 'south'
                    if neary < ycoord:
                        return 'north'
                
                if neary > ycoord:
                    if nearx > xcoord:
                        return 'south'
                    if nearx < xcoord:
                        return 'south'
                
                if nearx < xcoord:
                    if neary > ycoord:
                        return 'south'
                    if neary < ycoord:
                        return 'north'
                if neary < xcoord:
                    if nearx > xcoord:
                        return 'north'
                    if nearx < xcoord:
                        return 'north'
                        
                
        
        """
         ACTIONS------------------------------------------------------------------------------------------------------------------
        """  
        def move(self,crtr,obj,arr,direction,away):
            crtr[0] -= 1
            x = arr[0]
            y = arr[1]
            nx = x - 50
            ny = y - 50
            nu = x +60
            nv = y +60
            z = self.obj_size
            if away == 0:
                if direction == 'north':   
                     
                    self.canvas.move(obj,0,-z)
                    arr[1] -= z
                if direction == 'east':    
                                  
                    self.canvas.move(obj,z,0)
                    arr[0] += z
                if direction == 'south':
                    
                    self.canvas.move(obj,0,z)
                    arr[1] += z
                if direction == 'west':    
                                    
                    self.canvas.move(obj,-z,0)
                    arr[0] -= z
                if direction == 'random':
                    randir = ['north','east','south','west']
                    directionr = random.choice(randir)
                    if directionr == 'north':
                        
                        self.canvas.move(obj,0,-z)
                        arr[1] -= z
                    if directionr == 'east':
                        
                        self.canvas.move(obj,z,0)
                        arr[0] += z
                    if directionr == 'south':
                        
                        self.canvas.move(obj,0,z)
                        arr[1] += z
                    if directionr == 'west':
                        
                        self.canvas.move(obj,-z,0)
                        arr[0] -= z
                        
            elif away == 1:#away from
                if direction == 'south':
                    
                    self.canvas.move(obj,0,-z)
                    arr[1] -= z
                if direction == 'west':
                    
                    self.canvas.move(obj,z,0)
                    arr[0] += z 
                if direction == 'north':
                    
                    self.canvas.move(obj,0,z)
                    arr[1] += z
                if direction == 'east':
                    
                    self.canvas.move(obj,-z,0)
                    arr[0] -= z
                if direction == 'random':
                    randir = ['north','east','south','west']
                    directionr = random.choice(randir)
                    if directionr == 'north':
                        
                        self.canvas.move(obj,0,-z)
                        arr[1] -= z
                    if directionr == 'east':
                        
                        self.canvas.move(obj,z,0)
                        arr[0] += z 
                    if directionr == 'south':
                        
                        self.canvas.move(obj,0,z)
                        arr[1] += z
                    if directionr == 'west':
                        
                        self.canvas.move(obj,-z,0)
                        arr[0] -= z
            self.canvas.update()
        
        def eat(self,crtrnum,itemx,itemy,food):
            #find out what were eating strawbs or mushrms
            
            self.creature[crtrnum][0] -= 1
            eating = [itemx,itemy]
            if food == 0:#strawb
                i=0
                while i < len(self.strawb):
                    if eating == self.strawb_array[i]:
                        if self.strawb[i] != 0:
                            print 'NOMMMMM'
                            self.creature[crtrnum][0] += 4 #add 2 energy per strawb
                            #print str(self.creature[crtrnum][0])
                            self.strawb[i] -= 1
                    i+=1
            if food == 1:#mushrm
                i=0
                while i < len(self.mushrm):               
                    if eating == self.mushrm_array[i]:
                        if self.mushrm[i] != 0:
                            #print str(self.creature[crtrnum][0])
                            
                            self.canvas.itemconfig("creature"+ str(crtrnum), fill="blue")
                            self.creature[crtrnum][1] = 1
                            self.mushrm[i] -= 1
                    i+=1
        
                    
            
            
                              
        """
        updates the canvas
        """
        
        def update(self):
                i = 0
                while i < len(self.strawb):#checks if strawbs are still present if not delete from canvas
                    if self.strawb[i] == 0:
                        self.canvas.delete("strawb"+str(i))
                    i+=1
                
                while i < len(self.mushrm):#checks if mushys are still present if not delete from canvas
                    if self.mushrm[i] == 0:
                        self.canvas.delete("mushrm"+str(i))
                    i+=1    
                #creature    
                i = 0
                while i < len(self.creature):#each time step /move deducts 1 point from energy.... For each creature
                   # self.creature[i][0] -= 1#for now
                    if self.creature[i][1] != 1:
                        if self.creature[i][0] == 0:#if ran out of energy die
                            self.creature[i][1] = 1
                            self.canvas.itemconfig("creature"+str(i), fill='blue')
                            
                        j = 0    
                        while j < len(self.monster):
                            carr = str(self.creature_array[i])
                            marr = str(self.monster_array[j])
                            
                            if carr == marr:#if on same spot as monster die
                                self.creature[i][1] = 1
                                self.canvas.itemconfig("creature"+str(i), fill='blue')
                            j += 1
                        
                        #sense/act? here
                        cstr = 'creature' + str(i)
                        #move(self,obj,arr,direction,away)
                        # print cstr
                        x = self.creature_array[i][0]
                        y = self.creature_array[i][1]
                        #dire = self.nearest_mushrm(x,y)
                        
                        if self.creature[i][1] != 1:#if not dead
                            
                            #print str(self.strawb)
                            """#makes craetures go after strawbs
                            if self.mushrm_present(x,y) == 1:
                                self.eat(i,x,y,1)
                            if self.mushrm_present(x,y) == 0:
                                self.move(self.creature[i],cstr,self.creature_array[i],dire,0)
                            v    """  
                            #chromosome stuff here
                            action_list = []
                            chrm = self.chromosome[i]
                            #mushrm eater 
                            #chrm = ['eat','ignore','0','ignore','ignore','ignore','random',5,1,6,3,4,2]
                            """
                            having atleast one good-ish chromosome makes a difference
                            """
                            #straw eater chrm = ['ignore','eat','ignore','0','ignore','away','random',1,5,3,6,4,2]
                            
                            weight = []
                            k = 7
                            
                            while k < len(chrm):# made a weights thing to make calculation easy
                                cool = int(chrm[k])
                                weight.append(cool)
                                k+=1
                            
                            #for sensory functions 1-6
                            mp = self.mushrm_present(x,y)
                            if mp != 'null':
                                #calc action by lookup
                                action = chrm[0]
                                if action != 'ignore':
                                    action_list.append(action)
                                else:
                                    action_list.append('ignore')
                            sp = self.strawb_present(x,y)
                            if sp != 'null':
                                action = chrm[1]
                                if action != 'ignore':
                                    action_list.append(action)
                                else:
                                    action_list.append('ignore') 
                                                               
                            nm = self.nearest_mushrm(x,y)
                            if nm != 0:
                                action = chrm[2]
                                if action != 'ignore':
                                    action_list.append(action)
                                else:
                                    action_list.append('ignore')
                            else:
                                action_list.append('ignore')                                    
                            ns = self.nearest_strawb(x,y)
                            #print str(ns)
                            if ns != 0:
                                action = chrm[3]
                                if action != 'ignore':
                                    action_list.append(action)
                                else:
                                    action_list.append('ignore')
                            else:
                                action_list.append('ignore')
                            nc = self.nearest_creature(x,y)
                            if nc != 0:
                                action = chrm[4]
                                if action != 'ignore':
                                    action_list.append(action)
                                else:
                                    action_list.append('ignore')
                            else:
                                action_list.append('ignore')                                                                
                            nr = self.nearest_monster(x,y)
                            if nr != 0:
                                action = chrm[5]
                                if action != 'ignore':
                                    action_list.append(action)
                                else:
                                    action_list.append('ignore')
                            else:
                                action_list.append('ignore')                            
                            #if action list is empty// is all ignore// do default
                            
                            p = 0
                            ign = 0
                            while p < len(action_list):
                                 if action_list[p] == "ignore":
                                     ign += 1
                                 p += 1
                            
                            if ign == len(action_list):
                                default_dire = chrm[6]
                                self.move(self.creature[i],cstr,self.creature_array[i],default_dire,0)
                            else:
                                #determine strongest weight and which action
                                p=0
                                maxp = 0
                                maxw = -1
                                
                                while p < len(weight):
                                    if action_list[p] != 'ignore':
                                        if weight[p] > maxw:
                                            maxp = p
                                            maxw = weight[p]
                                    p += 1
                                
                                if maxp == 0:
                                    self.eat(i,x,y,1)
                                if maxp == 1:
                                    self.eat(i,x,y,0)
                                if maxp == 2:
                                    if action_list[maxp] == 'random':
                                        nm = 'random'
                                        self.move(self.creature[i],cstr,self.creature_array[i],nm,0)
                                    else:
                                        self.move(self.creature[i],cstr,self.creature_array[i],nm,int(action_list[maxp]))
                                if maxp == 3:
                                    if action_list[maxp] == 'random':
                                        ns = 'random'
                                        self.move(self.creature[i],cstr,self.creature_array[i],ns,0)
                                    else:
                                        self.move(self.creature[i],cstr,self.creature_array[i],ns,int(action_list[maxp]))                                
                                if maxp == 4:
                                    if action_list[maxp] == 'random':
                                        nc = 'random'
                                        self.move(self.creature[i],cstr,self.creature_array[i],nc,0)
                                    else:
                                        self.move(self.creature[i],cstr,self.creature_array[i],nc,int(action_list[maxp]))                                    
                                if maxp == 5:
                                    if action_list[maxp] == 'random':
                                        nr = 'random'
                                        self.move(self.creature[i],cstr,self.creature_array[i],nr,0)
                                    else:
                                        self.move(self.creature[i],cstr,self.creature_array[i],nr,int(action_list[maxp]))                               
                            
                            
                            # pos      role                     action
                            # 0       action mushrm present     eat/ignore
                            # 1       action STrawb present     eat/ignore
                            # 2       action near mush          towards=0/away=1/random/ignore
                            # 3       action near strawb        towards=0/away=1/random/ignore
                            # 4       action near creature      towards=0/away=1/random/ignore
                            # 5       action near monster       towards=0/away=1/random/ignore
                            # 6       default-------------      random/north/east/south/west
                            # 7       pos1 weight       
                            # 8       pos2 weight
                            # 9       pos3 weight
                            # 10      pos4 weight
                            # 11      pos5 weight
                            # 12      pos6 weight
                            #test chrm = ['ignore','eat','ignore','0','ignore','away','random',1,6,3,4,5,2]                                                                                                             
                    i += 1
                                 
                #monster
                if self.timestep % self.mstep == 0:#moves every two counts
                    z=0
                    while z < len(self.monster_array):
                        
                        x = self.monster_array[z][0]
                        y = self.monster_array[z][1]
                        dire = self.nearest_creature(x,y)
                        if dire == 0:
                            dire = 'random'
                        
                        #print str(dire)
                        #print str(self.creature)
                        mnstr = 'monster' + str(z)
                       # print mnstr                      
                        self.move(self.monster[z],mnstr,self.monster_array[z],dire,0)
                        z += 1
                i=0
                while i < len(self.strawb):#checks if strawbs are still present if not delete from canvas
                    if self.strawb[i] == 0:
                        self.canvas.delete("strawb"+str(i))
                    i+=1
                while i < len(self.mushrm):#checks if mushys are still present if not delete from canvas
                    if self.mushrm[i] == 0:
                        self.canvas.delete("mushrm"+str(i))
                    i+=1        
                self.timestep += 1
                
                if self.timestep != self.timelimit:
                    print 'generation:' + str(self.gl) + " timestep:" + str(self.timestep)
                    self.canvas.after(self.wait_time, self.update)
                else:
                    #one iteration of tielimit = one generation... evolve from here
                    
                    if self.gl != self.generation:
                        print 'now'
                        self.timestep = 0
                        avg = []
                        for c in self.creature:
                            avg.append(c[0])
                        sm = sum(avg)
                        avrg = sm/len(avg)    
                        self.generation_averages.append(avrg)
                        #evolve here gonna tournament
                        #pick a subset of n
                        subfit = []#has fitness
                        subchrom = [] #chromosome
                        i = 0
                        while i < self.subsize:
                            rnd = random.randrange(0,self.cp,1)
                            subfit.append(self.creature[rnd][0])
                            subchrom.append(self.chromosome[rnd])
                            i += 1
                        maxfit = -1#find first parent fittest
                        maxi = 0
                        i = 0
                        while i < len(subfit):
                            if subfit[i] > maxfit:
                                maxfit = subfit[i]
                                maxi = i
                            i +=1
                        p1 = subchrom[maxi]
                        subchrom.pop(maxi)
                        subfit.pop(maxi) 
                        maxfit = -1#find second parent fittest
                        maxi = 0
                        i = 0
                        while i < len(subfit):
                            if subfit[i] > maxfit:
                                maxfit = subfit[i]
                                maxi = i
                            i +=1
                        p2 = subchrom[maxi]                         
                        #crossover chromo length is 13
                        #crossover point will be after default so 7
                        probabilitator = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,]
                        new = []
                        i=0
                        while i < 13:
                            if i != 7:
                                new.append(p1[i])
                            else:
                                new.append(p2[i])
                            i+=1
                        #low probability mutation note:couldnt be bothered for second half
                        if random.choice(probabilitator) == 1:#lucky 10%
                            index = random.randrange(0,12,1)
                            if index < 6:
                                newval = random.choice(['0','1','random','ignore'])
                                new[index] = newval
                            if index ==6:
                                newval = random.choice(['random','north','south','east','west'])
                                new[index] = newval
                            if index > 6:
                                newval = random.randrange(1,6,1)
                                oldy = 0
                                y = 7
                                while y < 13:
                                    if newval == new[y]:
                                        oldy = new[y]
                                        new[y] = new[index]
                                        new[index] = oldy 
                                    y +=1
                                
                        self.ulti = new        
                        self.canvas.delete('all')
                        
                        """======================================================================================
                        """
                        
                        self.strawb_array = []#this contains the location
                        self.strawb = []#this contains the number of strawberrys in this location
                        self.mushrm_array = []
                        self.mushrm = []
            
                        #creatur and Monster data sets
                        self.creature_array = []#location of creature
                        self.creature = []#creature's enrgy, and state
                        self.chromosome = []
                        self.monster_array = []
                        self.monster = []#myt hold monster's energy level?

            
                        #add creatures and monsters to arrays and make sure not
                        i =0 
                        while i < self.cp:
                            self.creature_array.append([self.randy(),self.randy()])
                            self.chromosome.append(new)
                            self.creature.append([self.energy,0])#creature energy set to 10
                            i += 1
                        i =0 
                        #print str(len(self.chromosome[11]))
                        while i < self.mp:

                            self.monster_array.append([self.randy(),self.randy()])
                            self.monster.append([10,0])  
                            i += 1                
            
                        l = 0
                        while l < self.cp:
                            x = self.creature_array[l]
                            p = 0
                            while p < self.mp:
                                y = self.monster_array[p]
                                if x == y:
                                    newlocation = [self.randy(),self.randy()]
                                    self.monster_array[p] = newlocation
                                p += 1  
                            l += 1
    
                        #add strawbs and mushrooms with random locations
                        i = 0
                        while i < self.itm_count:
                            self.strawb_array.append([self.randy(),self.randy()])
                            self.strawb.append(random.randrange(1,5,1))
                            self.mushrm_array.append([self.randy(),self.randy()])
                            self.mushrm.append(random.randrange(1,5,1))
                            i += 1
                
                        #make sure not same spot
                        i = 0
            
                        while i < self.itm_count:
                            x = self.strawb_array[i]
                            if i < self.cp:
                                c = self.creature_array[i]
                                p = 0
                                while p < self.cp:
                                    y = self.creature_array[p]
                                    if x == y:
                                        newlocation = [self.randy(),self.randy()]
                                        self.creature_array[p] = newlocation
                                    p += 1
                            j = 0
                            while j < self.itm_count:
                                y = self.mushrm_array[j]
                                if x == y:
                                    newlocation = [self.randy(),self.randy()]
                                    self.mushrm_array[j] = newlocation
                            
                                j += 1  
                            i += 1
                
                        #insert mushroom and strawberrys in the field
                        i = 0
                        j = 0
                        while i < self.itm_count:
                            x = self.strawb_array[i]
                            y = self.mushrm_array[i]
                            
                            self.ins_strawb(x[0],x[1],i)
                            self.ins_mushrm(y[0],y[1],i)
                            i += 1
            
                        #insert creature and mosnter to field    
                        i = 0
                        while i < self.cp:
                            x = self.creature_array[i]
                            self.ins_creature(x[0],x[1],i)
                            i += 1
                        i = 0
                        while i < self.mp:
                            y = self.monster_array[i]
                            self.ins_monster(y[0],y[1],i)
                            i += 1
            
        
                
                        self.gl += 1 
                        #update canvas each second
                        self.canvas.after(self.wait_time, self.update)                                                            
                        
      
                    else:
                        print str(self.generation_averages)
                        print str(self.ulti)
                        self.canvas.delete('all')
                        
                    
                    

                    
                   
            
        """----------------------------------------------------------------------------------------------------------------------------------------
        the species class which has the monster and creature species as subclass?     
        """
        def __init__(self,parent,width = 200, height = 200,itm_count=10,obj_size=10, wait_time=1000,cp = 3,mp=2,energy = 15,mstep =2,timelimit = 50,generation = 5,subsize=5):
            sys.setrecursionlimit(1500)
            self.ulti = []
            self.subsize = subsize
            self.generation = generation
            self.gl = 0
            self.generation_averages = []
            self.timelimit = timelimit
            self.mstep = mstep
            self.energy = energy
            self.width = width
            self.height = height
            self.randsize = width
            self.timestep = 0
            self.obj_size = 10
            self.canvas = Canvas(width=width, height=height)
            self.canvas.grid(column=0,row=0)
            self.canvas.wait_visibility()
            self.itm_count = itm_count
            self.wait_time=wait_time
            
            self.nearest1 = 'null' #bad coding
            self.nearest2 = 'null'
            self.nearest3 = 'null'
            self.nearest4 = 'null'
            #population for mosnter and creature
            self.cp = cp
            self.mp = mp
                
            #arrays for location, just the names for stats
                
            #Strawberry & mushrm data sets
            self.strawb_array = []#this contains the location
            self.strawb = []#this contains the number of strawberrys in this location
            self.mushrm_array = []
            self.mushrm = []
            
            #creatur and Monster data sets
            self.creature_array = []#location of creature
            self.creature = []#creature's enrgy, and state
            self.chromosome = []
            self.monster_array = []
            self.monster = []#myt hold monster's energy level?
            """
            maybe later add a survived stat showing how long it survived
            """
            
            #manual initialise of chromosome
            present_action = ['eat','ignore']
            default_action = ['random','north','east','south','west']
            nearest_action = ['0','1','random','ignore']# 0 =towards, 1 = away
            #need to shuffle 1-6
            wei = ['1','2','3','4','5','6']
            
            
            
            
            #add creatures and monsters to arrays and make sure not
            i =0 
            while i < cp:
                self.creature_array.append([self.randy(),self.randy()])
                random.shuffle(wei)
                self.chromosome.append([random.choice(present_action),random.choice(present_action),random.choice(nearest_action),random.choice(nearest_action),random.choice(nearest_action),random.choice(nearest_action),random.choice(default_action),wei[0],wei[1],wei[2],wei[3],wei[4],wei[5]])
                self.creature.append([self.energy,0])#creature energy set to 10
                i += 1
            i =0 
            #print str(len(self.chromosome[11]))
            #straw eater "ELITE"
            self.chromosome[0] = ['ignore','eat','ignore','0','ignore','away','random',1,5,3,6,4,2]
            while i < mp:

                self.monster_array.append([self.randy(),self.randy()])
                self.monster.append([10,0])  
                i += 1                
            
            l = 0
            while l < cp:
                x = self.creature_array[l]
                p = 0
                while p < mp:
                    y = self.monster_array[p]
                    if x == y:
                        newlocation = [self.randy(),self.randy()]
                        self.monster_array[p] = newlocation
                    p += 1  
                l += 1
    
            #add strawbs and mushrooms with random locations
            i = 0
            while i < itm_count:
                self.strawb_array.append([self.randy(),self.randy()])
                self.strawb.append(random.randrange(1,5,1))
                self.mushrm_array.append([self.randy(),self.randy()])
                self.mushrm.append(random.randrange(1,5,1))
                i += 1
                
            #make sure not same spot
            i = 0
            
            while i < itm_count:
                x = self.strawb_array[i]
                if i < cp:
                    c = self.creature_array[i]
                    p = 0
                    while p < cp:
                        y = self.creature_array[p]
                        if x == y:
                            newlocation = [self.randy(),self.randy()]
                            self.creature_array[p] = newlocation
                        p += 1
                j = 0
                while j < itm_count:
                    y = self.mushrm_array[j]
                    if x == y:
                        newlocation = [self.randy(),self.randy()]
                        self.mushrm_array[j] = newlocation
                
                    j += 1  
                i += 1
                
            #insert mushroom and strawberrys in the field
            i = 0
            j = 0
            while i < itm_count:
                x = self.strawb_array[i]
                y = self.mushrm_array[i]
                
                self.ins_strawb(x[0],x[1],i)
                self.ins_mushrm(y[0],y[1],i)
                i += 1
            
            #insert creature and mosnter to field    
            i = 0
            while i < cp:
                x = self.creature_array[i]
                self.ins_creature(x[0],x[1],i)
                i += 1
            i = 0
            while i < mp:
                y = self.monster_array[i]
                self.ins_monster(y[0],y[1],i)
                i += 1
            
        
                
                
            #update canvas each second
            self.canvas.after(self.wait_time, self.update())
            
   
  

                                 
                        

root = Tk()
main = Evolve(root,width =400,height=400,itm_count = 50,obj_size=10,wait_time=200,cp = 30, mp=10, energy = 30, mstep= 2, timelimit = 35, generation = 5,subsize=20)
root.mainloop()