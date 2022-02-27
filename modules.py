import string
import random
def random_user_id():
    chars=string.ascii_lowercase + string.digits
    size_input = int(input('size of size:'))
    print_amount = int(input('print amount:'))
    for i in range (print_amount):
        print(''.join(random.choice(chars) for _ in range(size_input)))
print(random_user_id()) 

#task 2
import string
import random
def random_user_id(size=6, chars=string.ascii_lowercase + string.digits):
        return''.join(random.choice(chars) for _ in range(size))
print(random_user_id())  

#task3
import random
def rgb_color_gen():
    size = random.sample(range(0, 255), 3)
    return size

print(rgb_color_gen())  

#task3
import random
def shuffled_list ():
    mylist = ['mango', 'banana', 'orange', 'apple']
    random.shuffle(mylist)
    return mylist
print(shuffled_list())