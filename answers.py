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

if __name__ == "__main__":
    ask_user(answers)