
######################################
'''Directories , Loops and Classes'''

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



