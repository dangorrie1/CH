#import sys
#import os


rd = []
list1 = []
fractionlist = []
route_hold_list = []
list2 = []
volumelist = {}
pairlist = {}
x = 0
number_routes = 0
route_count = 0
key_link = 0
volume = 0

input = open('I_95_Existing AM_V4_COMscript_routes.inp' , 'r')
Directory = input.readlines()
#reads the text file as a list, with each line a seperate element


for line in Directory:
    if line == "-- Routing Decisions: --":
        listbegin = line
    elif line == "-- Desired Speed Decisions: --":
        listend = line
    else:
        pass  
rd = Directory [listbegin : listend]    

for line in Directory:
    if line == "-- Inputs: --":
        m = line
    elif line == "-- Traffic Compositions: --":
        n = line
    else:
        pass
input_list = Directory [m:n]
  
#cuts out irrelevant sections of the list

for line in input_list:
    line.split()
for line in rd:
    line.split([]) 
#each element in the list is now a list; each word in the text file is an element

 
    

def routing_decision_count(): #counts the total number of routing decisions
    count = []
    for line in rd:
        if line[0] == 'ROUTING_DECISION':
            count.append(1)
            x = len(count)
        return x
       
        
        
def routing_decision_isolate(): #isolates a single route from the list rd
    for line in rd:
        if line [0] == 'ROUTING_DECISION':
            listbegin1 = line
            next()
            listend1 = line
            StopIteration
            list1 = rd[listbegin1 : listend1]
            s = list1 [1]
            originlink = s [1]
        else:
            pass
    return originlink, list1

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
    while x < route_count:   
        for line in list1:
            if x == 0 and line[0] == 'ROUTE':
                listbegin2 = line
                next ()
                listend2 = line
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

    links = b + temp + list2[3:]
    route_hold_list.append(links)
    number_routes = len(route_hold_list)               

    return number_routes

def key_link_identify():
    for line in list1:
        if line[0] == 'LINK':
            key_link = line[1]
            
    return key_link
 
def route_manipulate():
    
    
    
    return

        
     
#creates a list with the fraction for the first route.the goal here is to extend the list
#to match the length of the list contining the routes. The fraction will then be manipulated, 
#calcualting the volume. This list, and the list of routes will be combined in a dictionary, 
#with each route being a key for the fraction. At that point, we will simply have to run a 
#sort function in the dictionary, and add up all thev volume values that are called for by 
#the same key     
def fraction_list_create():                 
    for line in list1:                      
        if line[0] == 'FRACTION':
            fraction = line [1]
            fractionlist.append(fraction)
            fraction_sum = sum(fractionlist)
            decimal = fraction / fraction_sum
        else:
            pass   
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

def volume_identify():
    for line in input_list:
        if line[0] == 'LINK' and line[1] == key_link:
            volumelist[key_link] = line[4]
    return volumelist

           


