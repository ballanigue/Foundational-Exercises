N = int(input("Enter any number: "))
 
# iterate using a for loop till the
# given range
for i in range(1, N+1):

    # if no. is multiple of 4 and 5
    # print fizzbuzz
    if i % 5 == 0:
        print("buzz")
        
        # continue with the loop
        continue
 
    else:
        # else just print the no.
        print(i)
