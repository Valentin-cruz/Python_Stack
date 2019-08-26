# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x [1][0] = 15
print(x)

students [0]['last_name'].append('Bryent')
students [0]['last_name'].pop(1)
print(students)

sports_directory [1]['soccer'].append('Andres')
sports_directory [1]['soccer'].pop(1)
print(sports_directory)

z[0]{'y'}.append(30)
z[0]{'y'}.pop(1)

# Iterate Through a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}

def iterateDictionary(students):
    for k, v in students.items():
        print(k, v)

def iterateDictionary1(first_name, students):
    for d in students:
        print(d[first_name])

def iterateDictionary2(last_name, students):
    for d in students:
        print(d[last_name])

def printInfo(dojo):
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)