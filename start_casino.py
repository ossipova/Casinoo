from logic_casino import bet
my_money = 1000
while True:
    print('Your balance is ' + str(my_money))
    print('Do you want to start game? (yes or no)')
    a = input('')
    if a == 'no':
        print('Game over!')
        break
    elif a == 'yes':
        numm = int(input('Guess a number from 1 to 30 -'))
        amount = int(input('How much would you like to bet? - '))
        my_money -= amount
        my_money += bet(numm, amount)
    else:
        print('Please check your entry.')





