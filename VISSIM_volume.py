#import sys
#import os
from Tkinter import *
import tkFileDialog
 
 
master = Tk()
master.withdraw() #hiding tkinter window

input_list = [] 
temp_list = []
temp1 = [] 
temp2 = [] 
rd = []
list1 = []
fractionlist = []
route_hold_list = []
list2 = []
volumelist = {}
pairlist = {}
x = 0
m = 0
n = 0
number_routes = 0
route_count = 0
key_link = 0
volume = 0
rd_count = 0
listbegin = 0
listend = 0
perm_counter = 0


file_path = tkFileDialog.askopenfilename(title="Open file", filetypes=[("VISSIM File",".inp"),("All files",".*")])
f = open(file_path)
Directory = f.readlines()
#print(Directory)
#print(len(Directory))
#print(Directory[3050:3070])

#reads the text file as a list, with each line a seperate element

listbegin = Directory.index("-- Routing Decisions: --\r\n")
listend = Directory.index("-- Desired Speed Decisions: --\r\n")
m = Directory.index("-- Inputs: --\r\n")
n = Directory.index("-- Traffic Compositions: --\r\n") 
        
#print(listbegin)    
#print(listend)
a = Directory[listbegin : listend] 
temp1.append(a)   

a = Directory [m:n]
temp2.append(a)
  
#cuts out irrelevant sections of the list

for line in temp1:
    for item in line:
        a = item.split()
        rd.append(a)
for line in temp2:
    for item in line:
        a = item.split()
        input_list.append(a)
#each element in the list is now a list; each word in the text file is an element

#print(rd)
#print(input_list) 
    


count = 0
for line in rd:
    for item in line:
        if item == 'ROUTING_DECISION':
            count = count + 1
rd_count = count
#print(rd_count)                                

       
        
        
def routing_decision_isolate(): #isolates a single routing decision from the list rd
    m = 0
    while m < rd_count:
        for line in rd:
            for item in line:
                if item == 'ROUTING_DECISION':
                    temp_list.append(rd.index(line))
                    
                    
    listbegin = temp_list[perm_counter]
    listend = temp_list[perm_counter]
    perm_counter += 1                
                    
                
'''
                if item == 'ROUTING_DECISION' and m == 0:
                    
                    listbegin1 = rd.index(line)
                    next()
                    listend1 = rd.index(line)
                    StopIteration
                    list1 = rd[listbegin1 : listend1]
                    
                    print(list1)
                    
                    #volume_identify()
                    #route_counter()
                    #route_isolate()
                
                elif item == 'ROUTING_DECISION' and m != 0:
                    n = m
                    while n > 0:
                        next()
                        n = n - 1
                    listbegin1 = rd.index(line)
                    next()
                    listend1 = rd.index(line)
                    StopIteration
                    list2 = rd[listbegin1 : listend1]
                    
                    print(list2)
                    
                    #volume_identify()
                    #route_counter()
                    #route_isolate()
                    '''
                
            else:
                pass
                    
    return 

def route_counter(): #counts the number of routes in a given routing decision
    count1 = []
    for line in list1:
        if line[0] == 'ROUTE':
            count1.append(1)
        else:
            pass
        route_count = len(count1)
    
    return route_count
    
def route_isolate(): #isolates a single route from within the routing decision   
    key_link_identify ()
    
    while x < route_count:   
        for line in list1:
            if x == 0 and line[0] == 'ROUTE':
                listbegin2 = line
                next ()
                listend2 = line
                StopIteration
                list2.append(list1[listbegin2 : listend2])
                                
                links_isolate()
                
                x = x + 1 
               
                
            elif x!= 0 and line [0] == 'ROUTE':
                t = x
                while t > 0:
                    next()
                    t = t-1
                listbegin2 = line
                next ()
                listend2 = line
                StopIteration
                list2.append(list1[listbegin2 : listend2])
                
                
                links_isolate()
                
                x = x + 1   
            else:
                pass
            
                    

        return 
    
    
    
def links_isolate(): #isolates all the links in a given route and appends them to a list.
    a = list2 [0]
    b = a [4]
                
    a = list2 [2]
    temp = a [1:]

    links = b + temp + list2[3:] + key_link
    route_hold_list.append(links)
    
    for link in route_hold_list:
        pairlist[link] = volume              

    return pairlist

def key_link_identify(): #identifies the first link -- ties in with inputs
    for line in list1:
        if line[0] == 'LINK':
            key_link = line[1]
            
    return key_link
 

        
     
#creates a list with the fraction for the first route.the goal here is to extend the list
#to match the length of the list contining the routes. The fraction will then be manipulated, 
#calcualting the volume. This list, and the list of routes will be combined in a dictionary, 
#with each route being a key for the fraction. At that point, we will simply have to run a 
#sort function in the dictionary, and add up all thev volume values that are called for by 
#the same key     

def volume_identify():                 
    for line in list1:                      
        if line[0] == 'FRACTION':
            fraction = line [1]
            fractionlist.append(fraction)
            fraction_sum = sum(fractionlist)
            decimal = fraction / fraction_sum
        else:
            pass   
    
    
    for line in input_list:
        if line[0] == 'LINK' and line[1] == key_link:
            volumelist[key_link] = line[4]
    
    volume = volumelist[key_link] * decimal
    
    return volume        

def input_count():
    count1 = []
    for line in input_list:
        if line [0] == 'INPUT':
            count1.append(line)
            count_length = len(count1)
        else:
            pass
            
    return count_length


    
''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''



routing_decision_isolate()








           


