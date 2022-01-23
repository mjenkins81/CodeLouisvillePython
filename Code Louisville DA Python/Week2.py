'Birds & Coconuts'
import math
import random


perc = 1/3
coco_wt = 1450
macaw_wt = 900
macaw_limit = macaw_wt * perc
print(macaw_limit)

num_macaws = coco_wt/macaw_limit
print(math.ceil(num_macaws))

'Spam & Strings'

first_name = 'Monty'
last_name = 'Python'
full_name = first_name + ' ' + last_name
print(full_name)

#Describe the sketch comedy group
name = 'Monty Python'
description = 'sketch comedy group'
year = str(1969)

# Introduce them
sentence = name + ' is a ' + description + ' formed in ' + year
print(sentence)

#Describe Monty Python's work
famous_sketch = "Hell's Grannies"
print(famous_sketch)

famous_sketch1 = "Hell's Grannies"
famous_sketch2 = 'The Dead Parrot'
print(famous_sketch1 , famous_sketch2)

famous_sketch1 = "\nHell's Grannies"
famous_sketch2 = '\nThe Dead Parrot'
print('Famous Work:', famous_sketch1 , famous_sketch2)

famous_sketch1 = "\n\tHell's Grannies"
famous_sketch2 = '\n\tThe Dead Parrot'
print('Famous Work:', famous_sketch1 , famous_sketch2)



word1 = 'Good'
end1 = word1[2] + word1[3]
print(end1)

#slicing
word = 'pyton'
word[2:5]
word1[0:2]
word[:2]
word1[2:4]
word1[2:]

word1 = 'Good'
end1 = word1[2:4]
print(end1)

word1 = 'Good'
end1 = word1[2:]

word2 = 'Evening'
end2 = word2[3:]
print(end1, end2)

word1 = 'Good'
half1 = len(word1)//2
end1 = word1[half1:]

word2 = 'Evening'
half2 = len(word2)//2
end2 = word2[half2:]
print(end1, end2)


'Conditional Rules of Engagement'
#Battle Rules
num_knights = 4
    
if num_knights < 3:
    print('Retreat')
    print('Raise the white flag!')
print('Knights of the Round Table')

#Battle Rules
num_knights = 4
    
if num_knights < 3:
    print('Retreat')
else:
    print('Raise the white flag!')
print('Knights of the Round Table')

#Battle Rules
num_knights = 10
    
if num_knights < 3:
    print('Retreat')
else:
    print('Truce?')
print('Knights of the Round Table')


#Battle Rules
num_knights = 4
    
if num_knights < 3:
    print('Retreat')
elif num_knights < 10:
    print('Trojan Rabbit')
elif day == 'Tuesday':
    print('Taco Night')
else: 
    print('Truce?')
    
    
#Battle Rules
num_knights = int(input('Enter the number of knights '))
day = input('Enter day of the week ')
    
if num_knights < 3:
    print('Retreat')
elif num_knights < 10:
    print('Trojan Rabbit')
elif day == 'Tuesday':
    print('Taco Night')
else: 
    print('Truce?')
    

slang = ['cheerio', ' pip pip', 'smashing']
print(slang)

slang.append('cheeky')
slang.append('yonks')
print(slang)

slang.remove('cheeky')
del slang[3]
print(slang)


slang = {'cheerio': 'goodbye', 'knackered':'tired', 'yonks':'ages'}


total = 0
prices = [2.50, 3.50, 4.50]

for price in prices:
    print('Price is ', price)
    total = total + price
    print('Total is ', total)
    
average = total/len(prices)
print('Avg is ', average)

r1 = random.random()
print(r1)

r2 = random.choice([1,2,3,4,5,])
print(r2)

r3 =  random.randint(1, 1000)
print(r3)

for i in range(10):
    ticket = random.randint(1, 1000)
    print(ticket)
    
for i in range(2005, 2016, 2):
    print(i)

numbers = [1,2,3,4,5]


def average(numbers):
    total = 0
    for num in numbers:
       total = total + num
    avg = total/len(numbers)
    return avg
    
prices = [2.50, 3, 4.50, 5]
result = average(prices)
print(result)


def average(numbers):
    total = 0
    for num in numbers:
       total = total + num
    avg = total/len(numbers)
    return avg

def main():    
    prices = [29, 21, 55, 10]
    result = average(prices)
    print(result)

main()


