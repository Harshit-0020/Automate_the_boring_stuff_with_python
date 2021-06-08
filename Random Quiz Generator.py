import os
import random
os.chdir('C:\\Users\\harsh\\Desktop\\quiz&answers')
capitals = {
    'Andhra Pradesh': 'Hyderabad',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Gujrat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerela': 'Thiruvananthpuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizwal',
    'Nagaland': 'Kohima',
    'Odishs': 'Bhubaneshwar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lukhnow',
    'Uttarakhand (summer)': 'Gairsain',
    'Uttarakhand (winter)': 'Dehradun',
    'West Bengal': 'Kolkata'
}
for quizNum in range(50):
    quizFile = open(f"capitalsQuiz{quizNum + 1}.txt", 'w')
    answerFile = open(f"capital_quiz_anwers{quizNum +1}.txt", 'w')
    quizFile.write('Name:\nDate:\nPeriod:\n\n')
    quizFile.write((' ' * 50) + f"State Capitals Quiz (Form - {quizNum + 1})\n\n")
    states = list(capitals.keys())
    random.shuffle(states)
    for quesNum in range(len(states)):
        correct_answer = capitals[states[quesNum]]
        wrong_answer = list(capitals.values())
        wrong_answer.remove(correct_answer)
        wrong_answer = random.sample(wrong_answer, 3)
        answers = wrong_answer + [correct_answer]
        random.shuffle(answers)
        quizFile.write(f"Q{quesNum + 1}: What is the capital of {states[quesNum]}:\n")
        for i in range(4):
            quizFile.write(f"{'ABCD'[i]}" + ') ' + answers[i] + '\n')
        quizFile.write('\n')
        answerFile.write(f"{quesNum + 1}: {'ABCD'[answers.index(correct_answer)]}\n")
    quizFile.close()
    answerFile.close()
