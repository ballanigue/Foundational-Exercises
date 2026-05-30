print("-----------------")
print("Final Grade Maker📝")
print("-----------------")

QPT = input("Enter how many PT you have | MAX OF 2: ")

if QPT == ("1"):
    PT1_score = input("Enter your Score for PT1: ")
    PT1_total = input("Enter Total Score for PT1: ")
    PT_Total_P = (int(PT1_score)) / (int(PT1_total)) * 35.0
elif QPT == ("2"):
    PT1_score = input("Enter your Score for PT1: ")
    PT1_total = input("Enter Total Score for PT1: ")
    PT2_score = input("Enter your Score for PT2: ")
    PT2_total = input("Enter Total Score for PT2: ")
    PT_Total_P = (int(PT1_score + PT2_score)) / (int(PT1_total + PT2_total)) * 35.0
    
QT = input("Enter how many Test you have | MAX OF 2: ")

if QT == ("1"):
    T1_score = input("Enter your Score for Test1:: ")
    T1_total = input("Enter  Total score for Test1: ")
    Test_Total_P = (int(T1_score)) / (int(T1_total)) * 30.0
elif QPT == ("2"):
    T1_score = input("Enter your Score for Test1: ")
    T1_total = input("Enter Total Score for Test1: ")
    T2_score = input("Enter your Score for Test2: ")
    T2_total = input("Enter Total Score for Test1: ") 
    Test_Total_P = (int(T1_score + T2_score)) / (int(T1_total + T2_total)) * 30.0
    
QS = input("Enter how many Seatworks you have | MAX OF 2: ")

if QS == ("1"):
    S1_score = input("Enter your Grade for SW1:: ")
    S1_total = input("Enter Total Score for SW1: ") 
    SW_Total_P = (int(S1_score)) / (int(S1_total)) * 15.0
elif QS == ("2"):
    S1_score = input("Enter your Grade for SW1: ")
    S1_total = input("Enter Total Score for SW1: ") 
    S2_score = input("Enter your Grade for SW2: ")
    S2_total = input("Enter Total Score for SW2: ") 
    SW_Total_P = (int(S1_score + S2_score)) / (int(S1_total + S2_total)) * 15.0

RS = input("Enter your Recitation score: ")
RST = input("Enter max total Recitations: ")
RS_P = (int(RS)) / (int(RST)) * 20

Total = PT_Total_P + Test_Total_P + SW_Total_P + RS_P

SW_Total_P = 15
PT_Total_P = 35
Test_Total_P = 30
RS_P = 20

Numerical_grade = (Total*0.8333) + 16.67
Numerical_grade_F = str(round(Numerical_grade, 2))

print("-------------------------")

numgrade = float(Numerical_grade_F)
if numgrade >= 96.50 and numgrade <= 100.00:
    print("Your letter grade is A+")
elif numgrade >= 93.50 and numgrade <= 96.49:
    print("Your letter grade is A")
elif numgrade >= 89.50 and numgrade <= 93.49:
    print("Your letter grade is A-")
elif numgrade >= 86.50 and numgrade <= 89.49:
    print("Your letter grade is B+")
elif numgrade >= 83.50 and numgrade <= 86.49:
    print("Your letter grade is B")
elif numgrade >= 79.50 and numgrade <= 83.49:
    print("Your letter grade is B-")
elif numgrade >= 77.50 and numgrade <= 79.49:
    print("Your letter grade is C+")
elif numgrade >= 75.50 and numgrade <= 79.49:
    print("Your letter grade is C")
elif numgrade >= 74.50 and numgrade <= 75.49:
    print("Your letter grade is C-")
elif numgrade >= 70.00 and numgrade <= 74.49:
    print("Your letter grade is D")
elif numgrade >= 0.00 and numgrade <= 74.49:
    print("Your letter grade is F-")
elif numgrade > 100.00:
    print("That's crazy")
    print("Enter a range number to 100.00 - 0.00")

print(Numerical_grade_F)
