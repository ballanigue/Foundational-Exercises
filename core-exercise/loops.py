import time
run = True

while run == True:
    print("-----------------------------")
    print(" SW 3 | ALLANIGUE G11 - RUIZ ")
    print("-----------------------------")
    print("                             ")
    print("Running the code...🤖")
    time.sleep(1.5)
    print("1. Reverse your numbers")
    time.sleep(0.5)
    print("2. Descend your numbers")
    time.sleep(1)
    qs = input("Type a number you would like to run! ")
    if qs == '1':
        print(input("Enter any number(s) and I shall Reverse it!🪄✨ ")[::-1])
        
    elif qs =='2':
        print("Type your number(s) and I shall Descend it!🥷💨 ")
        print(*range(1,int(input())+1)[::-1],sep=' ')
    time.sleep(1)
    print("              ")
    q = input("Run it again❓ y/n ")
    
    if q == 'n':
        print("Owkey, bye bye!")
        run = False
    elif q == 'y':
        run = True
        print("Okie Dokie!")
    else:
        print("Please type n and y only.")
