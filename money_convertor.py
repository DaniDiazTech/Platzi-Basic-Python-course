DOLLAR = 3700
     

def cop_to_usd(money):
    return round((money / DOLLAR), 2)

def usd_to_cop(money):
    return round((money * DOLLAR), 2)

print(
    """
    What do you want to do?
    [0]: Convert USD to COP
    [1]: Convert COP to USD
    """
)

action = input('Your option: ').strip()

if action == "0":
    value = usd_to_cop(float(input("What's the amount? ")))
    print('Your dollars have been converted')
    print(f'You have ${value} Colombian Pesos')
elif action == "1":
    value = usd_to_cop(float(input("What's the amount? ")))
    print('Your pesos have been converted')
    print(f'You have ${value} Dollars')
else:
    print('Sorry, please enter a valid action')