import random
import time
total_questions = 10
score = 0
for ques_no in range(total_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    product = num1 * num2
    i = 0
    time_1 = time.time()
    while i < 3:
        answer = input(f"Q{ques_no + 1}: {num1} x {num2} = ")
        time_2 = time.time()
        if time_2 - time_1 <= 10:
            try:
                if int(answer) != product and i < 2:
                    print("Incorrect!")
                    i += 1
                    continue
                if int(answer) != product and i == 2:
                    print("Incorrect!")
                    print("You are Out of Tries.")
                    i += 1
                if int(answer) == product:
                    print("Correct!")
                    score += 1
                    break
            except ValueError:
                print("Please Enter Numeric Digits.")
                i += 1
        else:
            print('Your are out of time!')
            break
print(f"Your score is: {score}/{total_questions}")
