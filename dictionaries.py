# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 22:53:02 2019

@author: Awam Victor
"""
#dictionaries
#a simple dicitionary 
print("Working with Dictionary")
print("\n")
alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

#adding new key-value pairs
alien_1 = {'color':'green', 'points':5}
alien_1['x_position']=0
alien_1['y_position']=25
print(alien_1)

#modifying vakues that are in a dictionary
alien_2= {'color':'green'}
print(alien_2)
alien_2['color']='Yellow'
print("the alien is "+str(alien_2))

#removing key-value pair; use **del**
bag= {'color':'red', 'size':20}
print(bag)
del bag['size']
print(bag)

#A dictionary similar objects
favorite_languages= {
        'jen':'Python',
        'Sarah':'Java',
        'Aaron':'JavaScript',
        'Victor':'PHP',
        'Awam':'R',
        'Akachi':'Ruby'
        }

print(favorite_languages)

#looping through a dictionary
#looping through all key-value pairs

person = {
        'username':'AryanVikta',
        'first_name':'Aaron',
        'last_name':'Victor'}
for k,v in person.items():
    print(k+ " = "+ v)

#looping through all keys in dictionary
favorite_languages= {
        'jen':'Python',
        'Sarah':'Java',
        'Aaron':'JavaScript',
        'Victor':'PHP',
        'Awam':'R',
        'Akachi':'Ruby'
        }
for language in favorite_languages.keys():
    print(language.title())
friends= ['Victor', 'Sarah','Aaron']
#more concise form of the above
for name in favorite_languages:
    print(name.title())
    if name in friends:
        print(name+"'s favorite language "
              "is "
              +favorite_languages[name])
 
#looping through a dictionary keys in order
favorite_languages= {
        'Jen':'Python',
        'Sarah':'Java',
        'Aaron':'JavaScript',
        'Victor':'PHP',
        'Awam':'R',
        'Akachi':'Ruby'
        }
for name in sorted(favorite_languages.keys()):
    print(name)

#looping through all values in a dictionary
favorite_languages= {
        'jen':'Python',
        'Sarah':'Java',
        'Aaron':'JavaScript',
        'Victor':'PHP',
        'Awam':'R',
        'Akachi':'Ruby',
        'james':'Python'
        }
for name in favorite_languages.values():
    print(name)
#sorted 
for nam in sorted(favorite_languages.values()):
    print(nam)
#check for repeat
for val in set(favorite_languages.values()):
    print(val)

#nesting
#a list of dictionaries
buses=[]
#make 30 green buses
for bus_number in range(30):
    new_bus= {'color':'blue','speed':200}
    buses.append(new_bus)
#show the first 5 buses
for bus in buses[:5]:
    print(bus)

#modify the first 3 buses
for bus in buses[:3]:
    if bus['color']=='blue':
        bus['color']='red'
        bus['speed']='300'
        bus['drift']='2500'
print(bus)
        
#list in a dictionary
favorite_cars={
        'aaron':['bugatti','henessy'],
        'victor':'ford',
        'aryan':['mercedes','toyota']
        }
print('Aaron loves '
      +str(favorite_cars['aaron']))
print("your favorite cars are ")
for aaron in favorite_cars['aryan']:
    print(aaron)

#dictionary in dictionary
users={
       'akpamu':{
               'first':'Akpamu',
               'last':'Obi',
               'occupation':'thief'
               },
       'john':{
               'first':'john',
               'last':'Nick',
               'occupation':'vampire'
               }
      }
for username,user_info in users.items():
    print("\nusername" +username)
    print('Occupatn: '+user_info['occupation'])
    
