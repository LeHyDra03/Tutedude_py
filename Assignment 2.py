#Assignment 2

#Task 1
a=int(input('Enter a number: '))

if a%2==0:
    print(a,'is an even number')
else:
    print(a,'is an odd number')



#Task 2
x= 0
for i in range(1, 51):
    x += i
print("The sum of numbers from 1 to 50 is:", x)
