student = {
'first_name':'wilson',
'last_name':'emma',
'age':20,
'country':'nigeria',
'is_marred':False,
'skills' :['crypto', 'Python'],
'address': 'no 9a ayatoro street'
}
print(len(student)) 
print("type of student skills", type(student['skills']))
student['skills'].append('javascipt') 
print(student['skills']) 
students = student.keys() 
print('student dictionary keys: ', students) 
values = student.values() 
print('value of student: ', values) 
print('student dictionary as tuple: ', student.items()) 
student.pop('age') 
print(student) 
 







