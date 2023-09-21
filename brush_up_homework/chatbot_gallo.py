class bot:
    def __init__(self):
        self.name  = 'Trailer800'
        self.code = '999'
        self.job = 'Chat Bot' 
    # Actions
    # Objective: find whats the high level problem / add more attributes to chatbot from customer
    def greeting(self,names):
        problem = input(f"""
               Hi {names} thanks for contacting with XXXX. How can I help you today?""")
        #rember to add a space between cuotes
        problem = problem.split(' ')
        mlist = []
        for val in problem:
            val= val.replace('.','')
            val = val.lower()
            mlist.append(val)

        issues = []
        for item in mlist:
            if item in ['internet','interne','interet','inteert']:
                    #print(item)
                    issues.append('internet')
            elif item in ['phone','mobile','iphone','android','sim','sim card','4g']:
                    #print(item)
                    issues.append('phone')
            elif item in ['bills','bill','payments','invoice','invoices']:
                    #print(item)
                    issues.append('bills')
            else:
                pass
                    
        return set(issues)
    

               
    def respond(self,names,email,status,postal_code):
        print(f"""
               Thanks {name} for sending us your concerns. We will evaluate the problem priority {status} 
               and send it to one of our specialists. We'll get back to {email} as soon
               as we have more detail on how to proceed. In the mean time you can visit our QA website:
               www.isolutions.com/QA. In case the problem persists, here is a list of stablishments
               near postal code {postal_code}""")


# Create bot called rex:
def main():
     rex = bot()
     customer = input(f'Hello! welcome to XXXX corp customer service platform. Im REX, the ultimate {rex.job} {rex.name}. what is your name?')
     var = rex.greeting(customer)
     return var


# Execute script
main()



#########################################################
## greet the customer
name = input('Please enter your name ')
print('Hi',name,'nice to meet you!')


## choose problem 
problem = input('''
      Is your question related to one of these topics?: \n
      1. You have a problem with your internet.
      2. You have a problem with your phone.
      3. You want to check information about your bills.
      4. Other \n
      Please enter the corresponding number''')


## Redirect to  class/functions
if problem == 1:
    pass
elif problem ==2:
    pass
elif problem ==3:
    pass
elif problem ==4:
    problem_1 = input('please enter your problem: ')
    urgency_1 = input('rank your problem from 1 - 5 (1: high priority and 5: low priority )')
else:
    pass

## Define first class
### Corrected

