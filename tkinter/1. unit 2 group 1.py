import random
import time
import os

def main():
    global Life
    global Day
    print("Updating Module (78%)\nUpdating Module (100%)")
    print("Commencing program…\n")
    print("Full screen the program")
    input("(Press Enter to continue)")
    
    print("Welcome User428, this is the CIA’s secret"\
          "operation. Operation SKYFALL.")
    print("During 1898, we have replaced birds with drones,"\
          "and now in the past 5 years we have"\
          "been working on deleting the sky ")
    print("Lets see how loyal you are to our cause…")
    
    Day = night_not_real()
    Life = life(Day)

def night_not_real():
    global Sun
    global Moon
    while True:
        DayNight = input("Is it Day or Night"\
                         "real? (Enter \"day\" or \"night\")")
        if DayNight.lower() == "day":
            Sun = True
            Moon = False
            return True
        elif DayNight.lower() == "night":
            Sun = False
            Moon = True
            return False
        else:
            print("Incorrect input! Please"\
                  "enter either \'day\' or \'night\'.")

def life(Day):
    if Day:
        print("Put the 3 most common clouds in order from smallest"\
              "to largest: Stratocumulus, Cumulus, Cumulonimbus: ")
        ques_clouds1 = input("Enter Cloud One: ")
        ques_clouds2 = input("Enter Cloud Two: ")
        ques_clouds3 = input("Enter Cloud Three: ")

        if ques_clouds1.lower() == "Stratocumulus" and \
           ques_clouds2.lower() == "Cumulus" and \
           ques_clouds3.lower() == "Cumulonimbus":
            print("Correct, advance to the next round")
            return True
        else:
            print("Incorrect (Why did you not search online?)")
            return False
    else:
        ques_clouds = input("What is the thunder cloud Pokemon? ")
        if ques_clouds.lower() == "thundurus":
            print("Correct (you probably searched online)")
            return True
        else:
            print("Incorrect (Why did you not search online?)")
            return False

def ending():
    print("So I see you’ve come to the end of the program."\
          "To ensure you are a real person, please enter the"\
          "code given to you after you complete a question.")
    ran_eqn()
    if not(Life):
        print("YoU GOt tHe quEsTIOn RIgHt")
        input("But you got an earlier question wrong")
        input("Curtis told me to kill ur program")
        input("So ima do that now")
        os.system("taskkill /F /IM pythonw.exe /T")
    
    else:
        print("Correct! Your code is 80.932")
    code = float(input("Please now enter the code you received: "))
    if code == 80.932:
        true_ending()
    else:
        os.system("taskkill /F /IM pythonw.exe /T")

def true_ending(): 
    input("You will need to press enter after each line.")
    if Sun and not Moon:
        input("Welcome User428. To further understand"\
              "why the sky and the Moon are not real, we must go")
    else:
        input("Welcome User428. To further understand why"\
              "the sky and the Sun are not real, we must go")
    input("back to 2021 when COVID started. Truth be told,"\
          "COVID was a lie created")
    input("as a joint operation with China and America to remove the sky.")
    input("Now they have set their sights on revealing to"\
          "the world that we live in")
    input("the matrix. Your mission, should you choose to"\
          "accept, is to save the world.")
                    
    seconds = 5
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    
    os.system("taskkill /F /IM pythonw.exe /T")

def ran_eqn():   
    equations = [
        ("54 * 3", 54 * 3),
        ("847 / 11", 847 / 11),
        ("21 * 12", 21 * 12),
        ("5 * 10 + 35", 5 * 10 + 35),
        ("9898 / 98", 9898 / 98)
    ]
    
    equation, correct_answer = random.choice(equations)
    user_answer = float(input(f"What is the result of {equation}? "))
    
    if user_answer == correct_answer:
        pass
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")
        input("YOu ShAlL Die")
        os.system("taskkill /F /IM pythonw.exe /T")

# Call the ending function to start the program
main()
ending()
