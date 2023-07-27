a1=[2,5,'abc','welcome',7.4,'a']
print(a1)
print(a1[5]) #output is 'a'
print(a1[0:5]) # here 0:5 is index numbers output is 2,5,abc,welcome,7.4
print(a1[2]) # output is abc which is index number of 2
a1.append("python") #append is a function in python for adding a element to end of alist
print(a1) #output [2,5,abc,welcome,7.4,a,python]
a1.insert(3,44) # insert is a function to insert an element in a specific position to a list
print(a1)
a1[3]="kiran"
print(a1) #output is 2,5,abc,kiran,welcome,7.4,a,python
a1.pop() #pop removes end of the element by defaultly
print(a1)
a1.pop(1) # based on index number index number it removes that element
print(a1) #output is 5,abc,kiran,welcome,7.4,a
a1.remove('kiran')# remove function removes specific element
print(a1)
#print is a function for getting output on console
print(a1)  # after print we need to give a right click and run the file for output
