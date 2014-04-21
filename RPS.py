def show(type1, type2):
    if type1 == 1:
        print("         _________")
        print("--------'   ______)")
        print("           (_______)")
        print("           (_______)")
        print("           (______)")
        print("--------.__(_____)")
    elif type1 == 2:
        print("      _______")
        print("-----'   ____)____")
        print("            ______)")
        print("            _______)")
        print("           _______)")
        print("---.__________)")
    elif type1 == 3:
        print("      ________")
        print("-----'    ____)____")
        print("             ______)")
        print("         __________)")
        print("        (____)")
        print("----.__(___)")
    print("____________________")
    if type2 == 1:
        print("         _________")
        print("--------'   ______)")
        print("           (_______)")
        print("           (_______)")
        print("           (______)")
        print("--------.__(_____)")
    elif type2 == 2:
        print("      _______")
        print("-----'   ____)____")
        print("            ______)")
        print("            _______)")
        print("           _______)")
        print("---.__________)")
    elif type2 == 3:
        print("      ________")
        print("-----'    ____)____")
        print("             ______)")
        print("         __________)")
        print("        (____)")
        print("----.__(___)")

def game():
    from random import randrange
    from time import sleep
    roundCount = 0
    wins = 0
    ties = 0
    losses = 0
    rounds = raw_input('How many rounds (1 to 11): ')
    try:
        rounds = int(rounds)
    except ValueError:
        print("Whoops, it looks like that is not a vaild round number.  Giving you a random round count.")
        rounds = randrange(1, 12)
        print("This game will last you %d rounds" % rounds)
    numSwitch = {'R' : 1, 'ROCK' : 1, 'P' : 2, 'PAPER' : 2, 'S' : 3, 'SCISSORS' : 3}
    if int(rounds) > 11:
        rounds = randrange(1, 12)
    while (int(roundCount) < int(rounds)):
        i = raw_input('Enter rock, paper, or scissors: ')
        c = randrange(1, 4)
        print('')
        try:
            i = i.upper()
            i = numSwitch[i]
        except Exception:
            i = 0
            print('Oops, you made a typo. Try retrying. Check spelling.')
            roundCount = roundCount - 1
        if   i == c:
            print('It was a tie. Try again :|')
            show(i, c)
            ties = ties + 1
        elif i == 1 and c == 2:
            print('Ooh, looks like paper covers rock :(')
            show(c, i)
            losses = losses + 1
        elif i == 1 and c == 3:
            print('Yay! Rock crushes scissors :)')
            show(i, c)
            wins = wins + 1
        elif i == 2 and c == 1:
            print('Yay! Paper crushes rock :)')
            show(i, c)
            wins = wins + 1
        elif i == 2 and c == 3:
            print('Ooh, looks like scissors cuts paper :(')
            show(c, i)
            losses = losses + 1
        elif i == 3 and c == 1:
            print('Ooh, looks like rock crushes scissors :(')
            show(c, i)
            losses = losses + 1
        elif i == 3 and c == 2:
            print('Yay! Scissors cuts paper :)')
            show(i, c)
            wins = wins + 1
        elif i == 0:
            roundCount = roundCount - 1
        roundCount = roundCount + 1
        print('\n' * 2)
        print('The scores are as follows: \n Wins:   %d \n Ties:   %d \n Losses: %d' % (wins, ties, losses)) 
if __name__ == '__main__':
    game()
