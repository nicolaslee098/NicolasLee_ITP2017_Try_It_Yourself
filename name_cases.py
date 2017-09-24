name = 'hello pier, would you like to learn some python today?'
print (name.title())
print (name.upper())
print (name. lower())
var = 'albert einstein once said "creativity is contagious, pass it on"'
print (var)
famous_person = ('albert einstein')
message = ('"creativity is contagious, pass it on"')
print (message)
favourite_language = ' hello: \n\tpython \n\t a\n\t b\n\t c '
print (favourite_language)
print (favourite_language.rstrip())
print (favourite_language.lstrip())
print (favourite_language.strip())
age = 23
message ="Happy " +str(age)+ "rd Bitrhday!"
print (message)
# if no str, not working because integer.
# if list (strins) needs to use square bracket [] and its in order starts from 0
family = ["mom", "Dad", "Brother"]
print (family[2])
print (family [0], family[1])
print (family[-1])
#add a list, use append
#replace the list, below
family[0] = 'apapun'
print (family)
family.append ('yey')
print (family)
family.insert (3, 'new sister')
print (family)
del family [1]
print (family)
#excersice chap 3
print ('Dinner party')
names = ['pier', 'dumac', 'excel']
print (names)
del names [2]
print (names)
names.append ('las')
print (names)
a = '1'
b = '2'
print (int(a) +int (b))
print (float (a) + float (b))
print (int (a) + float (b))
#anything to integer use int, to float use float
cars = ['toyota', 'subaru', 'suzuki', 'hyundai']
cars.reverse ()
print (cars)
cars.sort (reverse=True)
# True or False, capital
print (sorted(cars))
len(cars)
print (cars)
data =['A', 'C', 'B', 'E', 'D']
print (sorted(data))
print (data)
#sorted data
# loop  can be used by using for, while, do while
'''
comment 
'''
print (data[0])


#write a program which will find all such numbers which are divisible by 7, but are not a multiple pf 5, between 2000 and 3200, the number should be printed in a comma-separated sequence on a line
list=[]
for a in range (2000,3200):
    if (a%7)==0 and (a%5)!=0:
        list.append(a)
print(list)
# in range, divide by 7 = 0 and divide by 5 can not be 0 (!)


#write a program which will find all such numbers which are divisible by 7, but are not a multiple pf 5, between 2000 and 3200, the number should be printed in a comma-separated sequence on a line
for a in range (2000,3200):
    if (a%7)==0 and (a%5)!=0:
        print (a)


for b in range (3000,6000):
    if(b%5)==0 and (b%8)!=0:
        print (b)

var=[]
for y in range (90, 30000):
    if (y%3)==0 and (y%5)!=0:
        var.append (y)
print (var)



for i in range (5):
    print(i)
