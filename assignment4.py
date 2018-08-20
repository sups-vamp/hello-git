#question-1
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1[::-1])


#question-2
a=input("enter a string")
a=list(a)
l=len(a)
for i in range(0,l):
    if a[i].isupper():
        print(a[i])

#question-3
a=input("enter a string")
a = list(map(int, a))       #reference taken from net.(map)
print(a)

#question-4
a=input("enter string")
c=a[::-1]
c="".join(c)
if a==c:
    print("palindrome")
else:
    print("not a palindrome")

    
#question-5
import copy as cop
a=[1,2,3,[9,10],4,5]
b=cop.deepcopy(a)
a[3][0]='yes'       #changes are made in list a.these changes won't reflect in list b as the concept of deep copy is used.
print(a)
print(b)
#the difference between shallow and deep copy is, that in shallow copy, if an object contains a reference to any mutable object then the duplicate reference variables will also point to the same content;changes made in the original object will be seen in the duplicate object as well.
#But in deep copy every single thing is copied, even the references. changes made in first object will not affect the other.


  

