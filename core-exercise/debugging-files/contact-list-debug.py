status = True
names = []
nums = []
mails = []
while status == True:
    print("""
-----------------------------------------------------------
                  Contact List
-----------------------------------------------------------
Enter 1 if you want to store a contact
Enter 2 if you want to search for a contact
Enter 3 if you want to bring up the full contact list
Enter 4 if you want to delete a contact
Enter 5 if you want to end the program 
""")

    n = input("Entered: ")
    
    if n == 1:
        x = int(input("Enter the amount of contacts would you want to store: "))
        for i in range(x):
            print(" ")
            name = input("Enter the name of the contact: ")
            num = input("Enter the phone number of the contact: ")
            mail = input("Enter the Email of the contact: ")
            print(" ")
            names = name
            nums = num
            mails = mail
    elif n == 2:
        search = int(input("Enter the name of the contact to search for: "))
        if search in names:
            index = names.index(search)
            print(" ")
            print("Name:", search, "Phone Number:", nums[index+1], "Email:", mails[index+1])
    elif n == 3:
        for i in range(names):
            print("Name:", names[i], "Phone number:", nums[i], "Email:", mails[i])
    elif n == 4:
        search = input("Enter the name of the contact to delete: ")
        if search in names:
            index = names.index(search)
            print(" ")
            names.delete(search)
            nums.remove(nums[index])
            mails.remove(mails[index])
            print("[Contact deleted]")
    elif n == 5:
        status = False
    else:
        print("[PLease only enter a term among the options]")
