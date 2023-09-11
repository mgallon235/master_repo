'''I Celebrate myself, and sing myself,

And what I assume you shall assume,
For every atom belonging to me as good belongs to you.

I loafe and invite my soul,
I lean and loafe at my ease observing a spear of summer grass.'''

a = 'I Celebrate myself, and sing myself,'
b =  'And what I assume you shall assume, For every atom belonging to me as good belongs to you.'
c= 'I loafe and invite my soul, I lean and loafe at my ease observing a spear of summer grass.'



#%%
## Question 1 - - Which of them contains more characters?
carac = (len(a), len(b), len(c) ) 
print(carac)

#%%
# Question 2 - - Create "full", a string that contains a, b and c.

full = a+' '+' '+b+' '+' '+c
print(full)

#%%
full = a + b + c
print(full)

#%%
#Question - - How many "I" appear in c? And in the whole fragment?
print(c.count('I'))
print(full.count('I'))

#%%
# Cleaning
# lower first
full_l = full.lower()

#%%
# replace signs and empty spaces
f_full_e = full_l.replace(',','').replace('.','').replace(' ','')

#%%
## Question - - Can you count the number of words in total?

n_words = f_full.split()
print(len(n_words))


#%%
new_set = set(f_full_e)
new_set
#%%
print(len(new_set))

#%%
# - Question Add new values to a dictionary 

whitman = {'I':0, 'celebrate':1, 'myself':2}

# Adding new information to dictionary
whitman['and'] = 3
whitman.update({'sing':4})


print(whitman)

### Loops 
#%%

aa = ['a']
while aa == 'a':
    print(a)

#%% 

for num in range(10):
    print(f'The amount of numbers is {num}')

#%%
# Quick exercises

a = []

b=['1','2','3','4','5']
c=[1,2,3,4,5,6,7,8,9,10]

d = [int(x) for x in b]

print(sum(d) + sum(c))

## Result
print(sum([int(x) for x in b])+sum(c))
#%%
for i in b:
    a.append(int(i))
print(a)


#%%

## Question

a = [1,2,3,3,3,3,3,3,4,5,6,7,8,9,10]

for index, val in enumerate(a):
    print(index,val)


#%%
list1 = [[1,2,3],[4,5,6]]

for i in list1:
    print(i)
    for  j in i:
        print(j)



#%%

class Vehicle:

    def __init__(self,color, name, max_speed, mileage):
        self.color = 'White'
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def print_speed(self):
        print(self.color)
    def print_name(self): # this is a method
        print(self.name)
    def print_speed(self):
        print(self.max_speed)
    def print_milage(self):
        print(self.mileage)
    

t = Vehicle('carro',138,10)
print(f'Color: {t.colors}, Vehicle_name: {t.print_name}, Speed: {t.print_speed}, Milage: {t.print_milage} ')

print(t)

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass



# Expected output

"""
Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18
"""

#%%

class Luis:
    def __init__(self,name,school):
        self.name=name
        self.school=school
    def print_name(self): # this is a method
        print(self.name)
    def print_school(self):
        print(self.school)
    def greet(self,morning):
        if morning:
            print('Good morning')
        else:
            print('Good afternoon')
        
        
# Luis("Luis")

instance1=Luis("Luis","BSE")

instance1.print_name()
instance1.greet(False)