import random
from colorama import Fore, init

class Mazmorra:
    def __init__(self):
        self.heroes = ['A', 'G', 'M']
        self.monsters = ['O', 'E', 'Z', 'W', 'N', 'F', 'D', 'V', 'B', 'I', 'L']
        self.objects = ['C', 'P', 'T']

    def generate_mazmorra(self):
        mazmorra = []
        mazmorra.append(random.choice(self.heroes))
        mazmorra.extend(random.sample(self.monsters, 2))
        mazmorra.append(random.choice(self.objects))
        random.shuffle(mazmorra)
        return mazmorra

    def check_guess(self, mazmorra, guess):
        result = []
        for i, piece in enumerate(guess):
            if piece == mazmorra[i]:
                result.append(Fore.GREEN + piece)
            elif piece in mazmorra:
                result.append(Fore.YELLOW + piece)
            else:
                result.append(Fore.RED + piece)
        return result

    def play_game(self):
        mazmorra = self.generate_mazmorra()
        for i in range(6):  
            guess = input("Ingresa tu suposición (5 piezas): ")
            guess = list(guess.upper())  
            result = self.check_guess(mazmorra, guess)
            print(' '.join(result))
            if result.count(Fore.GREEN + 'Verde') == 5:
                print(Fore.GREEN + "¡Enhorabuena! ¡Has ganado!")
                break
        else:
            print(Fore.RED + "Lo siento, perdiste. La respuesta correcta era:", ''.join(mazmorra))
            play_again = input("¿Quieres jugar de nuevo? (s/n): ")
            if play_again.lower() == 's':
                self.play_game()

if __name__ == '__main__':
    init()
    mazmorra = Mazmorra()
    mazmorra.play_game()
