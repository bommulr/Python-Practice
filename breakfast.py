def breakfast(budget):
    dish = ''
    items = ''
    new_budget = 0
    response = ''
    dishes = {'idly' : 5 , 'dosa' : 25 , 'upma' : 30 , 'vada' : 7 , 'punugu' : 5}

    while budget > 0 and response == '':

        print(f'Your budget is {budget}')
        print(f'Availabe items are {list(dishes.keys())}')

        while dish not in list(dishes.keys()):
            
            dish = input('What would you like for breakfast?')
            print(f'One {dish} costs {dishes[dish]}')
            items = int(input(f"How many {dish}'s you want to add?"))
            new_budget += dishes[dish]*items
            budget = budget - new_budget
            print(f'You will get your {items} {dish} in 10 minutes')
            print(f'Your remaining balance : {budget}')
            
        if budget <= 0:

            print('Thank you')
            print(f'You will get your {items} {dish} in 10 minutes')
            print(f'Current remaining budget = {budget}')
        else:    
            response = input('You want to add items again?:')

        if response.lower() == 'yes':
            print(f'You currently ordered {items} {dish}')
            new_dish = input('What you want to add:')
            print(f'One {new_dish} costs {dishes[new_dish]}')
            number = int(input('How many will you add:'))
            new_dish = new_dish.lower()
            new_balance = dishes[new_dish]*number
            budget -= new_balance
            print(f'You will get your {dish} and {new_dish} soon')
        else:
            print('Thank you')
            print(f'You will get your {items} {dish} in 10 minutes')
            print(f'Current remaining budget = {budget}')
        if budget <= 0:
            print('Cannot add more')
            print(f'Remaining balance is {budget}')
        print(f'Remaining balance is {budget}')
        print('Thank you, your order is getting ready')
        
    if budget == 0:

        print(f'Purse zero, you have {budget}')
    else:
        pass




breakfast(100)