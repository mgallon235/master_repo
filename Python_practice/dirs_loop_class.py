
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



#### Practice

#%%
from datetime import date, timedelta

day_before=0
if day_before == 0:
    my_date=date.today() - timedelta(days=day_before+1) #timedelta helps in calculating the difference between two dates
elif day_before > 0:
    my_date=date.today() - timedelta(days=day_before - (day_before-1)) #timedelta helps in calculating the difference between two dates
else:
    my_date=date.today() # Anything lower than 0 will return current date

#%%
print(date.today())
print(timedelta(days=day_before - (day_before-1)))
print(my_date)
print(day_before)

my_date=str(date.today()-timedelta(days=day_before+1))
print(my_date)

#%%

my_currencies=[]
#my_date=str(date.today()-timedelta(days=day_before+1))
'''We can reuse the variable my_date that we calculated on the previous ifelse statement'''
my_date  = str(my_date)

print(type(my_date))

print(date.today()-timedelta(days=day_before - (day_before-1)))


#%%

# Given exchange rates with decimals
usd_to_jpy = 110.0
print(type(usd_to_jpy))
usd_to_eur = 0.854
type(usd_to_eur)
amount_in_usd = float(input('How much money do you have in USD?'))
type(amount_in_usd)
# Conversion to JPY
amount_in_jpy = amount_in_usd * usd_to_jpy
amount_in_jpy


#%%
# Conversion back to USD using EUR exchange rate
'''Calculate amount in euros from JPY amount'''
amount_in_eur = amount_in_jpy * (1 / usd_to_eur)
amount_in_eur = amount_in_jpy * (1 / usd_to_jpy) * usd_to_eur

print(amount_in_eur)




#%%


A=[[7,1,3],[5,6,4],[1,9,3]]



rows=[[i[0] for i in A],[i[1] for i in A],[i[2] for i in A]]

det=0
for index, row in enumerate(rows) :
    nums=[0,1,2]
    nums.pop(XXX)
    minor=[]   
    myrows=[]
    for j in nums:
        myrows.append(XXX)
    for i in myrows:
        minor.append(XXX)
    det+=((-1)**XXX)*(XXX*XXX-XXX*XXX)

print(det)


#%%
det=0
for index, row in enumerate(rows) :
    #print(index,row)
    nums=[0,1,2]
    nums.pop(index)
    minor=[]   
    myrows=[]
    for  j  in  nums:
        myrows.append(rows[j])
    for i in myrows:
        minor.append(i[1])
        minor.append(i[2])
    det+=((-1)**(index))*row[0]*(minor[0]*minor[3]-minor[2]*minor[1])

print(det)
