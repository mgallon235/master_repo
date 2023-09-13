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

class problem:
    def __init__(self, problem, urgency, email, postal_code):
        self.problem  = problem
        self.urgency = urgency
        self.email = email
        self.postal_code = postal_code

    def respond(self):
        print(f"""
               Thanks for sending us your concerns. We will evaluate the problem priority {self.urgency} 
               and send it to one of our specialists. We'll get back to {self.email} as soon
               as we have more detail on how to proceed. In the mean time you can visit our QA website:
               www.isolutions.com/QA. In case the problem persists, here is a list of stablishments
               near postal code {self.postal_code}""")

ppp = problem('internet', 1, 'mikel@sp.com', 445667)

ppp.respond()



