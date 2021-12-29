# day 6 of 30 days  of python 

brothers = ('mayowa', 'dayo', 'ope', 'dele') 
sisters = ('peace', 'grace', 'debby') 
brothers_and_sisters = brothers + sisters 
print(brothers_and_sisters) 
print(len(brothers_and_sisters)) 
ma, da, fr, bu, de, pe, *rest = brothers_and_sisters 
print(ma) 
print(da) 
print(fr)
print(bu)
print(de) 
print(pe) 
print(rest) 


fruits = ('banana', 'orange', 'mango', 'lemon') 
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot') 
animal_products = ('milk', 'flour', 'butter') 
food_stuff_tp = fruits + vegetables + animal_products 
print(food_stuff_tp) 
food_stuff_it  = fruits + vegetables + animal_products 
print(food_stuff_it) 
food_suff = food_stuff_it[5:6]  
print(food_suff) 
food_suff = food_stuff_it[0:3] 
print(food_suff) 
food_suff = food_stuff_it[9:12] 
print(food_suff) 
del food_stuff_tp 
print(food_stuff_it) 


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden') 
print('Estonia' in nordic_countries) 
print('Iceland' in nordic_countries) 




