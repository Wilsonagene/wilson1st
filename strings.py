f = 'thirty'
s = 'days,'
t = 'of,'
fo = 'python'
all = f + s + t + fo 
print(all)

fi = 'coding,'
sec = 'for,'
tr = 'all.' 
company = fi + sec + tr
print(company)
len(company)
print(len(company)) 
print(company.swapcase()) 
print(company.capitalize())
print(company.title())
print(company.swapcase()) 
first_word = company[0:6] 
print(company.replace('coding', 'python'))
challenge = 'Python for Everyone'
print(challenge.replace('Everyone', 'All')) 
challenge =  'Coding For All'
print(challenge.split()) 
challenge = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(challenge.split(',')) 
challenge =  'Coding For All' 
first_letter = challenge[0]
print(first_letter)
challenge = 'Coding For All' 
sub_string = 'C'
print(challenge.index(sub_string)) 
challenge = 'Coding For All'
sub_string = 'F'
print(challenge.index(sub_string)) 
challenge = 'Coding For All People'
print(challenge.find('l'))  
challenge = 'You cannot end a sentence with because because because is a conjunction'
print(challenge.find('because')) 
challenge = 'You cannot end a sentence with because because because is a conjunction'
sub_string = 'because'
print(challenge.index(sub_string)) 
challenge = 'You cannot end a sentence with because because because is a conjunction'
middle_words = challenge [31:54] 
print(middle_words) 
challenge = 'Coding For All'
print(challenge.startswith('Coding')) 
print(challenge.endswith('Coding')) 
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) 
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] 
result = '# '.join(python_libraries) 
print(result) 
print('I am enjoying this challenge.\nI just wonder what is next.') 
print('name\tage\tcountry')
print('wilson\t13\tnigeria') 
radius = 10 
area = 3.14 * radius ** 2 
formated_string = 'the area of a circle with {} is {} meters square'.format(radius,area) 
print(formated_string) 
a = 8 
b = 6 
print('{} + {} = {}'.format(a, b, a + b))  
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
