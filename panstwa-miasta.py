import random


def play_game():
    categories = {
        "Państwa": ["Polska", "Niemcy", "Francja", "Włochy", "Hiszpania"],
        "Miasta": ["Warszawa", "Berlin", "Paryż", "Rzym", "Madryt"],
        "Zwierzęta": ["Pies", "Kot", "Słoń", "Tygrys", "Żyrafa"],
    }

    while True:
        category = random.choice(list(categories.keys()))
        print("Kategoria:", category)

        word = random.choice(categories[category])
        print("Wylosowane słowo:", word)

        input("Naciśnij Enter, aby kontynuować...")

        print("Czas start!")
        print("Twoje odpowiedzi powinny zaczynać się na literę:", word[0])

        player_answers = {}

        for category, words in categories.items():
            if category == "Państwa" or category == "Miasta":
                prompt = f"Podaj {category.lower()}: "
            else:
                prompt = f"Podaj zwierzęta z literą {word[0]}: "

            answer = input(prompt)
            player_answers[category] = answer

        print("\nOdpowiedzi gracza:")
        for category, answer in player_answers.items():
            print(f"{category}: {answer}")

        input("\nNaciśnij Enter, aby poznać poprawne odpowiedzi...")

        print("\nPoprawne odpowiedzi:")
        for category, words in categories.items():
            print(f"{category}: {words}")

        play_again = input("\nCzy chcesz zagrać ponownie? (t/n): ")
        if play_again.lower() != "t":
            print("Dziękujemy za grę!")
            break


if __name__ == "__main__":
    play_game()
