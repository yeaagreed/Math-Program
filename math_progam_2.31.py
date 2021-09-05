##
# math_teacher.py
# 18/08/2021
# SF

def student_menu():
    """Student Module"""
    print("""\n\n---------------Welcome to Who Wants to be a Mathionaire!---------------
Who Wants to be a Mathionaire will test your ability at maths
while rewarding you with money. Questions will progressively get harder,
increasing in age level until you get one wrong
As you get more questions correct, the reward will increase,
but if you get one wrong you lose your whole reward.
""")

    print("\n#####  Lets go, first question  #####")
    reward = 10
    answer = 0
    i = 0
    grade = 1
    while True:


        # Steps the grade up every 3 questions
        i += 1
        if i % 3 == 0:
            grade += 1

        answer, operation = question_generation(grade, i)
            
        # If the user got it correct
        if answer == True:
            print("Good job, you got it correct!!")

            # Adds random reward on
            reward *= random.uniform(1, 3)
            print("Your reward is now ${:.0f}".format(reward))

            # Checks if user still wants to play
            quit_YN = input("\nTo continue play press enter or N to quit: ").upper().strip()
            while quit_YN != "" and quit_YN != "N":
                quit_YN = input("Please press enter or N" +
                                "\nTo continue play press enter or N to quit: ").upper().strip()
            if quit_YN == "N":
                print("Congratulations you won {:.0f}$ in total\n".format(reward))
                break

        # If user did not get it correct
        else:
            print("Unlucky that is incorrect.\n" +
                  "You lost all your money\n\n")
            break

    return grade, operation

        
def question_generation(grade, i):
    """Generates questions"""

    # Only do all operators if above grade two
    if grade > 2:
        operations = ["/", "x", "+", "-"]
        operation = random.choice(operations)
        number_1, number_2 = number_picker(grade)
        
        # Checks if plus or minus operator
        answer = plus_or_minus(operation, number_1, number_2)

        if operation == "x":
            answer = number_1*number_2
        
        # Need to make sure division gives a int answer
        elif operation == "/":
            while True:
                if number_1%number_2 == 0:
                        answer = number_1/number_2
                        break
                else:
                    number_1, number_2 = number_picker(grade)

    # If not above grade two, only do plus or minus
    else:
        operations = ["+", "-"]
        operation = random.choice(operations)
        number_1, number_2 = number_picker(grade)

        # Checks if plus or minus operator
        answer = plus_or_minus(operation, number_1, number_2)
    
    while True:
        try:
            user_answer = int(input("\nWhat is {} {} {}: ".format(number_1, operation, number_2)))
            break
        except:
            print("Please enter an whole number")

    question_info[i] = [operation, number_1, number_2, answer, user_answer, grade]



    # Check if answer is correct
    if answer == user_answer:
        operation = False 
        return True, operation
    else: 
        return False, operation


def number_picker(grade):
    """Picks two random numbers"""

    number_1 = random.randint(0, grade * 10)
    number_2 = random.randint(1, grade * 10)
    
    return number_1, number_2


def plus_or_minus(operation, number_1, number_2):
    "Checks if plus or minus operator then executes the operator"
    if operation == "+":
        answer = number_1 + number_2
        return answer
    elif operation == "-":
        answer = number_1 - number_2
        return answer


def teacher_menu(grade, operation):
    """Reads the teachers options"""
    while True:
        print("""\n#####Teacher Description#####""")
        mode = input("Press G for grade summary, T for students weaknesses, S to see past questions and Q to quit: ").lower()
        if mode == "g":
            grade_summary(grade)
        elif mode == "t":
            weakness(operation)
        elif mode == "s":
            question_print()
        elif mode == "q":
            print("\nExiting to main menu\n")
            break

def grade_summary(grade):
    """Gives Teacher a grade summary"""

    if grade == None:
        print("Math program has not been run yet by a student")
        return

    print("\nYour student is working comfortably " +
          "at grade number {}.".format(grade-1) +
          "\nGrade {} is challenging for them".format(grade))
        

def weakness(operation):
    """Gives the students weak operator"""

    if operation == False:
        print("We have not identified a weak operator for your students")
        return
    
    print("\nYour students are struggling with {}".format(operation))


def question_print():
    """Prints the questions that have been"""

    for question in question_info:
        print("\nGrade: {}".format(question_info[question][5]) +
              "\nWhat is {} {} {}: ".format(question_info[question][1], question_info[question][0], question_info[question][2]) +
              "\nStudent Answer: {}".format(question_info[question][4]) +
              "\nCorrect answer: {}\n".format(question_info[question][3]))



def main_menu():
    grade = None
    operation = False
    while True:
        print("""Welcome to Who wants to be a mathionaire!!"
(P) to play
(T) for teacher menu
(Q) to quit""")
        mode = input("Please enter your option: ").lower()
        if mode == "p":
            grade, operation = student_menu()
        elif mode == "t":
            teacher_menu(grade, operation)
        elif mode == "q":
            print("Thank you for playing")
            break
        else:
            print("Please enter either P, T or Q")


if __name__ == "__main__":
    import random
    question_info = {}
    main_menu()
    
    
