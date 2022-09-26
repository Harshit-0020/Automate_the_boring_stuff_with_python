print("Guess the number I have in my mind !!!")
secret_number = 9
guess_count = 1
guess_limit = 3
while guess_count <= guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Win!")
        break
else:
    print("You failed.")