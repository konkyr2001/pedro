from random import randrange


class SakClass:
    """
        σακουλάκι με τα γράμματα του παιχνιδιού
    """
    total_words_sak = None
    lets = {'A': [12, 1], 'Β': [1, 8], 'Γ': [2, 4], 'Δ': [2, 4], 'Ε': [8, 1],
            'Ζ': [1, 10], 'Η': [7, 1], 'Θ': [1, 10], 'Ι': [8, 1], 'Κ': [4, 2],
            'Λ': [3, 3], 'Μ': [3, 3], 'Ν': [6, 1], 'Ξ': [1, 10], 'Ο': [9, 1],
            'Π': [4, 2], 'Ρ': [5, 2], 'Σ': [7, 1], 'Τ': [8, 1], 'Υ': [4, 2],
            'Φ': [1, 8], 'Χ': [1, 8], 'Ψ': [1, 10], 'Ω': [3, 3]}

    def __init__(self, number):
        SakClass.total_words_sak = number

    def randomize_sak(self): # ετοιμάζει το σακουλάκι με τα γράμματα
        if SakClass.total_words_sak >= 7:  # αν χωραει να παρει 7 γραμματα απο σακουλι
            letters = list(SakClass.lets)
            self.letters = [] # τα γραμματα που θα παιξει ο παικτης/Η\Υ
            self.points = [] # οι ποντοι των γραμματων
            for i in range(7):  # 7 γραμματα, τυχαια καθε φορα

                random_number = randrange(24)
                while SakClass.lets.get(letters[random_number])[0] == 0: # οσο υπαρχει το νουμερο, ψαχνει αλλο
                    random_number = randrange(24)

                self.letters.append(letters[random_number])
                self.points.append(SakClass.lets.get(letters[random_number])[1])
                SakClass.lets.get(letters[random_number])[0] -= 1

    def getletters(self): # βγάζει από το σακουλάκι με τον παίκτη 7 γραμματα
        SakClass.total_words_sak -= 7
        for i in range(7):
            print(f'{self.letters[i]} - {self.points[i]}, ', end="")

        print()

    def putbackletters(self):
        SakClass.total_words_sak += 7
        for i in range(7):
            SakClass.lets.get(self.letters[i])[0] += 1
        pass  # επιστρέφει γράμματα παίκτη στο σακουλάκι


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

    def __init__(self):
        self.points = 0

    def __repr__(self):
        pass

    def play(self, sak, words, score):
        while True:
            answer = input("Δώσε την λέξη ή 'p' (για pass): ")
            if answer == 'p':
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
        if answer.upper() == 'P':  # επελεξε pass
            sak.putbackletters()
        elif answer.upper() in words:  # βρηκε σωστη λεξη
            print('Σωστή λέξη - Κέρδισες ', end='')
            for letter in answer:
                for i in range(len(sak.letters)):
                    if letter.upper() == sak.letters[i]:
                        round_points += sak.points[i]

            score += round_points
            print(round_points, 'Πόντους, Το Σκορ σου είναι: ', score)
            input('Enter για συνέχεια')
            print('--------------------------------------------------')
        else:  # βρηκε λαθος λεξη
            print('Λάθος λέξη')

        return round_points

class Computer(Player):
    """
        περιγράφει το πως παίζει ο υπολογιστής
    """

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def play(self):
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
