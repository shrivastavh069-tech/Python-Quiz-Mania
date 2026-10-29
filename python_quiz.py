import random
import time


"""theory quesation check"""
def theory_check (j,Answer):
    if 1== j:
        if Answer =="B":
            return("Correct Answer !")
        else:
            return("Incrrect Answer !")
    elif 2 == j :
        if Answer =="B":
           return("Correct Answer !")
        else: 
            return("Incorrect Answer !")      
    elif 3 == j:
        if Answer =="C":
            return("Correct Answer !")
        else:
            return("Incorrect Answer !")    
    elif 4 ==  j:
       if Answer =="C":
            return("Correct Answer !")
       else:             
            return("Incorrect Answer !")
    elif 5 == j:
        if Answer =="B":
           return("Correct Answer !")
        else:    
            return("Incorrect Answer !")
    elif 6== j:
        if Answer =="C":
            return("Correct Answer !")
        else:
            return("Incorrect Answer !")
    elif 7 == j:
        if Answer =="B":
            return("Correct Answer !")
        else:    
           return("Incorrect Answer !")
    elif 8 == j:
        if Answer =="B":
            return("Correct Answer !")
        else:
            return("Incorrect Answer !")
    elif 9 == j: 
        if Answer =="A":
            return("Correct Answer !")
        else:
            return("Incorrect Answer !")
    elif 10==j:
        if Answer =="C":
           return("Correct Answer !")
        else:
            return("Incorrect Answer !")
          

""" Coding check"""
def coding_check (j,Answer):
    if 1== j:
        if Answer =="C":
            return("Correct Answer !")
        else:
            return("Incrrect Answer !")      
    elif 2 == j :
        if Answer =="B":
           return("Correct Answer !")
        else:
           return("Incorrect Answer !")      
    elif 3 == j:
        if Answer =="C":
            return("Correct Answer !")
        else:
            return("Incorrect Answer !")    
    elif 4 ==  j:
       if Answer =="C":
            return("Correct Answer !")
       else:             
            return("Incorrect Answer !")
    elif 5 == j:
        if Answer =="C": 
            return("Correct Answer !")
        else:    
            return("Incorrect Answer !")
    elif 6== j:
        if Answer =="A":
            return("Correct Answer !")
        else:
           return("Incorrect Answer !")
    elif 7 == j:
        if Answer =="C":
           return("Correct Answer !")
        else:    
           return("Incorrect Answer !")
    elif 8 == j:
        if Answer =="C":
            return("Correct Answer !")
        else:
            return("Incorrect Answer !")
    elif 9 == j: 
        if Answer =="B":
            return("Correct Answer !")
        else:
           return("Incorrect Answer !")
    elif 10==j:
        if Answer =="A":
            return("Correct Answer !")
        else:
            return("Incorrect Answer !")
   

"""Coding questions"""       
coding={
    1:
    """data = {
    "a": 10,
    "b": 20,
    "c": 30

}
total = 0

for key in data:
    if data[key] > 15:
        total += data[key]

print(total)
A) 30
B) 40
C) 50
D) 60
""",
    2:
    """nums = [1, 2, 3, 4, 5]

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        nums[i] *= 2

print(nums)
A) [1, 2, 3, 4, 5]
B) [1, 4, 3, 8, 5]
C) [2, 2, 6, 4, 10]
D) [1, 4, 6, 8, 10]
""",
    3:
    """students = {
    101: {"name": "A", "marks": 80},
    102: {"name": "B", "marks": 90},
    103: {"name": "C", "marks": 70}
}

x = students[102]["marks"]

print(x)
A) 102
B) "B"
C) 90
D) {"name": "B", "marks": 90}
""",
    4:
    """def test(a, b=5):
    return a * b

x = test(3)
y = test(3, 2)

print(x + y)
A) 11
B) 15
C) 21
D) 30
""",
    5:
    """a = [1, 2, 3]
b = a

b.append(4)

print(a)
A) [1, 2, 3]
B) [4]
C) [1, 2, 3, 4]
D) Error
""",
    6:
    """total = 0

for i in range(1, 6):
    if i == 4:
        break
    total += i

print(total)
A) 6

B) 10

C) 15

D) 4
""",
    7:
    """nums = [1, 2, 1, 3, 2, 1]

count = {}

for n in nums:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

print(count[1])
A) 1

B) 2

C) 3

D) 6
""",
    8:
    """x = 0

for i in range(3):
    for j in range(2):
        x += 1

print(x)
A) 3

B) 5

C) 6

D) 9
""",
    9:
    """def test(n):
    if n > 5:
        return n * 2
    return n + 2

print(test(5))
A) 3
B) 5
C) 7
D) 10
""",
    10:
    """nums = [2, 4, 6, 8]

for i in range(len(nums) - 1):
    nums[i] = nums[i] + nums[i + 1]

print(nums)
A) [6, 10, 14, 8]
B) [6, 10, 14, 16]
C) [2, 6, 10, 14]
D) [4, 8, 12, 16]
""",
 }             
           
"""Theory questions """      
theory={
    1:"Which symbol is used to create a list in Python?\n\n\nA) {1, 2, 3}\nB) [1, 2, 3]\nC) (1, 2, 3)\nD) <1, 2, 3>",
    2:"""What is the output of len("Python")?\nA) 5\nB) 6\nC) 7\nD) Error""",
    3:"""Which of the following is a dictionary?\nA) [1, 2, 3]\nB) (1, 2, 3)\nC) {"name": "Alex", "age": 20}\nD) {1, 2, 3}""",
    4:"What is the value of x after this code?\nx = 10\nx += 5\nA) 5\nB) 10\nC) 15\nD) 105",
    5:"What will be the output?\na = [10, 20, 30]\nprint(a[1])\nA) 10\nB) 20\nC) 30\nD) Error",
    6:"Which keyword is used to define a function?\nA) function\nB) define\nC) def\nD) fun",
    7:"What is the output?\nprint(10 // 3)\nA) 3.33\nB) 3\nC) 4\nD) 1",
    8:"Which loop is commonly used to iterate through a sequence?\nA) if\nB) for\nC) def\nD) class",
    9:"""What is the output?\nx = "Python"\nprint(x[0])\nA) P\nB) y\nC) Python\nD) Error""",
    10:"What does None represent in Python?\nA) Zero\nB) Empty string\nC) No value / absence of a value\nD) False only",
     }

question=list(theory.keys())
random.shuffle(question)


"""Without timer theory questions """
def theoryques():
    i=1
    win=0
    for j in question:
        print("Question",i,":",end="")
        print(theory[j])
        Answer=input("Your Answer:")
        Answer=Answer.upper()
        result=theory_check(j,Answer)
        if result =="Correct Answer !":
            print("Correct Answer !")
            win+=10
        else:
            print("Incorrect Answer !")
            win-=10        
        i+=1
        print("points:",win)
        print("=================================")
    print("+========================+")
    print("|     Score Board        |")
    print("|Congratulations ",name," |")
    print("|     points:",win,"       |")
    print("+========================+")
            

"""Coding questions with not Timer"""
def codingques():
    i=1
    win=0
    for j in coding:
        print("Question",i,":",end="")
        print(coding[j])
        Answer=input("Your Answer:")
        Answer=Answer.upper()
        result=coding_check(j,Answer)
        if result =="Correct Answer !":
            print("Correct Answer !")
            win+=10
        else:
            print("Incorrect Answer !")
            win-=10        
        i+=1
        print("points:",win)
        print("=================================")

    print("+===============+")
    print("|  Score Board  |")
    print("|points:",win," |")
    print(f"{name} Wins !!!|")
    print("+===============+")

      
        
print("========================================")
print("|             Welcome To               |")
print("|        Torjis PYTHON  QUIZ           |")
print("========================================")
#time.sleep(1.2)
print("+---------------------+")
print("|Registration for quiz|")
print("+---------------------+")
time.sleep(1)
name=input("Please enter the name of candidate:")
print("🗄️")
print("Connecting to server....")
time.sleep(0.80)
print("📚")
print("Collecting Questions...")
time.sleep(1)
print("🪪")
print("Refreshing score card ")
time.sleep(1)
print("Preparing Menu")
        
while True:
    print("\n+-----------MENU------------+")
    print("1.Set Your level        [Type-1]")
    print("2.How To Play               [Type-2]")
    print("3.Exit                      [Type-3]")
    select=int(input("You want to enter in:"))
    if select == 1:
        print("+------------Set Your Level------------+")
        print("1.Theory Questions        [Type-1]")
        print("2.Coding Questions        [Type-2]")
        times=int(input("You Select:"))
        print("+------------------------------------------+")
        if times == 1:
            theoryques()
            
               
        if times == 2:
            
            codingques()
            
                
    elif select == 2:
        print("""
1.Set Your Level:-
------------------------------------------------------------------------------------------------------------------
    [1.1] Theory Quesations:-
        ->This section has theory quesations
        ->In Type of MCQs
        ->There are 10 quesations
    [1.2] Coding quesations:-
        ->This section has coding quesations
        ->Type:MCQs
        ->level:EASY To HARD
        ->There are 10 quesations 
        
2.Exit   
-----------------------------------------------------------------------------------------------------------------     
        ->To exit the application
""")        
    else:
        print("THANK YOU")
        break
if __name__=="main":
    print("python Quiz")
