#filtered list 
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [number for number in numbers if number < 1]
print(filtered_numbers)
#Flattened list 
list_of_lists = [[(1,2,3)],[(4,5,6)],[(7,8,9)]]
flattened_list =[numbers for row in list_of_lists for numbers in row]
print(flattened_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatenend_list = [country for row in countries for country in row]
print(flatenend_list)
#list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
newCountries = []
for x in names:
    for y in x:
        for z in y: 
            newCountries.append(z)
print(newCountries)


#list of dictionaries 
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
newCountries = []
def test():
    for x in countries:
        for y in x:
            for z in y:
                newCountries.append(z.upper())
    return newCountries


new_list = test()
#print("The original list: " + str(new_list))
key_list = ['country', 'city']
n = len(new_list)
res = []
for idx in range (0, n, 2):
    res.append({key_list[0]:new_list[idx], key_list[1] : new_list[idx + 1]})
print(str(res))  


#lambda function
multiple_variable = lambda x1, x2, y1, y2: y2 - y1 / x2 - x1 
print(multiple_variable(2, 2, 6, 10))

