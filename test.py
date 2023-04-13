import random

class Question:

    def question1():
        q1 = "1. What is your name?"
        getName = str(input("Name: ")).title()
        print(f"My name is {getName}, I am glad be here with you guys")
        
    def question2():
        q2 = "What is your age?"
        age = int(input("Enter youur age"))
        print(f"You are {age} years old")

    def question3():
        q3 = "3. How many years of coding experience do you have?"
        getExp = int(input("Years of Experience: "))
        print(f"I have {getExp} years of experience in coding")


def solve():
    solution = input("Enter the answere Here: ")
    Question.question1()
    if(solution == "Adewale"):
        Question.question2()
    else:
        print("Wrong answer")
        Question.question3()

#solve()

fruits = ["mango", "orange", "pineapple", "lemon"]
owner = ["Qodri", "Zainab", "Adewale", "Ramot"]
for fruit in fruits:
    print(fruit)
print("#" * 15)
for x in range(len(fruits)):
    print(fruits[x])

owner.extend(fruits)
print(fruits)
print("\n\n")
print(owner)
print("#" * 50)
other = ['Jamiu', "Jambaba", 'Yusuf', 'Adeshola']
names = other.extend(owner)
jamiuFamily = []
print(names)
for name in other:
    if "a" in name:
        jamiuFamily.append(name)
        print(jamiuFamily)
    else:
        print(names)
tram = ('yam', 'locust')
print(type(tram))
print(tram)
barn = tuple(('fowl', 'griddle', 'mantle'))
print(type(barn))
print(barn)