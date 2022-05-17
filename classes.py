from random import randrange

class SakClass:
    """
        σακουλάκι με τα γράμματα του παιχνιδιού
    """
    total_words_sak = None
    lets = {'A': [1, 1], 'Β': [1, 8], 'Γ': [1, 4], 'Δ': [1, 4], 'Ε': [1, 1],
            'Ζ': [1, 10], 'Η': [1, 1], 'Θ': [1, 10], 'Ι': [1, 1], 'Κ': [1, 2],
            'Λ': [1, 3], 'Μ': [1, 3], 'Ν': [1, 1], 'Ξ': [1, 10], 'Ο': [1, 1],
            'Π': [1, 2], 'Ρ': [1, 2], 'Σ': [1, 1], 'Τ': [1, 1], 'Υ': [1, 2],
            'Φ': [1, 8], 'Χ': [1, 8], 'Ψ': [1, 10], 'Ω': [1, 3]}

    def __init__(self, number):
        SakClass.total_words_sak = number

    def randomize_sak(self):  # ετοιμάζει το σακουλάκι με τα γράμματα
        if SakClass.total_words_sak >= 7:  # αν χωραει να παρει 7 γραμματα απο σακουλι
            letters = list(SakClass.lets)
            self.letters = []  # τα γραμματα που θα παιξει ο παικτης/Η\Υ
            self.points = []  # οι ποντοι των γραμματων
            for i in range(7):  # 7 γραμματα, τυχαια καθε φορα

                random_number = randrange(24)  # τυχαιος αριθμος
                while SakClass.lets.get(letters[random_number])[0] <= 0:  # οσο υπαρχει το νουμερο, ψαχνει αλλο
                    random_number = randrange(24)

                self.letters.append(letters[random_number])
                self.points.append(SakClass.lets.get(letters[random_number])[1])
                SakClass.lets.get(self.letters[i])[0] -= 1  # μειωνω την εμφανισει της λεξης

    def getletters(self):  # βγάζει από το σακουλάκι με τον παίκτη τα γραμματα που χρειαζεται
        SakClass.total_words_sak -= 7  # βγαινουν απο το σακουλακι 7 γραμματα
        for i in range(7):
            print(f'{self.letters[i]} - {self.points[i]} ', end="")
        print()

    def putbackletters(self):  # επιστρέφει γράμματα παίκτη στο σακουλάκι
        SakClass.total_words_sak += 7  # μπαινουν στο σακουλακι 7 γραμματα
        for i in range(7):
            SakClass.lets.get(self.letters[i])[0] += 1  # αυξανω την εμφανισει της λεξης

    def restorecorrectletters(self, answer):  # αντικαταστει τα νεα γραμματα
        if SakClass.total_words_sak >= len(answer): # αλλαζω μονο τα σωστα γραμματα που εδωσε ο χρηστης
            SakClass.total_words_sak -= len(answer)
            for letter in answer:
                for letter2 in self.letters:
                    if letter.upper() == letter2: # βρισκω το σωστο γραμμα
                        random_number = randrange(24) # περνω ενα αλλο τυχαιο γραμμα που να υπαρχει στο λεξικο
                        letters = list(SakClass.lets)
                        while SakClass.lets.get(letters[random_number])[0] <= 0:  # οσο υπαρχει το νουμερο, ψαχνει αλλο
                            random_number = randrange(24)

                        index = self.letters.index(letter) # αλλαζω την τιμη μονο εκεινου του στοιχειου
                        self.letters[index] = letters[random_number]
                        self.points[index] = SakClass.lets[letters[random_number]][1]
                        SakClass.lets[self.letters[index]][0] -= 1


class Player:
    """
        βασική κλάση για τους παίκτες Player και Computer
    """

    def __init__(self):
        pass

    def __repr__(self):
        pass


class Human(Player):
    """
        περιγράφει το πως παίζει ο παίκτης
    """

    def __init__(self, name):
        super().__init__()
        self.username = name
        self.round = 0
        self.points = 0

    def __repr__(self):
        pass

    def play(self, sak, words, score):
        while True:
            answer = input("Δώσε την λέξη ή 'p' (για pass): ").upper()
            if answer == 'P':
                break
            counter_flag = 0
            for letter in answer:
                for letter2 in sak.letters:
                    if letter.upper() == letter2:
                        counter_flag += 1
                        break

            if counter_flag == len(answer):  # επελεξε σωστα γραμματα
                break
            else:  # λαθος γραμματα
                print('Επέλεξες λάθος γράμματα, προσπάθησε ξανά!')

        round_points = 0
        if answer == 'P':  # επελεξε pass
            sak.putbackletters()
            sak.randomize_sak()
            self.round += 1
            print(f'Παίκτης: {self.username} \t Σκορ: {self.points} \t Σακουλάκι: {sak.total_words_sak} \t Γύρος: {self.round}')
            print(f'Διαθεσιμα γράμματα - Πόντοι: ', end="")
            sak.getletters()
        elif answer in words:  # βρηκε σωστη λεξη
            print('Σωστή λέξη - Κέρδισες ', end='')
            for letter in answer:
                for i in range(len(sak.letters)):
                    if letter.upper() == sak.letters[i]:
                        round_points += sak.points[i]

            score += round_points
            self.points += score
            print(round_points, 'Πόντους. Το Σκορ σου είναι: ', score)
            input('Enter για συνέχεια..  ')
            print('=======================================================')
            sak.restorecorrectletters(answer)
            print(SakClass.total_words_sak)
            self.round += 1
            print(f'Παίκτης: {self.username} \t Σκορ: {self.points} \t Σακουλάκι: {sak.total_words_sak + 7} \t Γύρος: {self.round}')
            print(f'Διαθεσιμα γράμματα - Πόντοι: ', end="")
            for i in range(7):
                print(f'{sak.letters[i]} - {sak.points[i]} ', end="")
            print()
        else:  # βρηκε λαθος λεξη
            print('Λάθος λέξη')
            sak.randomize_sak()
            self.round += 1
            print(f'Παίκτης: {self.username} \t Σκορ: {self.points} \t Σακουλάκι: {sak.total_words_sak} \t Γύρος: {self.round}')
            print(f'Διαθεσιμα γράμματα - Πόντοι: ', end="")
            sak.getletters()


class Computer(Player):
    """
        περιγράφει το πως παίζει ο υπολογιστής
    """

    def __init__(self, difficulty):
        super().__init__()
        self.round = 0
        self.points = 0
        self.difficulty = difficulty

    def __repr__(self):
        pass

    def play(self, sak, words, score):
        import itertools
        total_letters = ''
        for letter in sak.letters:
            total_letters += letter
        if self.difficulty == '1': # easy mode
            combination = 1
            while True:
                pc_word = ''
                combination += 1
                result_list = list(itertools.permutations(total_letters, combination))
                for result in result_list:
                    string = ''
                    for char in result:
                        string += char
                    if string.upper() in words: # found first correct word
                        pc_word = result
                        break

                if pc_word != '':
                    break

            pc_points = 0
            for char in pc_word:
                index_of_pc_word_in_sak = sak.letters.index(char)
                pc_points += sak.points[index_of_pc_word_in_sak]
            print(pc_word)
            print(pc_points)
        elif self.difficulty == '2': # hard mode
            pass
        elif self.difficulty == '3': # expert mode
            pass

class Game:
    """
        περιγράφει πως εξελίσσεται μια παρτίδα
    """

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def setup(self):
        pass

    def run(self):
        pass

    def end(self):
        pass
