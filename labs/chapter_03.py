# Quiz Program
print("Time for your math quiz! How many can you get right? For mutiple choice answers, input the letter ONLY.")

numOfCorrect = 0

def correct_answer():
    global numOfCorrect
    numOfCorrect += 1

def questions(question, correctAnswer, numOfCorrect, multipleChoice, choices):
    print()
    print(question)

    if multipleChoice:
        print(choices)
    
    userInput = input()
    
    if userInput.lower() == correctAnswer:
        print("Correct!")
        correct_answer()
    else:
        print(f"Wrong! The correct answer is {correctAnswer}")
    return numOfCorrect


# Question 1: written answer
question = "What is the name of a three-sided polygon?"
correctAnswer = "triangle"
ismultipleChoice = False
choices = "None"
questions(question, correctAnswer, numOfCorrect, ismultipleChoice, choices)

# Question 2, multiple question
question = "If a right angle triangle has sides 5 and 12, what is the length of the hypotnuse?"
correctAnswer = "b"
ismultipleChoice = True
choices = """
a) 5
b) 13
c) 21
d) hotdog"""
questions(question, correctAnswer, numOfCorrect, ismultipleChoice, choices)

# Question 3: multiple choice
question = "The average of two positive integers m and n is 5. What is the largest possible value of n?"
correctAnswer = "c"
choices = """
a) 25
b) 4
c) 9
d) 5"""
questions(question, correctAnswer, numOfCorrect, ismultipleChoice, choices)

# Question 4: number input
question = "A right-angled triangle with integer side lengths has one side with length 605. This side is neither the shortest side nor the longest side of the triangle. What is the maximum possible length of the shortest side of this triangle?"
correctAnswer = "528"
ismultipleChoice = False
choices = "none"
questions(question, correctAnswer, numOfCorrect, ismultipleChoice, choices)

# Question 5: number input
print("This one's easy, you should be able to get it")
print()
question = " Let  n  be a positive integer. Consider the set  S  of points  (x,y,z)  with  x,y,z∈{0,1,…,n}  and  x+y+z>0 , so  S  is a set of  (n+1)3−1  points in three-dimensional space. Determine the smallest possible number of planes, the union of which contains  S  but does not include  (0,0,0) ."
correctAnswer = "3n"
choices = "none"
questions(question, correctAnswer, numOfCorrect, ismultipleChoice, choices)

print("your score is " + str(numOfCorrect/5 * 100) + "percent, or " + f"{numOfCorrect} out of 5!")
