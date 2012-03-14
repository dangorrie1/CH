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
#m = 0
#while m < rd_count:
for line in rd:
    for item in line:
        if item == 'ROUTING_DECISION':
            temp_list.append(rd.index(line))
                    
                    
listbegin = temp_list[perm_counter]
listend = temp_list[perm_counter + 1]
perm_counter = perm_counter + 1

#print("perm_counter = " perm_counter)
#print(listbegin)
#print(listend)

#this is the first routing decision
routing_list = rd[listbegin:listend]

print(routing_list)

#these are some general manipulations. they could be moved above later, so as to take them out of the while loop
for line in routing_list:                      
    for item in line:
        if item == 'FRACTION':
            fraction = line [1]
            fractionlist.append(float(fraction))
            fraction_sum = sum(fractionlist)
            decimal = fractionlist[0] / fraction_sum
    else:
        pass   

print(fraction)
print(decimal)   

    
for line in input_list:
    for item in line:
        if item == 'LINK' and item == key_link:
            volumelist[key_link] = line[4]
    
volume = volumelist[key_link] * decimal



