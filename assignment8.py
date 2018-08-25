#ASSIGNMENT - CLASSES AND OBJECTS
#question-1
class circle:
    def __init__(self, r):
        self.radius = r
    def getArea(self):
        return(3.14*self.radius*self.radius)
    def getCircumference(self):
        return(2*3.14*self.radius)
r=int(input("enter radius"))
c=circle(r)
print("area is ",c.getArea())
print("circumference is ",c.getCircumference())


#question-2
class student:
    def __init__(self):
        self.name=(input("enter name"))
        self.roll=int(input("enter rollno"))
    def setAge(self):
        self.age=int(input("enter age"))
    def setMarks(self):
        self.marks=int(input("enter marks"))
    def display(self):
        print("name:",self.name,"\n","roll-no:",self.roll,"\n","age:",self.age,"\n","marks:",self.marks)
s=student()
s.setAge()
s.setMarks()
s.display()


#question-3
class temperature:
    def convertFahrenheit(self):
        self.c=int(input("enter temperature in celsius"))
        return((9/5)*self.c+32)
    def convertCelsius(self):
        self.f=int(input("enter temperature in Fahrenheit"))
        return(((self.f-32)*5)/9)
t=temperature()
print(t.convertFahrenheit())
print(t.convertCelsius())



#question-4
class MovieDetails:
    def __init__(self):
        self.artistname = input("enter artist name")
        self.year=input("enter year")
        self.rating=int(input("enter ratings out of 5"))
    def add(self):
        self.moviename=input("enter the movie name")
        self.collection=int(input("enter total collection"))
    def display(self):
        print(self.moviename)
        print(self.artistname)
        print(self.year)
        print(self.rating)
        print(self.collection)
m=MovieDetails()
m.add()
m.display()



#question-5



#question-6
'''output will be:
A B
A B'''


#question-7
