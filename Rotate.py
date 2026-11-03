"""Write a program that rotates the element 
   of a list so that the element at the first 
   index moves to the second index, the element 
   in the second index moves to the third index, 
   etc., and the element in the last index moves 
   to the first index."""
list = eval(input("Enter the list : "))
last=list.pop()
list.insert(0,last)
print("The rotated list is : ",list)
