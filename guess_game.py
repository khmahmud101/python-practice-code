secret_num = 9
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess_num = int(input("Guess Number:"))
    guess_count+=1
    if guess_num == secret_num:
        print("you win!")
        break
else:
    print("Sorry you failed")





