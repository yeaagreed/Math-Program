##
# math_teacher.py
# 18/08/2021
# SF


def student_menu():
    """Student Module"""
    print("""\nKia Ora, Welcome to Who wants to be a Mathionaire!\n
 - The game will give you maths question that slowly get harder.
 - If you get the question correct your money will increase by a random amount!
 - BE AWARE if you get a question wrong you will lose all your money!
 - Quit at any time to bank your money

Your scores, grade and questions will be shared with the teacher.

Purei me te ngahau! – Play hard and have fun!""")

    print("\n#####  Lets go, first question  #####")

    # Declaring variables
    reward = 10
    answer = 0
    i = 0
    grade = 1

    # Continues looping until user indicates
    while True:

        # Steps the grade up every 3 questions
        i += 1
        if i % 3 == 0:
            grade += 1

        # Gives the user a question and returns if the got it correct.
        answer, operation = question_generation(grade, i)

        # If the user got it correct
        if answer is True:
            print("Good job, you got it correct!!")

            # Adds random reward on
            reward *= random.uniform(1, 3)
            print("Your reward is now ${:.0f}".format(reward))

            # Checks if user still wants to play
            quit_YN = input("\nTo continue play press enter " +
                            "or N to quit: ").upper().strip()
            while quit_YN != "" and quit_YN != "N":
                quit_YN = input("Please press enter or N" +
                                "\nTo continue play press enter or N to quit: "
                                ).upper().strip()
            if quit_YN == "N":
                print("Congratulations you won" +
                      "{:.0f}$ in total\n".format(reward))
                break

        # If user did not get it correct
        else:
            print("Unlucky that is incorrect.\n" +
                  "You lost all your money\n\n")
            break

    # Returns the grade the operation for the teacher info menu
    return grade, operation

        
def question_generation(grade, i):
    """Generates questions"""

    # Only do all operators if above grade two
    if grade > 2:
        operations = ["/", "x", "+", "-"]
        operation = random.choice(operations)

        # Picks two random numbers
        number_1, number_2 = number_picker(grade)

        # Checks if plus or minus operator
        print(operation, number_1, number_2, grade)

        # Will return an error if not + or - so the try except to ignore that
        try:
            answer, number_1, number_2 = plus_or_minus(operation, number_1, number_2, grade)

        except:
            if operation == "x":
                answer = number_1*number_2

            # Need to make sure division gives a int answer
            elif operation == "/":
                while True:
                    if number_1 % number_2 == 0:
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
        answer, number_1, number_2 = plus_or_minus(operation, number_1, 
                                                   number_2, grade)

    # Forces the user to give an integer answer
    while True:
        try:
            user_answer = int(input("\nWhat is {} {} {}: ".format(number_1,
                                                                  operation,
                                                                  number_2)))
            break
        except:
            print("Please enter an whole number")

    # Add thes question info in for the teacher to see
    question_info[i] = [operation, number_1, number_2, answer,
                        user_answer, grade]

    # Check if answer is correct
    if answer == user_answer:
        operation = False
        return True, operation
    else:
        return False, operation


def number_picker(grade):
    """Picks two random numbers depending on the grade"""

    number_1 = random.randint(0, grade * 10)
    number_2 = random.randint(1, grade * 10)

    return number_1, number_2


def plus_or_minus(operation, number_1, number_2, grade):
    "Checks if plus or minus operator then executes the operator"

    if operation == "+":
        answer = number_1 + number_2

        return answer, number_1, number_2

    # Makes sure the subtraction is positive answer
    elif operation == "-":
        while True:
            number_1, number_2 = number_picker(grade)
            answer = number_1 - number_2
            if answer >= 0:
                return answer, number_1, number_2


def teacher_menu(grade, operation):
    """Reads the teachers options"""
    while True:
        
        print("""\n#### Teacher Menu ####\n
(G) for grade summary
(T) for students weaknesses
(S) to see questions and answers of last student
(Q) to quit""")
        mode = input("Please enter your option: ").lower()
        if mode == "g":
            grade_summary(grade)
        elif mode == "t":
            weakness(operation)
        elif mode == "s":
            question_print()
        elif mode == "q":
            print("\nExiting to main menu\n")
            break
        else:
            print("\nPlease enter a valid option")


def grade_summary(grade):
    """Gives Teacher a grade summary"""

    if grade is None:
        print("\nMath program has not been run yet by a student")
        return

    print("\nYour student is working comfortably " +
          "at grade {}.".format(grade-1) +
          "\nGrade {} is challenging for them".format(grade))


def weakness(operation):
    """Gives the students weak operator"""

    if operation is False:
        print("\nWe have not identified a weak operator for your students")
        return

    print("\nYour students are struggling with {}".format(operation))


def question_print():
    """Prints the questions that have been"""

    for question in question_info:
        print("\nGrade: {}".format(question_info[question][5]) +
              "\nWhat is {} {} {}: ".format(question_info[question][1],
                                            question_info[question][0],
                                            question_info[question][2]) +
              "\nStudent Answer: {}".format(question_info[question][4]) +
              "\nCorrect answer: {}\n".format(question_info[question][3]))


def main_menu():
    """Presents the user with the options"""
    grade = None
    first_time_checker = True
    operation = False
    while True:
        print("""Welcome to Who wants to be a Mathionaire!!
(P) to play
(T) for teacher menu
(Q) to quit""")
        mode = input("Please enter your option: ").lower()
        if mode == "p":
            grade, operation = student_menu()
        elif mode == "t":
            # Only want the teacher description to print once
            if first_time_checker is True:
                print("""\n#### Kia Ora Teacher ####\n
Want your students to have a fun maths with addition, subtraction,
multiplication, or division?

You have come to the right place. The game will present your students with
graded questions and you as the teacher will be able to see the results. We
offer informationon how the student is doing including a summary of the grade
they are working at, what the student is struggling with, and a recap of the
questions answered by the student.

I hope you find the program useful and effective!""")
                first_time_checker = False
            
            teacher_menu(grade, operation)
        elif mode == "q":
            print("Thank you for playing")
            break
        else:
            print("Please enter either P, T or Q\n")


if __name__ == "__main__":
    import random
    question_info = {}
    main_menu()
