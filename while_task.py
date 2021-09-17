
#task 1
names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
i = 0
while i <= len(names):
    if names.pop(i) == 'Валера':
        print("Валера нашелся!")
        break

#task 2
names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(name):
    if name == "Валера":
        print("Валера нашелся!")

i = 0
while i < len(names):
    find_person(names.pop(i))

#task 3
answers = {
    'Привет': 'Привет',
    'Как дела?': 'Отлично, а у тебя?',
    'Пока': 'Еще увидимся'
}

def get_answer(question, answers):
    return answers.get(question)

def ask_user(answers):
    while True:
        try:
            user_input = input("Начнем? ")
            answer = get_answer(user_input, answers)
            print(answer)
            if user_input.capitalize() == 'Пока':
                break
        except KeyboardInterrupt:
            print("Как жаль что уже уходите!")
            break

ask_user(answers)

