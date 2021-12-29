user =int(input("enter your age:"))
age_before_drive = 18 - user  
print(age_before_drive)      
if user > 18:
    print('you are old enough to drive')
else:
    print(f'wait for {age_before_drive} years  to lean to drive')


me = int(input("enter your age:"))  
you = 30 
total_age = 30 - me 
if me == you:
    print("we are of same age") 
else:
    print(f"you are {total_age} older than me") 


a = int(input('enter number one:')) 
b = int(input('enter number two:')) 
if a > b: 
    print(f'{a} is grater than {b} ') 
else:
    print(f'{a} is lesser then {b}') 

    score = int(input('enter student score:'))
if score in range(80, 101):
    print('You got a grade of A ') 
elif score in range(70, 80): 
    print('You got a grade of B ')
elif score in range(60, 70):
    print('You got a grade of C') 
elif score in range(50, 60):
    print('You got a grade of D')         
else:
    print('You got a grade of F')