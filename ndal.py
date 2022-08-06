# 1)Update values in dictionaries and lists
#   a)Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#   b)Change the last_name of the first student from 'Jordan' to 'Bryant'
#   c)In the sports_directory, change 'Messi' to 'Andres'
#   d)Change the value 20 in z to 30
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
# # answer
x[1][0] = 15
print(x)
students[0]['last_name'] = 'Bryant'
print(students[0])
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])
z[0]['y']=30
print(z)

# 2)Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# #answer
def iterateDictionary(students):
    for each_key in students:
        print(each_key)
    # for x in range (len(students)):
    #     print(students[0]['first_name']['last_name'])
iterateDictionary(students)

# 3)Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
    # a)And iterateDictionary2('last_name', students) should output:
students = [
    {'first_name':'Michael', 'last_name': 'Jordan'},
    {'first_name':'John', 'last_name': 'Rosales'},
    {'first_name':'Mark', 'last_name': 'Guillen'},
    {'first_name':'KB', 'last_name': 'Tonel'}
    ]
# print(students)
def iterateDictionary2(students):
    for each_key in students:
        print(each_key['first_name']) # comment out to change between first namd and last name
        print(each_key['last_name']) # comment out to change between last name and first
        #both enabled prints first name last name through each index of students
iterateDictionary2(students)

# 4)Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
winter = {
   'mountains': ['Teton', 'Telluride', 'Powderhorn', 'Patagonia', 'Baldface', 'Spinal-Tap', 'Burbank'],
   'styles': ['Glades', 'Cliffs', 'Backcountry', 'Groomed', 'Park', 'Hike-To']
}
def printInfo(winter):
    for i in (winter):
        if (i=='mountains'):
            print(len(winter['mountains']), "Mountains")
            for j in (winter['mountains']):
                print(j)
        if (i=='styles'):
            print(len(winter['styles']), "Styles")
            for h in (winter['styles']):
                print(h)
printInfo(winter)
