import random
import time

from colorama import Fore, Style, init
init(autoreset=True)

def generate_tickets(num_count):
    print("Your Lottery Number is...")
    Save = []
    num_count = int(num_count)
    lotto = list(range(1,56))
    for i in range(int(num_count)):
        Save.append(random.sample(lotto,6))
        print(Fore.YELLOW + Style.BRIGHT)
        print(Save[i-0])
        print(Style.RESET_ALL)
    return(Save)
    
def draw_numbers():   
    LWSave = []
    lottow = list(range(1,56))
    print("Your Winning Lottery Number is...")
    print(Fore.YELLOW + Style.BRIGHT)
    LWSave = random.sample(lottow,6)
    w = random.sample(lottow, 6)
    print(w)
    print(Style.RESET_ALL)
    return(LWSave)

def search_winners(Save, LWSave):
    t = 0
    f = 0
    fv = 0
    winner = 0
    
    for i in Save:
        Bah = set(i).intersection(LWSave)
        if len(Bah) == 3:
            t = t + 1
        elif len(Bah) == 4:
            f = f + 1
        elif len(Bah) == 5:
            fv = fv + 1
        elif len(Bah) == 6:
            winner = winner + 1
            
    print('3 Numbers that matched: ', t)
    print('4 Numbers that matched: ', f)
    print('5 Numbers that matched: ', fv)
    print('Winner! Winner! Chicken Dinner!🍗: ', winner)
    return(Save, LWSave)

print("------------------------------------------------")
print(Fore.GREEN + Style.BRIGHT + "           Lottery Simulator 💰")
print(Style.RESET_ALL)
print(Fore.MAGENTA + Style.BRIGHT + "         Made by B. Allanigue")
print(Style.RESET_ALL)
print("------------------------------------------------")
time.sleep(1)

print("1. Generate the Ticket (🎟️)")
print("2. Draw Winning Numbers (🎰)")
print("3. Display the Tickets that won, if any.")
print("i.     3 matching digits")
print("ii.    4 matching digits")
print("iii.   5 matching digits")
print("iv.    6 matching digits (WINNER! 🎆)")
print(" ")
time.sleep(0.5)
print(Fore.RED + Style.BRIGHT + "5. Exit")
print(Style.RESET_ALL)

run = True
while run == True:

    #- User's input
    QM = input("❓ - What would you like to do? ")
    time.sleep(0.3)
    
    if QM == ("1"):
        num_count = int(input("Enter how many tickets you would like to generate. "))
        Save = generate_tickets(num_count)

        
    if QM == ("2"):
        LWSave = draw_numbers()
        #- Making a winning number
        
    if QM == ("3"):
        search_winners(Save, LWSave)
        
    if QM == ("4"):
        print("dont gamble!! 👋")
        run = False
