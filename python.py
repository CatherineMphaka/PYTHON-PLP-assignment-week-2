#create an empty list called my_list
my_list=[]
#append the following elements to my_list: 10,20,30,40
my_list.append(10)
my_list(20)
my_list(30)
my_list(40)
#insert the value 15 at the second position on the list
my_list[1]=15
#extend my_list with another list: [50,60,70]
other_list=[50,60,70]
my_list.extend(other_list)
#remove the last element from my_list
del my_list[-1]
#sort my_list in ascending order
my_list.sort()
#find and print the index of the value 30 in my_list
print(my_list.index(30))