import classes

def main_menu():
    print("------------------------------")
    print("Επέλεξε μια απο τις παρακάτω επιλογές (1,2,3,q)")
    print('\t 1. Σκορ')
    print('\t 2. Ρυθμίσεις')
    print('\t 3. Παιχνίδι')
    print('\t q. Έξοδος')
    print("------------------------------")

def settings_menu(first_message, second_message, third_message):
    print('2. Ρυθμίσεις')
    print('\tΔυσκολία Υ\Η:')
    print('\t\t ', first_message)
    print('\t\t ', second_message)
    print('\t\t ', third_message)
    print('<= Back (b)')
    print("------------------------------")
def message(username, score, letters, round):
    print(f'Παίκτης: {username} \t Σκορ: {score} \t Σακουλάκι: {letters} \t Γύρος: {round}')
    print(f'Διαθεσιμα γράμματα - Πόντοι: ', end="")


with open('greek.txt', 'r', encoding="utf-8") as f:
    with open('greek7.txt', 'w') as f7:
        for line in f:
            if len(line) <= 8:
                f7.write(line)

words = []
with open('greek7.txt', 'r') as f7:
    for line in f7:
        words.append(line.strip('\n'))

pc_difficulty = '1'
while True: # το παιχνιδι σταματαει μονο οταν ο παικτης δωσει 'q' ή ληξει το παιχνιδι
    print('\tΚαλώς ήρθες στο SCRABBLE')
    main_menu()
    user_input = input('Βάλε την επιλογή σου εδώ: ')
    while True:
        if user_input == '1' or user_input == '2' or user_input == '3' or user_input.upper() == 'Q':
            break
        else:
            user_input = input('Δώσε μια από τις διαθέσιμες επιλογές (1, 2, 3, q): ')

    if user_input.upper() == 'Q':
        exit()
    elif user_input == '1':
        print("------------------------------")
        print('Score')
    elif user_input == '2':
        first_message = '1)Εύκολο (MIN)'
        second_message = '2)Δύσκολο (MAX)'
        third_message = '3)Expert (SMART)'
        if pc_difficulty == '1':
            first_message = '--> 1)Εύκολο (MIN)'
        elif pc_difficulty == '2':
            second_message = '--> 2)Δύσκολο (MAX)'
        else:
            third_message = '--> 3)Expert (SMART)'

        settings_menu(first_message, second_message, third_message)
        pc_lvl = input("Δώσε το lvl του υπολογιστή η 'b' (για back): ")
        while True:
            if pc_lvl == '1':
                pc_difficulty = '1'
                first_message = '--> 1)Εύκολο (MIN)'
                second_message = '2)Δύσκολο (MAX)'
                third_message = '3)Expert (SMART)'
                settings_menu(first_message, second_message, third_message)
                pc_lvl = input("Δώσε το lvl του υπολογιστή η 'b' (για back): ")
            elif pc_lvl == '2':
                pc_difficulty = '2'
                first_message = '1)Εύκολο (MIN)'
                third_message = '3)Expert (SMART)'
                second_message = '--> 2)Δύσκολο (MAX)'
                settings_menu(first_message, second_message, third_message)
                pc_lvl = input("Δώσε το lvl του υπολογιστή η 'b' (για back): ")
            elif pc_lvl == '3':
                pc_difficulty = '3'
                first_message = '1)Εύκολο (MIN)'
                second_message = '2)Δύσκολο (MAX)'
                third_message = '--> 3)Expert (SMART)'
                settings_menu(first_message, second_message, third_message)
                pc_lvl = input("Δώσε το lvl του υπολογιστή η 'b' (για back): ")
            elif not pc_lvl == 'b':
                pc_lvl = input('Δώσε μια από τις διαθέσιμες επιλογές (1, 2, 3, b): ')
            elif pc_lvl == 'b':
                break

        main_menu()
    elif user_input == '3':
        username = input('Ποιό είναι το username σου: ')
        scorePlayer = 0
        scorePC = 0
        round = 0
        sak = classes.SakClass(43)
        human = classes.Human(username)
        pc = classes.Computer(pc_difficulty)
        sak.randomize_sak()
        print(f'Παίκτης: {username} \t Σκορ: {scorePlayer} \t Σακουλάκι: {sak.total_words_sak} \t Γύρος: {round}')
        print(f'Διαθεσιμα γράμματα - Πόντοι: ', end="")
        sak.getletters()

        while True:
            human.play(sak, words, scorePlayer)
            pc.play(sak, words, scorePC)
            round += 1