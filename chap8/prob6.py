import random

print("                Welcome to Trivia Challenge!\n")
print("                An Episode You Can't Refuse\n\n")

quiz = {
    1: {
        'category': 'On the Run With a Mamma1',
        'question': 'Let\'s say you turn state\'s evidence and need to \"get on the lamb.\" If you wait too long, what will happen?',
        'answer': ['        1 - You\'ll end up on the sheep', '        2 - You\'ll end up on the cow', '        3 - You\'ll end up on the goat', '        4 - You\'ll end up on the emu'],
        'correct_answer': '1',
        'explanation': 'Answer is 1. I don\'t know what the question says. But lamb is sheep.'
    },
    2: {
        'category': 'What is my favorite ramen',
        'question': 'I like ramen with thick noodles. What is my favorite ramen?',
        'answer': ['        1 - Shin Ramen', '        2 - Neoguli', '        3 - Hot Chicken Flavor Ramen', '        4 - Yukejang'],
        'correct_answer': '2',
        'explanation': 'Answer is 2. I like Neoguli with thick noodles the most.'
    },
    3: {
        'category': 'How old am I',
        'question': 'I was born in 2001. How old am I?',
        'answer': ['        1 - 21', '        2 - 22', '        3 - 23', '        4 - 24'],
        'correct_answer': '3',
        'explanation': 'Answer is 3. hahaha~'
    }
}

def quiz_start(quiz, number):
    Q = quiz[number]
    print(Q['category'] + "\n")
    print(Q['question'] + "\n")
    for answer_list in Q['answer']:
        print(answer_list + "\n")
    user_answer = input('What\'s your answer?: ').strip()
    if user_answer == Q['correct_answer']:
        print('Correct! ' + Q['explanation'] + "\n\n")
    else:
        print('Incorrect. ' + Q['explanation'] + "\n\n")


quiz_number = list(quiz.keys())
random.shuffle(quiz_number)

for number in quiz_number:
    quiz_start(quiz, number)
print("\n\nPress the enter key to exit.")
