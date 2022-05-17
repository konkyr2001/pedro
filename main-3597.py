import classes


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

print('\tΚαλώς ήρθες στο SCRABBLE')
print("------------------------------")
print("Επέλεξε μια απο τις παρακάτω επιλογές (1,2,3,q)")
print('\t 1. Σκορ')
print('\t 2. Ρυθμίσεις')
print('\t 3. Παιχνίδι')
print('\t q. Έξοδος')
print("------------------------------")

user_input = input('Βάλε την επιλογή σου εδώ: ')
while user_input != '1' and user_input != '2' and user_input != '3' and user_input.upper() != 'Q':
    user_input = input()

if user_input.upper() == 'Q':
    exit()
elif user_input == '1':
    print('Score')
elif user_input == '2':
    print('Settings')
else:
    username = input('Ποιό είναι το username σου: ')

    scorePlayer = 0
    scorePC = 0
    round = 0
    sak = classes.SakClass(50)
    human = classes.Human()
    pc = classes.Computer()

    while True:
        sak.randomize_sak()
        message(username, scorePlayer, classes.SakClass.total_words_sak, round)
        sak.getletters()

        scorePlayer += human.play(sak, words, scorePlayer)
        round += 1
