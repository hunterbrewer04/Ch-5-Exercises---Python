

import random

def conversion():
    kmtomiles = int(input("Please input the amount of kilometers: "))
    miles = kmtomiles * .6214
    format_miles = "{:.2f}".format(miles)
    print(kmtomiles, "Kilometers is", format_miles, "Miles.")

def insurance():
  value = int(input("How much is the replacement of your property? "))
  insuredvalue = value * .8
  format_insuredvalue = "{:.2f}".format(insuredvalue)
  print("You should insure up to $", format_insuredvalue )

def costs():
  loan = int(input("How much is your loan payment per month? "))
  insurance = int(input("How much is your insurance per month? "))
  gas = int(input("How much is your gas this month? "))
  oil = int(input("How much did you spend on oil this month? "))
  tires = int(input("How much did you spend on tires this month? "))
  maintenance = int(input("How much did you spend on maintenance this month? "))

  yearloan = loan * 12
  yearinsurance = insurance * 12
  yeargas = gas * 12
  yearoil = oil * 12
  yeartires = tires * 12
  yearmaintenance = maintenance * 12

  print("\nMonthly Payments", "\t", "Yearly Total")
  print("$",loan, "\t","\t","\t","\t","$", yearloan)
  print("$",insurance, "\t","\t","\t","\t","$", yearinsurance)
  print("$",gas, "\t","\t","\t","\t","$", yeargas)
  print("$",oil, "\t","\t","\t","\t","$", yearoil)
  print("$",tires, "\t","\t","\t","\t","$", yeartires)
  print("$",maintenance, "\t","\t","\t","\t","$", yearmaintenance)
  
  yearlytotal = yearloan + yearinsurance + yeargas + yearoil + yeartires + yearmaintenance
  print("\nYearly Total: $", yearlytotal )
  
def calories():
  carbgrams = int(input("How many grams of carbohydrates do you consume a day? "))
  fatgrams = int(input("\nHow many grams of fats do you consume a day? "))

  calsfromcarbs = carbgrams * 4
  calsfromfats = fatgrams * 9
  
  print("\nYou gain", calsfromcarbs, "calories from carbohydrates, and", calsfromfats, "calories from fats.\n")

def seats():
  costclassa = 20
  costclassb = 15
  costclassc = 10

  classa = int(input("\nHow many class A tickets were sold? "))
  classb = int(input("\nHow many class B tickets were sold? "))
  classc = int(input("\nHow many class C tickets were sold? "))

  totalticketsa = classa * costclassa
  totalticketsb = classb * costclassb
  totalticketsc = classc * costclassc

  totaltickets = totalticketsa + totalticketsb + totalticketsc

  print("\nThere was $", totaltickets, "made.\n")


def feet_to_inches():
  feet = 12 
  askfeet = int(input("How many feet? "))
  inches = feet * askfeet
  print("\nThere are", inches, "inches in", askfeet, "feet")


# def mathquiz():
  
randomnumber1 = random.randint(1, 250)
randomnumber2 = random.randint(1, 250)


def askquestions():
    global randomnumber1
    global randomnumber2

    useranswer = int(input("What is " + str(randomnumber1) + "+" + str(randomnumber2) + ": "))
    return useranswer


def checkanswer(useranswer):
    global randomnumber1
    global randomnumber2

    correctanswer = randomnumber1 + randomnumber2
    print()
    if useranswer == correctanswer:
      print("Congratulations!")
    else:
      print("Its wrong, the correct answer is", correctanswer)


def mathquiz():
    useranswer = askquestions()
    checkanswer(useranswer)                 


def test():
    test_scores = collect_scores()
    print()
    show_grades(test_scores)
    print()
    print('Test Average:', calc_average(test_scores))


def collect_scores():
    number_of_tests = 5

    scores = [0] * number_of_tests

    for index in range(len(scores)):
        test_score = int(input('Enter score for test #' + str(index + 1) + ': '))
        scores[index] = verify_test_score(test_score)
    return scores


def calc_average(grade_list):
    grade_total = 0

    for grade in grade_list:
        grade_total += grade

    return grade_total / len(grade_list)


def show_grades(grade_list):
    print('TEST GRADES')
    print('-----------')
    for index in range(len(grade_list)):
        print('Test #', index + 1, ': ', determine_grade(grade_list[index]), sep='')


def determine_grade(score):
    if score < 60:
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    else:
        return 'A'


def verify_test_score(score):
    while score < 0 or score > 100:
        print('Invalid test score. Please enter score between 0 and 100.')
        score = int(input('Enter new score: '))

    return score



 


    







print("\nWelcome to Chapter 5, Functions. What problem would you like to see?")


choice = ''


print("\n[1] Enter 1 for Kilometer to Mile conversion.")
print("[2] Enter 2 for How much Insurance?")
print("[3] Enter 3 for Automobile Cost")
print("[4] Enter 4 for Calories for fats and carbohydrates.")
print("[5] Enter 5 for Stadium Tickets")
print("[6] Enter 6 for Feet to Inches")
print("[7] Enter 7 for Math Quiz")
print("[8] Enter 8 for Test Scores")
print("[q] Enter q to quit.")


choice = input("\nWhat would you like to do? ")


if choice == '1':
    print("\nKilometer to Miles Conversion\n")
    conversion()
elif choice == '2':
    print("\nHow Much Insurance?\n")
    insurance()
elif choice == '3':
    print("\nAutomobile Cost\n")
    costs()
elif choice == '4':
    print("\nCalories from Fat and Carbohydrates\n")
    calories()
elif choice == '5':
    print("\nStadium Seats\n")
    seats()
elif choice == '6':
    print("\nFeet to inches\n")
    feet_to_inches()
elif choice == '7':
    print("\nMath Quiz\n")
    mathquiz()
elif choice == '8':
    print("\nTest Scores\n")
    test()
elif choice == 'q':
    print("\nThanks for playing. See you later.\n")
else:
    print("\nI don't understand that choice, please try again.\n")
        

print("Thanks again, bye now.")
