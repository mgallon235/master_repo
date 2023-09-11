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
