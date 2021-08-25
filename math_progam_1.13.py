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

    i = 0
    grade = 1
    while True:


        # Steps the grade up every 3 questions
        i += 1
        if i == 3:
            grade += 1
            i = 0

        # If the user got it correct
        if question_generation(grade) == True:
            print("Good job, you got it correct!!")
            reward *= random.uniform(1, 3)
            print("Your reward has increased to ${:.0f}".format(reward))
            quit_YN = input("\nTo continue play press enter: ").upper().strip()
            if quit_YN != "":
                print("Congratulations you won {:.0f}$ in total".format(reward))
                break

        # If user did not get it correct
        else:
            print("Unlucky that is incorrect.\n" +
                  "You lost all your money")
            break

        
def question_generation(grade):
    """Generates questions"""
    
    operations = ["/", "x", "+", "-"]
    operation = operations[random.randint(0, 3)]
    number_1 = random.randint(0, grade * 10)
    number_2 = random.randint(0, grade * 10)
    if operation == "x":
        answer = number_1*number_2
    elif operation == "+":
        answer = number_1+number_2
    elif operation == "-":
        answer = number_1 - number_2


    # Need to make sure division gives a int answer
    elif operation == "/":
        while True:
            try:
                if number_1%number_2 == 0:
                    answer = number_1/number_2
                    break
                else:
                    number_1 = random.randint(0, grade * 10)
                    number_2 = random.randint(0, grade * 10)
            except:
                number_1 = random.randint(0, grade * 10)
                number_2 = random.randint(0, grade * 10)
                
    while True:
            user_answer = input("\nYour next question is {} {} {} = ?\nIf you do not want to attempt the question enter N, otherwise type your answer:  ".format(number_1, operation, number_2))
            print("Congratulations you won 10$ in total")
            break

    # Check if answer is correct
    if answer == user_answer:
        return True
    else:
        return False    


if __name__ == "__main__":
    import random
    while True:
        mode = input("Press P to play, T for teacher menu or Q to quit: ").lower()
        if mode == "p":
            student_menu()
        elif mode == "t":
            pass
        elif mode == "q":
            print("Thank you for playing")
            break
        else:
            print("Please enter either P, T or Q")
