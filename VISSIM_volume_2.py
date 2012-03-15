'''
Created on Mar 14, 2012

@author: daniel
'''

from Tkinter import *
import tkFileDialog
 
 
master = Tk()
master.withdraw() #hiding tkinter window

input_list = [] 
temp_list = []
temp_route_list = []
temp1 = [] 
temp2 = [] 
rd = []
fractionlist = []
route_hold_list = []
route_list = []
list2 = []
destination_list = []
link_list = []
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
input_volume = 0
ultimate_list = []

#to be used in while loops
perm_counter = 1
perm_route_counter = 1



file_path = tkFileDialog.askopenfilename(title="Open file", filetypes=[("VISSIM File",".inp"),("All files",".*")])
f = open(file_path)
Directory = f.readlines()


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




count = 0
for line in rd:
    for item in line:
        if item == 'ROUTING_DECISION':
            count = count + 1
rd_count = count
#print(rd_count)                                

       
        
        
# Section below isolates an individual routing decision from the list of all routing decisions

for line in rd:
    for item in line:
        if item == 'ROUTING_DECISION':
            temp_list.append(rd.index(line))

#beginning of first while loop

while perm_counter < rd_count:                   
                    
    listbegin = temp_list[perm_counter-1]
    listend = temp_list[perm_counter]
    perm_counter = perm_counter + 1
    
    
    #this is the first routing decision
    #will need code to clear and reset for subsequent iterations
    routing_list = rd[listbegin:listend]
    
    for line in routing_list:                      
        for item in line:
            if item == 'FRACTION':
                fraction = line [1]
                fractionlist.append(float(fraction))
                fraction_sum = sum(fractionlist)
                
        else:
            pass   
    
    
    
    count = 0
    for line in routing_list:
        for item in line:
            if item == 'ROUTE':
                count = count + 1
    route_count = count
    
    
    
    for line in routing_list:
        for item in line:
            if item == 'LINK':
                for item in line:
                    if item == 'DESTINATION':
                        destination_link = line[4]
                        destination_list.append(destination_link) 
                    elif line[0] != 'ROUTE':
                        key_link = line [1]
            
            
                
    #print(key_link)
    #print(destination_list)
    
    
    
        
    #isolates the individual route, will be looped in a while loop to accomodate each route   
    for line in routing_list:
        for item in line:
            if item == 'ROUTE':
                temp_route_list.append(routing_list.index(line))



while perm_route_counter < (route_count-1):
    
    link_list = []       
    routelistbegin = temp_route_list[perm_route_counter-1]
    routelistend = temp_route_list[perm_route_counter]
    
    
    route_list = routing_list[routelistbegin : routelistend]
    
    #print(route_list)
    
    #following codeseparates the individual links from the rest and appends to a list
    link_list.append(destination_list[perm_route_counter-1])
    print(destination_list[perm_route_counter-1])
    link_list.append(key_link)
    print(key_link)
    
    a = route_list[2]
    for item in a[1:]:
        link_list.append(item)
        
    for line in route_list[3:]:
        for item in line:
            link_list.append(item)
    
    link_list.sort()
    print(link_list)
    
    for item in link_list:
        ultimate_list.append(item)
    
    
    decimal = fractionlist[perm_route_counter-1] / fraction_sum
    
    for line in input_list:
        for item in line:
            if item == 'LINK':
                for item in line:
                    if item == key_link:
                        input_volume = line[3]   
    volume = float(input_volume) * decimal
    print(volume)
    
    perm_route_counter = perm_route_counter + 1
    
    for item in link_list:
        pairlist[item] = volume
    #OUTPUT
    import simplejson
    f = open('/home/daniel/CH/output.txt', 'w')
    simplejson.dump(pairlist, f)
    
    
    print(pairlist)


f.close()