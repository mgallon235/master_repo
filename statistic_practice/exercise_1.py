'''I Celebrate myself, and sing myself,

And what I assume you shall assume,
For every atom belonging to me as good belongs to you.

I loafe and invite my soul,
I lean and loafe at my ease observing a spear of summer grass.'''

a = 'I Celebrate myself, and sing myself,'
b =  'And what I assume you shall assume,For every atom belonging to me as good belongs to you.'
c= 'I loafe and invite my soul, I lean and loafe at my ease observing a spear of summer grass.'

# q1 

# variable c
carac = (len(a), len(b), len(c) ) 
print(carac)


# Join all variables
full = a + b + c
print(full)

print(full.split())

# How many I appear in c ? 
values = c.count('I')
values

values_f = full.count('I')
values_f

full.count('')

len(full.split())

print(a[27])

print(c[::-1])

len(set(full))

hh = set(full)

print(len(hh))

# lower first
full_l = full.lower()

print(full_l)

print(len(set(full_l)))


n_full = full_l.replace(',','')

f_full = n_full.replace('.','')

new_set = set(f_full)

print(new_set)

f_full_f = f_full.strip()

final = f_full_f.replace(' ','')

final_set = len(set(final))

final_set




