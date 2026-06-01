run = True

while run == True:

    i = 1
    num = int(input("Calculate factorial of: "))
    product = 1
    
    while i <= num:
        product = product * i
        i = i + 1
    
    print("The factorial is", product)

    
    q = input("Calculate again? y/n ")
    
    if q == 'n':
        run = False
    elif q == 'y':
        run = True
        print("Okie Dokie!")
    else:
        print("Please type n and y only.")
