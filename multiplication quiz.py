import time
import pyinputplus as pi
import random
no_of_questions = 10
correct_ans = 0
for que_number in range(1, no_of_questions+1):
    try:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        product = num1 * num2
        pi.inputNum(prompt=f"Q{que_number}: {num1} x {num2} = ", limit=3, timeout=8, allowRegexes=[fr'^{product}$'],
                    blockRegexes=[('.*', 'Incorrect!')])
    except pi.TimeoutException:
        print('Out of time!')
    except pi.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correct_ans += 1
    time.sleep(1)  # Brief pause to let the user see the result.
print(f"Score: {correct_ans}/{no_of_questions}")
