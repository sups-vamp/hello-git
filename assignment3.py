#question-1
a=[]
size=int(input("enter size of list"))
for i in range(0,size):
    ans=input("")
    a.append(ans)
print(a)

#question-2
b=["google","apple","facebook","microsoft","tesla"]
a.append(b)
print(a)

#question-3
#taking 'a' as our base list
ans=input("enter the object whose frequency you want to check")
print(ans," ","occurs"," ",a.count(ans)," times")

#question-4
num_list=[10,5,2,7,5,1,99]
num_list.sort()
print(num_list)

#question-5
a=[1,2,6,10]
b=[3,5,11,12]
c=[]
c=a+b
c.sort()
print(c)

#question-6
#reference taken from geeks for geeks website
#stack
stack = ["A", "B", "C"]
print(stack)
print(stack.pop())      #pop will remove the last element....stack follows last in first out principle.
print(stack)
print(stack.pop())
print(stack)

#queue
from collections import deque
queue = deque(["A", "B", "C", "D"])
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)

#question-7(optional question)
a=[]
even=0
odd=0
size=int(input("enter size of the list"))
for i in range(0,size):
    ans=int(input(""))
    a.append(ans)
    if ans%2==0:
        even+=1
    else:
        odd+=1;
print("list is-",a)
print("list contains %d odd and %d even numbers."%(odd,even))
