# q.1
name = ['tarteel', 'asmaa', 'ahmed']
name.insert(0, 'sabrin')
print(name)
name.remove('ahmed')
print(name)
name.append('hamada')
print(name)
name.pop(2)
print(name)

# q.2

friends = ['adel', 'ahmed']
employees = ['samah', 'amjad']
school = ['ali', 'basma']
friends.extend(employees), friends.extend(school)
print(friends)

# q.3
# update()	Updates the dictionary with the specified key-value pairs

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2), dic1.update(dic3)
print(dic1)

# q.4

dicti_square = {}

for k in range(1, 16):
    dicti_square[k] = k ** 2

print(dicti_square)

# q.5

d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':150, 'b':200, 'd':400}

new_dict = {}

# Add values from dict1
for k, v in d1.items():
    new_dict[k] = v

for k, v in d2.items():
    if k in new_dict:
        new_dict[k] += v
    else:
        new_dict[k] = v

print(new_dict)

# q.6

keys = ['ten', 'twenty', 'thirty']
values = [10, 20, 30]
new_dict = {}

for k in range(len(keys)):
    new_dict[keys[k]] = values[k]

print(new_dict)

# q.7
sampledict = {
    'class': {
        'studant' : {
           'name': 'mike',
           'marks': {
            'physics': 70,
            'history': 80
           }
        }
    }
}


history_mark = sampledict['class']['studant']['marks']['history']
print(history_mark)

# q.8

mydict = {1:'alaa', 5:'hadeel', 7:'hanin', 13:'malak'}
my = {k:v
      for k,v in mydict.items()
      if k < 10
      }
print("->".join(my.values()))
