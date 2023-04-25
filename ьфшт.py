import random

result = {"computer": 0, "player": 0} #словник
choice = 0
computer_choice = 0

def menu():
     print("rock,paper,scissors")
def menu_choice():
    global choice
    global computer_choice
    choice = input("Введіть [r] - rock, [p] - paper, [s] - scissors \n")
    computer_choice = random.choice('rps')

    print(f"Ви обрали: {choice}, бот обрав {computer_choice}")
    return choice, computer_choice

def  winner_player(result):
    print("переміг користувач")  # winner_player(result)
    result['player'] += 1
    print(f"рахунок бота {result['computer']}, гравець {result['player']} ")
def winner_bot(result):
    print("переміг бот")  # winner_player(result)
    result['computer'] += 1
    print(f"рахунок бота {result['computer']}, гравець {result['player']} ")

def win(result):
    if result['computer'] == result['player']:
        print("DRAW")
    elif result['computer'] > result['player']:
        print("Переможець гри бот!")
    elif result['computer'] < result['player']:
        print("Переможець гри користувач!")

def game():
 while True:
    menu_choice()
    if str.lower(choice) == computer_choice:
        print("DRAW")
        print(f"рахунок бота {result['computer']}, гравець {result['player']} ")
    elif str.lower(choice) == 'r' and computer_choice == 's':
        winner_player(result)
    elif str.lower(choice) == 'p' and computer_choice == 's':
        winner_player(result)
    elif str.lower(choice) == 's' and computer_choice == 'p':
        winner_player(result)
    elif str.lower(choice) == 'p' and computer_choice == 's':
        winner_bot(result)
    elif str.lower(choice) == 'r' and computer_choice == 'p':
        winner_bot(result)
    elif str.lower(choice) == 's' and computer_choice == 'r':
        winner_bot(result)
    else:
        print("помилка!")
    print("продовжити гру, чи показати абсолютного переможця?")
    question = input("[y] - yes [n] - no")
    if str.lower(question) == 'y':
        continue
    elif str.lower(question) == 'n':
        win(result)
        break
    else:
        print("не зовсім згода, але продовжуємо)")
        continue
menu()
game()

