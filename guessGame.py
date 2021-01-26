secretWord = "Mustafa"
guessGame = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guessGame !=secretWord and not (out_of_guesses):
    if guess_count < guess_limit:
        guessGame = input("Введи слово: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Limit of guess")
else:
    print("ТЫ выиграл")
