import random

play = True

def random_number(a,b):
    return random.randint(a,b)

while play:
    print("Válaszd ki mit szeretnél:")
    choice = input("Új játék (new), kilépés(exit)  - ")
    
    guessed_numbers = []
    
    if choice == "new":
        too_low = "A megadott szám túl kicsi. Próbáld újra!"
        too_high = "A megadott szám túl magas. Próbáld újra!"
        congrat = "Nagyon szuper! Eltaláltad! Próbálkozásaid száma: "
        serious = "Ez most komoly? Ezt a számot már próbáltad."
        
        print("Válaszd ki, mely számok között szeretnél találgatni:")
        a = int(input("Szám-tól:  - "))
        b = int(input("Szám-ig:  - "))
        guess = int()
        tries = 0
        random_number = random_number(a,b)
        
        while guess != random_number:
            guess = int(input("Melyik számra gondoltam?  - "))
                        
            if guess in guessed_numbers:
                tries += 1
                print(serious)
            elif guess < random_number:
                tries += 1
                guessed_numbers.append(guess)
                print(too_low)
            elif guess > random_number:
                tries += 1
                guessed_numbers.append(guess)
                print(too_high)
            else:
                tries += 1
                print(f"{congrat}{tries}")
    else:
        play = False
