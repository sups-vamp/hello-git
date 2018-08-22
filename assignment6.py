#question-1
'''def calculate(rad):
    return(4*3.14*rad*rad)
rad=int(input("enter radius"))
print(calculate(rad))'''


#question-2
def perfect(num):
    sum=0
    for j in range(1,num):
        if num%j==0:
            sum=sum+j
    if sum==num:
        print(num)
for i in range(1,1000):
    perfect(i)


#question-3



#question-4
