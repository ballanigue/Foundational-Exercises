# ask user for any number
N = int(input("Enter any number: "))

# set up a variable to store the sum
# with initial value of 0
s = 0

# since we want to include the given number in the sum
# increment given number by 1 in the for loop
for i in range(1, N + 1):
    s = s + 1
    
# print the total sum at the end
print(sum(range(N + 1)))
