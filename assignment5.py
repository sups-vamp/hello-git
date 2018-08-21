#question-1
year=int(input("enter a year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("year is a leap year")
        else:
            print("not a leap year")
    else:
        print("year is a leap year")
else:
    print("not a leap year")


#question-2
length=int(input("enter length"))
breadth=int(input("enter breadth"))
if length==breadth:
    print("its a square")
else:
    print("its a rectangle")


#question-3
age1=int(input("enter age of first person"))
age2=int(input("enter age of second person"))
age3=int(input("enter age of third person"))
if age1>age2 and age1>age3:
    print("first person is the oldest")
elif age2>age1 and age2>age3:
    print("second person is the oldest")
else:
    print("third person is the oldest")
if age1<age2 and age1<age3:
    print("first person is the youngest")
elif age2<age1 and age2<age3:
    print("second person is the youngest")
else:
    print("third person is the youngest")


#question-4
age=int(input("enter age of person"))
sex=input("your sex?")
st=input("your marital status?")
if age>60 and age<20:
    print("error")
else:
    if sex=='female':
        print("you'll work only in urban areas.")
    else:
        if age>20 and age<40:
            print("you can work anywhere")
        else:
            print("you'll work only in urban areas.")


#question-5
quan=int(input("enter quantity"))
quan=quan*100
if quan>1000:
    quan=quan-(quan*0.1)
print("final payment:",quan)

# LOOPS

#question-6
a=[]
for i in range(0,10):
    num=int(input(""))
    a.append(num)
print(a)


#question-7
a=0
while a==0:
    print("hi")


#question-8
a=[]
b=[]
for i in range(0,5):
    num=int(input(""))
    a.append(num)
    b.append(num*num)
print(a)    #list of original numbers
print(b)    #list of their squares


#question-9


#question-10
a=[]
for j in range(1,101):
    flag=0
    if j==2:
        a.append(j)
    else:
        for i in range(2,j):
            if j%i==0:
                flag=1
                break;
            else:
                flag=0
        if flag==0:
            a.append(j)
a.remove(1)
print(a)
        

#question-11
for i in range(0,4):
    for j in range(0,i+1):
        print("*",end='')
    print("\r")

#question-12
a=[]
for i in range(0,10):
    num=int(input(""))
    a.append(num)
num=int(input("enter number you want to delete"))
a.remove(num)
print(a)
    
