it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
len(it_companies) 
it_companies.add('twitter') 
print(it_companies) 
it_companies.update(['Ebenet', 'interlsta', 'excellium'])
print(it_companies) 
it_companies.remove ('Google') 
print(it_companies) 

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27} 
C = A.union(B) 
print(C)

A.intersection(C)

A.issubset(C) 

A.isdisjoint(C) 

C = A.union(B) 

